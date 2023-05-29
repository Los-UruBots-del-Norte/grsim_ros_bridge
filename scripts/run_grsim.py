#! /usr/bin/env python3
import rospy
import rospkg
import os
#this variable takes the value of the variable home eg: /home/ricardo/ssl_ws
my_home = os.environ.get('SSL_WS_HOME')

myCmd = my_home +'/src/grSim/bin/grSim'
os.system(myCmd)
