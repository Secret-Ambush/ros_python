from robot_control_class import RobotControl

rc = RobotControl()

laser1 = rc.get_laser(0)
print ("The laser value received is: ", laser1)

laser2 = rc.get_laser(360)
print ("The laser value received is: ", laser2)

laser2 = rc.get_laser(719)
print ("The laser value received is: ", laser2)