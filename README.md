# grsim_ros_bridge

## Prerequisites

install the official SSL simulator from 
[grSim](https://github.com/RoboCup-SSL/grSim).
```bash
git clone git@github.com:RoboCup-SSL/grSim.git
```
and follow its [installation instructions](https://github.com/RoboCup-SSL/grSim/blob/master/INSTALL.md)


## Installation
To Install:
```bash
git clone git@github.com:Los-UruBots-del-Norte/vision_comm.git
git clone git@github.com:Los-UruBots-del-Norte/grsim_ros_bridge.git
git clone git@github.com:Los-UruBots-del-Norte/grsim_ros_bridge_msgs.git
git clone git@github.com:KRSSG/krssg_ssl_msgs.git
```
After clonning install:
testresources needed for ErForce
```bash
pip install grsim_ros_bridge/ssl-python-clients/
```
 Export an eviroment variable setting your ssl_ws home.
 Example given: if my ws directory is "/home/ricardo/testssl_ws" use: 
 ```bash
 export SSL_WS_HOME ='/home/ricardo/testssl_ws'
```


## Running
```bash
roslaunch grsim_ros_bridge launch.launch
```
