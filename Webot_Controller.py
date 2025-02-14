"""simulation_code controller."""

# this is the file we run on the simulation controller. It is responsible for
# making the robot translate the optimum path and follow it smoothly 

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, InertialUnit, Motor
import numpy as np
import operator

#-------------------------------------------------------
# Initialize variables

MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 1   # [ms]

# Creat a variable to define all possible states
states = ['Wait', 'Turn', 'Straight']
curent_state = 'Wait'      # This is the active state

# counter: used to maintain an active state for a number of cycles
counter = 0
COUNTER_MAX = 5
wait = 0

#-------------------------------------------------------
# Initialize devices

# distance sensors

# motors    
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

#GPS
gps = robot.getDevice('gps')
gps.enable(timestep)

#compass
compass = robot.getDevice('compass')
compass.enable(timestep)


#-------------------------------------------------------
# Dictionariec

coordinates = {
    'A': [0.5203909068940236, 0.7805592126409339, 0.04853610061240178],
    'B': [0.5597847533284892, 0.44087441460550786, 0.04839428959255795],
    'C': [0.6989737559164702, 0.09095825789060932, 0.04823721545492198],
    'D': [0.6972319029472618, -0.738861358107975, 0.04790640157889506],
    'E': [0.03126182671058787, 1.102539611090158, 0.0485154734258905],
    'F': [0.2300785806879423, 0.64235539593765, 0.048529278294856946],
    'G': [0.2569465483486195, -0.5975979196842485, 0.04851639968691315],
    'H': [0.2559722616159768, -0.9872393772263438, 0.04850244181562907],
    'I': [-0.18985272215357266, 0.6338164696592195, 0.04853705745872092],
    'J': [-0.2016783780733591, -0.0859521525366429, 0.04853443634826586],
    'K': [-0.43364725882916866, -0.8852003817695542, 0.04853731357176925],
    'L': [-0.5595907093102195, 0.7750336148587058, 0.048535406211242665],
    'M': [-0.5512707914349618, 0.09522618182659003, 0.04853645014210037],
    'N': [-0.553345232850511, -0.7445959364841807, 0.04853588622360096],
    'AA': [0.4610989066500465, 0.7728309848505983, 0.04853626770790887],
    'AB': [0.46030608536746886, 0.44324707665875696, 0.04853481712406783],
    'AC': [0.4594938941623827, 0.10365385833167022, 0.048535742449618835],
    'AD': [0.4574749339967083, -0.7361677531211916, 0.04853507495542517],
    'AE': [0.25110994199120207, 0.7742366255575546, 0.04853751186367089],
    'AF': [0.26747511970235854, -0.7357049044535611, 0.04853553844557308],
    'AG': [0.031141478080765096, 0.7747714236237475, 0.04853981532272726],
    'AH': [0.02946558684566663, 0.0949894747832652, 0.048533213364366244],
    'AI': [0.027466946167653758, -0.7448325492155052, 0.048537496858779214],
    'AJ': [-0.17889000655709533, 0.7755732777298124, 0.04850857626704836],
    'AK': [-0.2016783780733591, 0.0949894747832652, 0.04853449814485199],
    'AL': [-0.4388255510037137, 0.776212651940659, 0.04851948163119511],
    'AM': [-0.4404964977310851, 0.09642479749101536, 0.048478422945366105],
    'AN': [-0.44257561883930274, -0.7433928184193558, 0.04853449814485199]
}

#-------------------------------------------------------
# Extra functions:

def direction(rotation, compass_value):
    con1 = compass_value == [1.0, 0.0, 0.0] and rotation == [0.0, -1.0, 0.0]
    con2 = compass_value == [-1.0, 0.0, 0.0] and rotation == [0.0, 1.0, 0.0]
    con3 = compass_value == [0.0, 1.0, 0.0] and rotation == [1.0, 0.0, 0.0]
    con4 = compass_value == [0.0, -1.0, 0.0] and rotation == [-1.0, 0.0, 0.0]
    
    if con1 or con2 or con3 or con4:
        return 'left'
    else:
        return 'right'


def translaton(start, stop):
    y_dif = coordinates[stop][1] - coordinates[start][1]
    x_dif = coordinates[stop][0] - coordinates[start][0]
    
    if abs(y_dif) > abs(x_dif):
        if y_dif > 0:
            return [1.0, 0.0, 0.0], 1, coordinates[stop][1], 'Turn', operator.ge
        else:
            return [-1.0, 0.0, 0.0], 1, coordinates[stop][1], 'Turn', operator.le
    else:
        if x_dif > 0:
            return [0.0, 1.0, 0.0], 0, coordinates[stop][0], 'Turn', operator.ge
        else:
            return [0.0, -1.0, 0.0], 0, coordinates[stop][0], 'Turn', operator.le


#-------------------------------------------------------
# Optimazation algorethemz:

def next_path(i):
    que = [('A', 'AA'),
  ('AA', 'AB'),
  ('AB', 'B'),
  ('B', 'AB'),
  ('AB', 'AC'),
  ('AC', 'AD'),
  ('AD', 'AF'),
  ('AF', 'G'),
  ('G', 'AF'),
  ('AF', 'AI'),
  ('AI', 'AN'),
  ('AN', 'K'),
  ('K', 'AN'),
  ('AN', 'AI'),
  ('AI', 'AH'),
  ('AH', 'AG'),
  ('AG', 'AE'),
  ('AE', 'F'),
  ('F', 'AE'),
  ('AE', 'AA'),
  ('AA', 'A')]
  
  
    return que[i]
#-------------------------------------------------------
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    
    if curent_state == 'Turn':
        

        compass_value = compass.getValues()
        compass_value = [round(num, 2) for num in compass_value]
        compass_value = [0 if num == -0.0 else num for num in compass_value]
                                
        if rotation == compass_value:
            leftSpeed  = 0
            rightSpeed = 0
            curent_state = 'Straight'
        elif direc == 'right':
            leftSpeed  = 0.05 * MAX_SPEED
            rightSpeed = -0.05 * MAX_SPEED
        elif direc == 'left':
            leftSpeed  = -0.05 * MAX_SPEED
            rightSpeed = 0.05 * MAX_SPEED
        
    elif curent_state == 'Straight':
        leftSpeed  = 0.5 * MAX_SPEED
        rightSpeed = 0.5 * MAX_SPEED
        
        gps_value = gps.getValues()
        
        if oper(gps_value[axies], finish):
            leftSpeed  = 0
            rightSpeed = 0
            counter += 1
            curent_state = 'Wait'
        
    elif curent_state == 'Wait':
        leftSpeed  = 0
        rightSpeed = 0
        
        """ 
        code for the algorethems
        """
        try:
            start, stop = next_path(counter)
        except:
            print('Robot has reached its destination')
        
        rotation, axies, finish, curent_state, oper = translaton(start, stop)

        compass_value = compass.getValues()
        compass_value = [round(num, 2) for num in compass_value]
        compass_value = [0 if num == -0.0 else num for num in compass_value]
        
        direc = direction(rotation, compass_value)
    #print(curent_state)

    # increment counter
    #counter += 1
    
    #print('Counter: '+ str(counter) + '. Current state: ' + current_state)

    # Set motor speeds with the values defined by the state-machine
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)

    # Repeat all steps while the simulation is running.
