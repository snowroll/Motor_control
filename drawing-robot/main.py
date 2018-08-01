from draw import *
import sys, os, time
try:
    import vrep
except:
    print ('--------------------------------------------------------------')
    print ('"vrep.py" could not be imported. This means very probably that')
    print ('either "vrep.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "vrep.py"')
    print ('--------------------------------------------------------------')
    print ('')


def cache_sa(paths):
    npy = 'solution.npy'
    # if os.path.exists(npy):
    #     print('using existing solution')
    #     return np.load(npy).tolist()
    # else:
    sol = simulated_annealing(paths)
    np.save(npy, sol)
    return sol


vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5) # Connect to V-REP
if clientID == -1:
    print('Failed connecting to remote API server')
    sys.exit(1)
print ('Connected to remote API server')


imgname = '../Data/slam.jpg'
while True:
    if os.path.exists(imgname) == False:
        time.sleep(1)
    else:
        break

edgeimg = canny(imgname) // 255
# edgeimg = cv2.imread('face edge.png')[:, :, 0] // 255
paths = PathList(edgeimg)

print('total path: ', len(paths))
print('origin dist:', paths.tot_dist())

bestsol = cache_sa(paths)
print('sa dist:', paths.tot_dist(bestsol))
paths.solution = bestsol

#paths.solution = [[84*2+1,84*2]]
pathlist = paths.tolist()
print('path list len:', len(pathlist))
strlist = vrep.simxPackInts(pathlist)
vrep.simxSetStringSignal(clientID, 'paths', strlist, vrep.simx_opmode_oneshot)


# close the connection to V-REP:
vrep.simxGetPingTime(clientID)
vrep.simxFinish(clientID)