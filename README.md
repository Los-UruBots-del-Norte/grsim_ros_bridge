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
 Modify src/grsim_ros_bridge/scripts/run_grsim.py setting your path in: 
 ```python
 myCmd = my_home +'/testssl_ws/src/grSim/bin/grSim'
```


## Running
```bash
roslaunch grsim_ros_bridge launch.launch
```
