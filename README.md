# Motor_control
project -- getsture control, vrep UAV control(pd, pid), Qt-client, 2D slam
gesutre model and all code can found in the release
##### run method:  
- server: 
cd Motor_control   
python run_model.py [pid] [control]
(default use pd algorithm to control UAV and use qt-client show result)
- client: 
cd Motor_control/Qt-client  
python client.py
(program will connect to v-rep automaticly)

remoteApi.so is for linux, if you run in other system, you need to change the file

