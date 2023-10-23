from robot_control_class import RobotControl

robotcontrol = RobotControl()

l = robotcontrol.get_laser_full()

maximum = 0

for value in l:
    if value > maximum:
        maximum = value

print ("The higher value in the list is: ", maximum)