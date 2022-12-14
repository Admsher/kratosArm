#!/usr/bin/env python3
import rospy
from std_msgs import Float64
from sensor_msgs.msg import Joy
import math


class ik():

    def __init__(self):
        self.x = 0
        self.y = 0
        rospy.init_node('ik', anonymous=True)

    def callback(self,data):
        self.x -= data.axes[0]
        self.y += data.axes[1]
        rospy.loginfo(self.x)
        rospy.loginfo(self.y)
        self.a6 = 1
        self.a4 = 1 
        self.h = 60 #fixed angle wrt a6
        self.k = 0.3 #fixed length wrt a6
        self.j = 0.1 #fixed length wrt a4
        self.theta4 = (-1* math.acos(((self.x**2) + (self.y**2) - (self.a6**2) - (self.a4**2))/(2*self.a6*self.a4)))*180/math.pi
        print(self.theta4*180/math.pi)
        self.theta6 = (math.atan(self.y/self.x) + math.atan((self.a4*math.sin(self.theta4))/(self.a6+(self.a4*math.cos(self.theta4)))))*180/math.pi

        print("theta6 = ",self.theta6)
        print("theta4 = ",self.theta4)

        #self.l6 = math.sqrt((a6**2)+(h**2) - (2*a6*k*math.cos(180 - theta6 - h)))
        #self.l4 = math.sqrt((a4**2)+(i**2) - (2*a4*j*math.cos(180 - theta4)))
    def listener(self):
        rospy.Subscriber("/joy", Joy, self.callback)

    def publisher(self):
        self.pub4 = rospy.Publisher("inv_k",Float64,queue_size = 10)
        self.pub6 = rospy.Publisher("inv_k",Float64,queue_size = 10)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.pub.publish(self.theta4)
            self.pub.publish(self.theta6)
            rate.sleep()


if __name__ == '__main__':
    ik().listener()
    ik().publisher()

"""
x = float(input("Enter x"))
y = float(input("Enter y"))
a6 = 1
a4 = 1 
h = 60 #fixed angle wrt a6
k = 0.3 #fixed length wrt a6
j = 0.1 #fixed length wrt a4
theta4 = (-1* math.acos(((x**2) + (y**2) - (a6**2) - (a4**2))/(2*a6*a4)))*180/math.pi
print(theta4*180/math.pi)
theta6 = (math.atan(y/x) + math.atan((a4*math.sin(theta4))/(a6+(a4*math.cos(theta4)))))*180/math.pi

print("theta6 = ",theta6)
print("theta4 = ",theta4)

l6 = math.sqrt((a6**2)+(h**2) - (2*a6*k*math.cos(180 - theta6 - h)))
l4 = math.sqrt((a4**2)+(i**2) - (2*a4*j*math.cos(180 - theta4)))
"""sg.ModelStates, callback)


    rospy.spin()