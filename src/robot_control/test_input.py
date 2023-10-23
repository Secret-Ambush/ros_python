from robot_control_class import RobotControl

rc = RobotControl()

number = int(input("Enter a number: "))

a = rc.get_laser(number)

print("The laser value received is: ", a)
