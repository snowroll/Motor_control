import platform
import struct
import sys
import os
import ctypes as ct
from vrepConst import *

#load library
libsimx = None
try:
    file_extension = '.so'
    if platform.system() =='cli':
        file_extension = '.dll'
    elif platform.system() =='Windows':
        file_extension = '.dll'
    elif platform.system() == 'Darwin':
        file_extension = '.dylib'
    else:
        file_extension = '.so'
    libfullpath = os.path.join(os.path.dirname(__file__), 'remoteApi' + file_extension)
    libsimx = ct.CDLL(libfullpath)
except:
    print ('----------------------------------------------------')
    print ('The remoteApi library could not be loaded. Make sure')
    print ('it is located in the same folder as "vrep.py", or')
    print ('appropriately adjust the file "vrep.py"')
    print ('----------------------------------------------------')
    print ('')

#ctypes wrapper prototypes
c_GetJointPosition          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxGetJointPosition", libsimx))
c_SetJointPosition          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_float, ct.c_int32)(("simxSetJointPosition", libsimx))
c_GetJointMatrix            = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxGetJointMatrix", libsimx))
c_SetSphericalJointMatrix   = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxSetSphericalJointMatrix", libsimx))
c_SetJointTargetVelocity    = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_float, ct.c_int32)(("simxSetJointTargetVelocity", libsimx))
c_SetJointTargetPosition    = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_float, ct.c_int32)(("simxSetJointTargetPosition", libsimx))
c_GetJointForce             = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxGetJointForce", libsimx))
c_SetJointForce             = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_float, ct.c_int32)(("simxSetJointForce", libsimx))
c_ReadForceSensor           = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_ubyte), ct.POINTER(ct.c_float), ct.POINTER(ct.c_float), ct.c_int32)(("simxReadForceSensor", libsimx))
c_BreakForceSensor          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32)(("simxBreakForceSensor", libsimx))
c_ReadVisionSensor          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_ubyte), ct.POINTER(ct.POINTER(ct.c_float)), ct.POINTER(ct.POINTER(ct.c_int32)), ct.c_int32)(("simxReadVisionSensor", libsimx))
c_GetObjectHandle           = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetObjectHandle", libsimx))
c_GetVisionSensorImage      = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.POINTER(ct.POINTER(ct.c_byte)), ct.c_ubyte, ct.c_int32)(("simxGetVisionSensorImage", libsimx))
c_SetVisionSensorImage      = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_byte), ct.c_int32, ct.c_ubyte, ct.c_int32)(("simxSetVisionSensorImage", libsimx))
c_GetVisionSensorDepthBuffer= ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.POINTER(ct.POINTER(ct.c_float)), ct.c_int32)(("simxGetVisionSensorDepthBuffer", libsimx))
c_GetObjectChild            = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetObjectChild", libsimx))
c_GetObjectParent           = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetObjectParent", libsimx))
c_ReadProximitySensor       = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_ubyte), ct.POINTER(ct.c_float), ct.POINTER(ct.c_int32), ct.POINTER(ct.c_float), ct.c_int32)(("simxReadProximitySensor", libsimx))
c_LoadModel                 = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.c_ubyte, ct.POINTER(ct.c_int32), ct.c_int32)(("simxLoadModel", libsimx))
c_LoadUI                    = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.c_ubyte, ct.POINTER(ct.c_int32), ct.POINTER(ct.POINTER(ct.c_int32)), ct.c_int32)(("simxLoadUI", libsimx))
c_LoadScene                 =  ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.c_ubyte, ct.c_int32)(("simxLoadScene", libsimx))
c_StartSimulation           = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32)(("simxStartSimulation", libsimx))
c_PauseSimulation           = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32)(("simxPauseSimulation", libsimx))
c_StopSimulation            = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32)(("simxStopSimulation", libsimx))
c_GetUIHandle               = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetUIHandle", libsimx))
c_GetUISlider               = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetUISlider", libsimx))
c_SetUISlider               = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.c_int32, ct.c_int32)(("simxSetUISlider", libsimx))
c_GetUIEventButton          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetUIEventButton", libsimx))
c_GetUIButtonProperty       = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetUIButtonProperty", libsimx))
c_SetUIButtonProperty       = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.c_int32, ct.c_int32)(("simxSetUIButtonProperty", libsimx))
c_AddStatusbarMessage       = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.c_int32)(("simxAddStatusbarMessage", libsimx))
c_AuxiliaryConsoleOpen      = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.POINTER(ct.c_int32), ct.POINTER(ct.c_float), ct.POINTER(ct.c_float), ct.POINTER(ct.c_int32), ct.c_int32)(("simxAuxiliaryConsoleOpen", libsimx))
c_AuxiliaryConsoleClose     = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32)(("simxAuxiliaryConsoleClose", libsimx))
c_AuxiliaryConsolePrint     = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_char), ct.c_int32)(("simxAuxiliaryConsolePrint", libsimx))
c_AuxiliaryConsoleShow      = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_ubyte, ct.c_int32)(("simxAuxiliaryConsoleShow", libsimx))
c_GetObjectOrientation      = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxGetObjectOrientation", libsimx))
c_GetObjectQuaternion       = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxGetObjectQuaternion", libsimx))
c_GetObjectPosition         = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxGetObjectPosition", libsimx))
c_SetObjectOrientation      = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxSetObjectOrientation", libsimx))
c_SetObjectQuaternion       = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxSetObjectQuaternion", libsimx))
c_SetObjectPosition         = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxSetObjectPosition", libsimx))
c_SetObjectParent           = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.c_ubyte, ct.c_int32)(("simxSetObjectParent", libsimx))
c_SetUIButtonLabel          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_char), ct.c_int32)(("simxSetUIButtonLabel", libsimx))
c_GetLastErrors             = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_int32), ct.POINTER(ct.POINTER(ct.c_char)), ct.c_int32)(("simxGetLastErrors", libsimx))
c_GetArrayParameter         = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxGetArrayParameter", libsimx))
c_SetArrayParameter         = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxSetArrayParameter", libsimx))
c_GetBooleanParameter       = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_ubyte), ct.c_int32)(("simxGetBooleanParameter", libsimx))
c_SetBooleanParameter       = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_ubyte, ct.c_int32)(("simxSetBooleanParameter", libsimx))
c_GetIntegerParameter       = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetIntegerParameter", libsimx))
c_SetIntegerParameter       = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.c_int32)(("simxSetIntegerParameter", libsimx))
c_GetFloatingParameter      = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxGetFloatingParameter", libsimx))
c_SetFloatingParameter      = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_float, ct.c_int32)(("simxSetFloatingParameter", libsimx))
c_GetStringParameter        = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.POINTER(ct.c_char)), ct.c_int32)(("simxGetStringParameter", libsimx))
c_GetCollisionHandle        = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetCollisionHandle", libsimx))
c_GetDistanceHandle         = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetDistanceHandle", libsimx))
c_GetCollectionHandle       = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetCollectionHandle", libsimx))
c_ReadCollision             = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_ubyte), ct.c_int32)(("simxReadCollision", libsimx))
c_ReadDistance              = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxReadDistance", libsimx))
c_RemoveObject              = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32)(("simxRemoveObject", libsimx))
c_RemoveModel               = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32)(("simxRemoveModel", libsimx))
c_RemoveUI                  = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32)(("simxRemoveUI", libsimx))
c_CloseScene                = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32)(("simxCloseScene", libsimx))
c_GetObjects                = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.POINTER(ct.POINTER(ct.c_int32)), ct.c_int32)(("simxGetObjects", libsimx))
c_DisplayDialog             = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_char), ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_float), ct.POINTER(ct.c_float), ct.POINTER(ct.c_int32), ct.POINTER(ct.c_int32), ct.c_int32)(("simxDisplayDialog", libsimx))
c_EndDialog                 = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32)(("simxEndDialog", libsimx))
c_GetDialogInput            = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.POINTER(ct.c_char)), ct.c_int32)(("simxGetDialogInput", libsimx))
c_GetDialogResult           = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetDialogResult", libsimx))
c_CopyPasteObjects          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_int32), ct.c_int32, ct.POINTER(ct.POINTER(ct.c_int32)), ct.POINTER(ct.c_int32), ct.c_int32)(("simxCopyPasteObjects", libsimx))
c_GetObjectSelection        = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.POINTER(ct.c_int32)), ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetObjectSelection", libsimx))
c_SetObjectSelection        = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_int32), ct.c_int32, ct.c_int32)(("simxSetObjectSelection", libsimx))
c_ClearFloatSignal          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.c_int32)(("simxClearFloatSignal", libsimx))
c_ClearIntegerSignal        = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.c_int32)(("simxClearIntegerSignal", libsimx))
c_ClearStringSignal         = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.c_int32)(("simxClearStringSignal", libsimx))
c_GetFloatSignal            = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_float), ct.c_int32)(("simxGetFloatSignal", libsimx))
c_GetIntegerSignal          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetIntegerSignal", libsimx))
c_GetStringSignal           = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.POINTER(ct.c_ubyte)), ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetStringSignal", libsimx))
c_SetFloatSignal            = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.c_float, ct.c_int32)(("simxSetFloatSignal", libsimx))
c_SetIntegerSignal          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.c_int32, ct.c_int32)(("simxSetIntegerSignal", libsimx))
c_SetStringSignal           = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_ubyte), ct.c_int32, ct.c_int32)(("simxSetStringSignal", libsimx))
c_AppendStringSignal        = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_ubyte), ct.c_int32, ct.c_int32)(("simxAppendStringSignal", libsimx))
c_WriteStringStream         = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_ubyte), ct.c_int32, ct.c_int32)(("simxWriteStringStream", libsimx))
c_GetObjectFloatParameter   = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.c_int32)(("simxGetObjectFloatParameter", libsimx))
c_SetObjectFloatParameter   = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.c_float, ct.c_int32)(("simxSetObjectFloatParameter", libsimx))
c_GetObjectIntParameter     = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetObjectIntParameter", libsimx))
c_SetObjectIntParameter     = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.c_int32, ct.c_int32)(("simxSetObjectIntParameter", libsimx))
c_GetModelProperty          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetModelProperty", libsimx))
c_SetModelProperty          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.c_int32)(("simxSetModelProperty", libsimx))
c_Start                     = ct.CFUNCTYPE(ct.c_int32,ct.POINTER(ct.c_char), ct.c_int32, ct.c_ubyte, ct.c_ubyte, ct.c_int32, ct.c_int32)(("simxStart", libsimx))
c_Finish                    = ct.CFUNCTYPE(None, ct.c_int32)(("simxFinish", libsimx))
c_GetPingTime               = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_int32))(("simxGetPingTime", libsimx))
c_GetLastCmdTime            = ct.CFUNCTYPE(ct.c_int32,ct.c_int32)(("simxGetLastCmdTime", libsimx))
c_SynchronousTrigger        = ct.CFUNCTYPE(ct.c_int32,ct.c_int32)(("simxSynchronousTrigger", libsimx))
c_Synchronous               = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_ubyte)(("simxSynchronous", libsimx))
c_PauseCommunication        = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_ubyte)(("simxPauseCommunication", libsimx))
c_GetInMessageInfo          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32))(("simxGetInMessageInfo", libsimx))
c_GetOutMessageInfo         = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32))(("simxGetOutMessageInfo", libsimx))
c_GetConnectionId           = ct.CFUNCTYPE(ct.c_int32,ct.c_int32)(("simxGetConnectionId", libsimx))
c_CreateBuffer              = ct.CFUNCTYPE(ct.POINTER(ct.c_ubyte), ct.c_int32)(("simxCreateBuffer", libsimx))
c_ReleaseBuffer             = ct.CFUNCTYPE(None, ct.c_void_p)(("simxReleaseBuffer", libsimx))
c_TransferFile              = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_char), ct.c_int32, ct.c_int32)(("simxTransferFile", libsimx))
c_EraseFile                 = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.c_int32)(("simxEraseFile", libsimx))
c_GetAndClearStringSignal   = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.POINTER(ct.c_ubyte)), ct.POINTER(ct.c_int32), ct.c_int32)(("simxGetAndClearStringSignal", libsimx))
c_ReadStringStream          = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.POINTER(ct.c_ubyte)), ct.POINTER(ct.c_int32), ct.c_int32)(("simxReadStringStream", libsimx))
c_CreateDummy               = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_float, ct.POINTER(ct.c_ubyte), ct.POINTER(ct.c_int32), ct.c_int32)(("simxCreateDummy", libsimx))
c_Query                     = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.c_ubyte), ct.c_int32, ct.POINTER(ct.c_char), ct.POINTER(ct.POINTER(ct.c_ubyte)), ct.POINTER(ct.c_int32), ct.c_int32)(("simxQuery", libsimx))
c_GetObjectGroupData        = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.c_int32, ct.POINTER(ct.c_int32), ct.POINTER(ct.POINTER(ct.c_int32)), ct.POINTER(ct.c_int32), ct.POINTER(ct.POINTER(ct.c_int32)), ct.POINTER(ct.c_int32), ct.POINTER(ct.POINTER(ct.c_float)), ct.POINTER(ct.c_int32), ct.POINTER(ct.POINTER(ct.c_char)), ct.c_int32)(("simxGetObjectGroupData", libsimx))
c_GetObjectVelocity         = ct.CFUNCTYPE(ct.c_int32,ct.c_int32, ct.c_int32, ct.POINTER(ct.c_float), ct.POINTER(ct.c_float), ct.c_int32)(("simxGetObjectVelocity", libsimx))
c_CallScriptFunction        = ct.CFUNCTYPE(ct.c_int32,ct.c_int32,ct.POINTER(ct.c_char),ct.c_int32,ct.POINTER(ct.c_char),ct.c_int32,ct.POINTER(ct.c_int32),ct.c_int32,ct.POINTER(ct.c_float),ct.c_int32,ct.POINTER(ct.c_char),ct.c_int32,ct.POINTER(ct.c_ubyte),ct.POINTER(ct.c_int32), ct.POINTER(ct.POINTER(ct.c_int32)),ct.POINTER(ct.c_int32), ct.POINTER(ct.POINTER(ct.c_float)),ct.POINTER(ct.c_int32), ct.POINTER(ct.POINTER(ct.c_char)),ct.POINTER(ct.c_int32), ct.POINTER(ct.POINTER(ct.c_ubyte)),ct.c_int32)(("simxCallScriptFunction", libsimx))

#API functions
def simxGetJointPosition(clientID, jointHandle, operationMode):
    """
    (regular API equivalent: sim.getJointPosition)
    Retrieves the intrinsic position of a joint. This function cannot be used with spherical joints (use simxGetJointMatrix instead). See also simxSetJointPosition and simxGetObjectGroupData.
    number returnCode,number position=simxGetJointPosition(number clientID,number jointHandle,number operationMode)
    
    :param clientID: the client ID. refer to simxStart.
    :param jointHandle: handle of the joint
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)
    
    :return returnCode: a remote API function return code
    :return position: intrinsic position of the joint. This is a one-dimensional value: if the joint is revolute, the rotation angle is returned, if the joint is prismatic, the translation amount is returned, etc.
    """
    position = ct.c_float()
    return c_GetJointPosition(clientID, jointHandle, ct.byref(position), operationMode), position.value

def simxSetJointPosition(clientID, jointHandle, position, operationMode):
    """
    (regular API equivalent: sim.setJointPosition)
    Sets the intrinsic position of a joint. May have no effect depending on the joint mode. This function cannot be used with spherical joints (use simxSetSphericalJointMatrix instead). If you want to set several joints that should be applied at the exact same time on the V-REP side, then use simxPauseCommunication. See also simxGetJointPosition and simxSetJointTargetPosition.
    number returnCode=simxSetJointPosition(number clientID,number jointHandle,number position,number operationMode)
    
    :param clientID: the client ID. refer to simxStart.
    :param jointHandle: handle of the joint
    :param position: position of the joint (angular or linear value depending on the joint type)
    :param 
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_oneshot or 
    :param simx_opmode_streaming
    
    :return returnCode: a remote API function return code
    """

    return c_SetJointPosition(clientID, jointHandle, position, operationMode)

def simxGetJointMatrix(clientID, jointHandle, operationMode):
    """
    (regular API equivalent: sim.getJointMatrix)
    Retrieves the intrinsic transformation matrix of a joint (the transformation caused by the joint movement). See also simxSetSphericalJointMatrix.
    number returnCode,array matrix=simxGetJointMatrix(number clientID,number jointHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param jointHandle: handle of the joint
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return matrix: array containing 12 values. See the regular API equivalent function for details
    """
    matrix = (ct.c_float*12)()
    ret = c_GetJointMatrix(clientID, jointHandle, matrix, operationMode)
    arr = []
    for i in range(12):
        arr.append(matrix[i])
    return ret, arr

def simxSetSphericalJointMatrix(clientID, jointHandle, matrix, operationMode):
    """
    (regular API equivalent: sim.setSphericalJointMatrix)
    Sets the intrinsic orientation matrix of a spherical joint object. This function cannot be used with non-spherical joints (use simxSetJointPosition instead). See also simxGetJointMatrix..
    number returnCode=simxSetSphericalJointMatrix(number clientID,number jointHandle,array matrix,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param jointHandle: handle of the joint
    :param matrix: 12  values. See the regular API equivalent function for details
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_oneshot or
    :param simx_opmode_streaming

    :return returnCode: a remote API function return code
    """
    matrix = (ct.c_float*12)(*matrix)
    return c_SetSphericalJointMatrix(clientID, jointHandle, matrix, operationMode)

def simxSetJointTargetVelocity(clientID, jointHandle, targetVelocity, operationMode):
    """
    (regular API equivalent: sim.setJointTargetVelocity)
    Sets the intrinsic target velocity of a non-spherical joint. This command makes only sense when the joint mode is in torque/force mode: the dynamics functionality and the joint motor have to be enabled (position control should however be disabled)
    number returnCode=simxSetJointTargetVelocity(number clientID,number jointHandle,number targetVelocity,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param jointHandle: handle of the joint
    :param targetVelocity: target velocity of the joint (linear or angular velocity depending on the joint-type)
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_oneshot or
    :param simx_opmode_streaming

    :return returnCode: a remote API function return code
    """

    return c_SetJointTargetVelocity(clientID, jointHandle, targetVelocity, operationMode)

def simxSetJointTargetPosition(clientID, jointHandle, targetPosition, operationMode):
    """
    (regular API equivalent: sim.setJointTargetPosition)
    Sets the target position of a joint if the joint is in torque/force mode (also make sure that the joint's motor and position control are enabled). See also simxSetJointPosition.
    number returnCode=simxSetJointTargetPosition(number clientID,number jointHandle,number targetPosition,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param jointHandle: handle of the joint
    :param targetPosition: target position of the joint (angular or linear value depending on the joint type)
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_oneshot or
    :param simx_opmode_streaming

    :return returnCode: a remote API function return code
    """

    return c_SetJointTargetPosition(clientID, jointHandle, targetPosition, operationMode)

def simxJointGetForce(clientID, jointHandle, operationMode):
    """
    (DEPRECATED)
    DEPRECATED. See simxGetJointForce instead.
    number returnCode,number force=simxJointGetForce(number clientID,number jointHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param jointHandle: handle of the joint
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return force: the force or the torque applied to the joint  along/about its z-axis
    """
    force = ct.c_float()
    return c_GetJointForce(clientID, jointHandle, ct.byref(force), operationMode), force.value

def simxGetJointForce(clientID, jointHandle, operationMode):
    """
    (regular API equivalent: sim.getJointForce)
    Retrieves the force or torque applied to a joint  along/about its active axis. This function retrieves meaningful information only if the joint is prismatic or revolute, and is dynamically enabled. With the Bullet engine, this function returns the force or torque applied to the joint motor  (torques from joint limits are not taken into account). With the ODE or Vortex engine, this function returns the total force or torque applied to a joint  along/about its z-axis. See also simxSetJointForce,  simxReadForceSensor and simxGetObjectGroupData.
    number returnCode,number force=simxGetJointForce(number clientID,number jointHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param jointHandle: handle of the joint
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return force: the force or the torque applied to the joint  along/about its z-axis
    """
    force = ct.c_float()
    return c_GetJointForce(clientID, jointHandle, ct.byref(force), operationMode), force.value

def simxSetJointForce(clientID, jointHandle, force, operationMode):
    """
    (regular API equivalent: sim.setJointForce)
    Sets the maximum force or torque that a joint can exert. This function has no effect when the joint is not dynamically enabled, or when it is a spherical joint. See also simxGetJointForce.
    number returnCode=simxSetJointForce(number clientID,number jointHandle,number force,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param jointHandle: handle of the joint
    :param force: the maximum force or torque that the joint can exert
    :param
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """
    return c_SetJointForce(clientID, jointHandle, force, operationMode)

def simxReadForceSensor(clientID, forceSensorHandle, operationMode):
    """
    (regular API equivalent: sim.readForceSensor)
    Reads the force and torque applied to a force sensor (filtered values are read), and its current state ('unbroken' or 'broken'). See also simxBreakForceSensor,  simxGetJointForce and simxGetObjectGroupData.
    number returnCode,number state,array forceVector,array torqueVector=simxReadForceSensor(number clientID,number forceSensorHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param forceSensorHandle: handle of the force sensor
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return state: the state of the force sensor
    :return bit 0 set: force and torque data is available, otherwise it is not (yet) available (e.g. when not enough values are present for the filter)
    :return bit 1 set: force sensor is broken, otherwise it is still intact ('unbroken')
    :return forceVector: the force vector (x,y,z)
    :return torqueVector: the torque vector (x,y,z)
    """
    state = ct.c_ubyte()
    forceVector  = (ct.c_float*3)()
    torqueVector = (ct.c_float*3)()
    ret = c_ReadForceSensor(clientID, forceSensorHandle, ct.byref(state), forceVector, torqueVector, operationMode)
    arr1 = []
    for i in range(3):
        arr1.append(forceVector[i])
    arr2 = []
    for i in range(3):
        arr2.append(torqueVector[i])
    #if sys.version_info[0] == 3:
    #    state=state.value
    #else:
    #    state=ord(state.value)
    return ret, state.value, arr1, arr2

def simxBreakForceSensor(clientID, forceSensorHandle, operationMode):
    """
    (regular API equivalent: sim.breakForceSensor)
    Allows breaking a force sensor during simulation. A broken force sensor will lose its positional and orientational constraints. See also simxReadForceSensor.
    number returnCode=simxBreakForceSensor(number clientID,number forceSensorHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param forceSensorHandle: handle of the force sensor
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """
    return c_BreakForceSensor(clientID, forceSensorHandle, operationMode)

def simxReadVisionSensor(clientID, sensorHandle, operationMode):
    """
    (regular API equivalent: sim.readVisionSensor)
    Reads the state of a vision sensor. This function doesn't perform detection, it merely reads the result from a previous call to sim.handleVisionSensor (sim.handleVisionSensor is called in the default main script). See also simxGetVisionSensorImage and simxGetObjectGroupData.
    number returnCode,boolean detectionState,array auxPackets=simxReadVisionSensor(number clientID,number sensorHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param sensorHandle: handle of the vision sensor
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return detectionState: the detection state (i.e. the trigger state).
    :return auxPackets: packets containing auxiliary values returned from the applied filters. By default V-REP returns one packet of 15 auxiliary values:the minimum of {intensity, red, green, blue, depth value}, the maximum of {intensity, red, green, blue, depth value}, and the average of {intensity, red, green, blue, depth value}. If additional filter components return values, then they will be appended as packets after the first packet.
    """

    detectionState = ct.c_ubyte()
    auxValues      = ct.POINTER(ct.c_float)()
    auxValuesCount = ct.POINTER(ct.c_int)()
    ret = c_ReadVisionSensor(clientID, sensorHandle, ct.byref(detectionState), ct.byref(auxValues), ct.byref(auxValuesCount), operationMode)

    auxValues2 = []
    if ret == 0:
        s = 0
        for i in range(auxValuesCount[0]):
            auxValues2.append(auxValues[s:s+auxValuesCount[i+1]])
            s += auxValuesCount[i+1]

        #free C buffers
        c_ReleaseBuffer(auxValues)
        c_ReleaseBuffer(auxValuesCount)

    return ret, bool(detectionState.value!=0), auxValues2

def simxGetObjectHandle(clientID, objectName, operationMode):
    """
    (regular API equivalent: sim.getObjectHandle)
    Retrieves an object handle based on its name. If the client application is launched from a child script, then you could also let the child script figure out what handle correspond to what objects, and send the handles as additional arguments to the client application during its launch. See also simxGetObjectGroupData.
    number returnCode,number handle=simxGetObjectHandle(number clientID,string objectName,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectName: name of the object. If possibe, don't rely on the automatic name adjustment mechanism, and always specify the full object name, including the #: if the object is "myJoint", specify "myJoint#", if the object is "myJoint#0", specify "myJoint#0", etc.
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return handle: the handle
    """
    handle = ct.c_int()
    if (sys.version_info[0] == 3) and (type(objectName) is str):
        objectName=objectName.encode('utf-8')
    return c_GetObjectHandle(clientID, objectName, ct.byref(handle), operationMode), handle.value

def simxGetVisionSensorImage(clientID, sensorHandle, options, operationMode):
    """
    (regular API equivalent: sim.getVisionSensorImage)
    Retrieves the image of a vision sensor. The returned data doesn't make sense if sim.handleVisionSensor wasn't called previously (sim.handleVisionSensor is called by default in the main script if the vision sensor is not tagged as explicit handling). Use the simxGetLastCmdTime function to verify the "freshness" of the retrieved data. See also simxSetVisionSensorImage, simxGetVisionSensorDepthBuffer and simxReadVisionSensor.
    number returnCode,array resolution,array image=simxGetVisionSensorImage(number clientID,number sensorHandle,number options,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param sensorHandle: handle of the vision sensor
    :param options: image options, bit-coded:
    :param bit0 set: each image pixel is a byte (greyscale image), otherwise each image pixel is a rgb byte-triplet
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return resolution: the resolution of the image (x,y)
    :return image: the image data.
    """

    resolution = (ct.c_int*2)()
    c_image  = ct.POINTER(ct.c_byte)()
    bytesPerPixel = 3
    if (options and 1) != 0:
        bytesPerPixel = 1
    ret = c_GetVisionSensorImage(clientID, sensorHandle, resolution, ct.byref(c_image), options, operationMode)

    reso = []
    image = []
    if (ret == 0):
        image = [None]*resolution[0]*resolution[1]*bytesPerPixel
        for i in range(resolution[0] * resolution[1] * bytesPerPixel):
            image[i] = c_image[i]
        for i in range(2):
            reso.append(resolution[i])
    return ret, reso, image

def simxSetVisionSensorImage(clientID, sensorHandle, image, options, operationMode):
    """
    (regular API equivalent: sim.setVisionSensorImage)
    Sets the image of a vision sensor (and applies any image processing filter if specified in the vision sensor dialog). Make sure the vision sensor is flagged as use external image. The "regular" use of this function is to first read the data from a vision sensor with simxGetVisionSensorImage, do some custom filtering, then write the modified image to a passive vision sensor. The alternate use of this function is to display textures, video images, etc. by using a vision sensor object (without however making use of the vision sensor functionality), since a vision sensor can be "looked through" like camera objects.
    number returnCode=simxSetVisionSensorImage(number clientID,number sensorHandle,array image,number options,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param sensorHandle: handle of the vision sensor
    :param image: image data
    :param options: image options, bit-coded:
    :param bit0 set: each image pixel is a byte (greyscale image), otherwise each image pixel is a rgb byte-triplet
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """
    size = len(image)
    image_bytes  = (ct.c_byte*size)(*image)
    return c_SetVisionSensorImage(clientID, sensorHandle, image_bytes, size, options, operationMode)

def simxGetVisionSensorDepthBuffer(clientID, sensorHandle, operationMode):
    """
    (regular API equivalent: sim.getVisionSensorDepthBuffer)
    Retrieves the depth buffer of a vision sensor. The returned data doesn't make sense if sim.handleVisionSensor wasn't called previously (sim.handleVisionSensor is called by default in the main script if the vision sensor is not tagged as explicit handling). Use the simxGetLastCmdTime function to verify the "freshness" of the retrieved data. See also simxGetVisionSensorImage.
    number returnCode,array resolution,array buffer=simxGetVisionSensorDepthBuffer(number clientID,number sensorHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param sensorHandle: handle of the vision sensor
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return resolution: the resolution of the image (x, y)
    :return buffer: the depth buffer data. Values are in the range of 0-1 (0=closest to sensor, 1=farthest from sensor).
    """
    c_buffer  = ct.POINTER(ct.c_float)()
    resolution = (ct.c_int*2)()
    ret = c_GetVisionSensorDepthBuffer(clientID, sensorHandle, resolution, ct.byref(c_buffer), operationMode)
    reso = []
    buffer = []
    if (ret == 0):
        buffer = [None]*resolution[0]*resolution[1]
        for i in range(resolution[0] * resolution[1]):
            buffer[i] = c_buffer[i]
        for i in range(2):
            reso.append(resolution[i])
    return ret, reso, buffer

def simxGetObjectChild(clientID, parentObjectHandle, childIndex, operationMode):
    """
    (regular API equivalent: sim.getObjectChild)
    Retrieves the handle of an object's child object. See also simxGetObjectParent.
    number returnCode,number childObjectHandle=simxGetObjectChild(number clientID,number parentObjectHandle,number childIndex,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param parentObjectHandle: handle of the object
    :param childIndex: zero-based index of the child's position. To retrieve all children of an object, call the function by increasing the index until the child handle is  -1
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return childObjectHandle: the handle of the child object. If the value is -1, there is no child at the given index
    """
    childObjectHandle = ct.c_int()
    return c_GetObjectChild(clientID, parentObjectHandle, childIndex, ct.byref(childObjectHandle), operationMode), childObjectHandle.value

def simxGetObjectParent(clientID, childObjectHandle, operationMode):
    """
    (regular API equivalent: sim.getObjectParent)
    Retrieves the handle of an object's parent object. See also simxGetObjectChild and simxGetObjectGroupData.
    number returnCode,number parentObjectHandle=simxGetObjectParent(number clientID,number objectHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return parentObjectHandle: the handle of the parent object. If the value is -1, the object has no parent
    """

    parentObjectHandle = ct.c_int()
    return c_GetObjectParent(clientID, childObjectHandle, ct.byref(parentObjectHandle), operationMode), parentObjectHandle.value

def simxReadProximitySensor(clientID, sensorHandle, operationMode):
    """
    (regular API equivalent: sim.readProximitySensor)
    Reads the state of a proximity sensor. This function doesn't perform detection, it merely reads the result from a previous call to sim.handleProximitySensor (sim.handleProximitySensor is called in the default main script). See also simxGetObjectGroupData.
    number returnCode,boolean detectionState,array detectedPoint,number detectedObjectHandle,array detectedSurfaceNormalVector=simxReadProximitySensor(number clientID,number sensorHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param sensorHandle: handle of the proximity sensor
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return detectionState: the detection state.
    :return detectedPoint: the detected point coordinates (relative to the sensor reference frame).
    :return detectedObjectHandle:the handle of the detected object.
    :return detectedSurfaceNormalVector: the normal vector (normalized) of the detected surface. Relative to the sensor reference frame.
    """

    detectionState = ct.c_ubyte()
    detectedObjectHandle = ct.c_int()
    detectedPoint  = (ct.c_float*3)()
    detectedSurfaceNormalVector = (ct.c_float*3)()
    ret = c_ReadProximitySensor(clientID, sensorHandle, ct.byref(detectionState), detectedPoint, ct.byref(detectedObjectHandle), detectedSurfaceNormalVector, operationMode)
    arr1 = []
    for i in range(3):
        arr1.append(detectedPoint[i])
    arr2 = []
    for i in range(3):
        arr2.append(detectedSurfaceNormalVector[i])
    return ret, bool(detectionState.value!=0), arr1, detectedObjectHandle.value, arr2

def simxLoadModel(clientID, modelPathAndName, options, operationMode):
    """
    (regular API equivalent: sim.loadModel)
    Loads a previously saved model. See also simxLoadScene and simxTransferFile.
    number returnCode,number baseHandle=simxLoadModel(number clientID,string modelPathAndName,number options,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param modelPathAndName: the model filename, including the path and extension ("ttm"). The file is relative to the client or server system depending on the options value (see next argument)
    :param options: options, bit-coded:
    :param bit0 set: the specified file is located on the client side (in that case the function will be blocking since the model first has to be transferred to the server). Otherwise it is located on the server side
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return baseHandle: the loaded model base.
    """
    baseHandle = ct.c_int()
    if (sys.version_info[0] == 3) and (type(modelPathAndName) is str):
        modelPathAndName=modelPathAndName.encode('utf-8')
    return c_LoadModel(clientID, modelPathAndName, options, ct.byref(baseHandle), operationMode), baseHandle.value

def simxLoadUI(clientID, uiPathAndName, options, operationMode):
    """
    (DEPRECATED)
    DEPRECATED. Use the Qt-based custom user interfaces, via simxCallScriptFunction instead.
    """

    count = ct.c_int()
    uiHandles = ct.POINTER(ct.c_int)()
    if (sys.version_info[0] == 3) and (type(uiPathAndName) is str):
        uiPathAndName=uiPathAndName.encode('utf-8')
    ret = c_LoadUI(clientID, uiPathAndName, options, ct.byref(count), ct.byref(uiHandles), operationMode)

    handles = []
    if ret == 0:
        for i in range(count.value):
            handles.append(uiHandles[i])
        #free C buffers
        c_ReleaseBuffer(uiHandles)

    return ret, handles

def simxLoadScene(clientID, scenePathAndName, options, operationMode):
    """
    (regular API equivalent: sim.loadScene)
    Loads a previously saved scene. Should only be called when simulation is not running and is only executed by continuous remote API server services. See also simxCloseScene, simxLoadModel, and simxTransferFile.
    number returnCode=simxLoadScene(number clientID,string scenePathAndName,number options,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param scenePathAndName: the scene filename, including the path and extension ("ttt"). The file is relative to the client or server system depending on the options value (see next argument)
    :param options: options, bit-coded:
    :param bit0 set: the specified file is located on the client side (in that case the function will be blocking since the scene first has to be transferred to the server). Otherwise it is located on the server side
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    """

    if (sys.version_info[0] == 3) and (type(scenePathAndName) is str):
        scenePathAndName=scenePathAndName.encode('utf-8')
    return c_LoadScene(clientID, scenePathAndName, options, operationMode)

def simxStartSimulation(clientID, operationMode):
    """
    (regular API equivalent: sim.startSimulation)
    Requests a start of a simulation (or a resume of a paused simulation). This function is only executed by continuous remote API server services. See also simxPauseSimulation and simxStopSimulation.
    number returnCode=simxStartSimulation(number clientID,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot.

    :return returnCode: a remote API function return code
    """

    return c_StartSimulation(clientID, operationMode)

def simxPauseSimulation(clientID, operationMode):
    """
    (regular API equivalent: sim.pauseSimulation)
    Requests a pause of a simulation. See also simxStartSimulation and simxStopSimulation.
    number returnCode=simxPauseSimulation(number clientID,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function is simx_opmode_oneshot.

    :return returnCode: a remote API function return code
    """

    return c_PauseSimulation(clientID, operationMode)

def simxStopSimulation(clientID, operationMode):
    """
    (regular API equivalent: sim.stopSimulation)
    Requests a stop of the running simulation. See also simxStartSimulation and simxPauseSimulation.
    number returnCode=simxStopSimulation(number clientID,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function is simx_opmode_oneshot.

    :return returnCode: a remote API function return code
    """

    return c_StopSimulation(clientID, operationMode)

def simxGetUIHandle(clientID, uiName, operationMode):
    """
    (DEPRECATED)
    DEPRECATED. Use the Qt-based custom user interfaces, via simxCallScriptFunction instead.
    """

    handle = ct.c_int()
    if (sys.version_info[0] == 3) and (type(uiName) is str):
        uiName=uiName.encode('utf-8')
    return c_GetUIHandle(clientID, uiName, ct.byref(handle), operationMode), handle.value

def simxGetUISlider(clientID, uiHandle, uiButtonID, operationMode):
    """
    (DEPRECATED)
    DEPRECATED. Use the Qt-based custom user interfaces, via simxCallScriptFunction instead.
    """

    position = ct.c_int()
    return c_GetUISlider(clientID, uiHandle, uiButtonID, ct.byref(position), operationMode), position.value

def simxSetUISlider(clientID, uiHandle, uiButtonID, position, operationMode):
    """
    (DEPRECATED)
    DEPRECATED. Use the Qt-based custom user interfaces, via simxCallScriptFunction instead.
    """

    return c_SetUISlider(clientID, uiHandle, uiButtonID, position, operationMode)

def simxGetUIEventButton(clientID, uiHandle, operationMode):
    """
    (DEPRECATED)
    DEPRECATED. Use the Qt-based custom user interfaces, via simxCallScriptFunction instead.
    """

    uiEventButtonID = ct.c_int()
    auxValues = (ct.c_int*2)()
    ret = c_GetUIEventButton(clientID, uiHandle, ct.byref(uiEventButtonID), auxValues, operationMode)
    arr = []
    for i in range(2):
        arr.append(auxValues[i])
    return ret, uiEventButtonID.value, arr

def simxGetUIButtonProperty(clientID, uiHandle, uiButtonID, operationMode):
    """
    (DEPRECATED)
    DEPRECATED. Use the Qt-based custom user interfaces, via simxCallScriptFunction instead.
    """

    prop = ct.c_int()
    return c_GetUIButtonProperty(clientID, uiHandle, uiButtonID, ct.byref(prop), operationMode), prop.value

def simxSetUIButtonProperty(clientID, uiHandle, uiButtonID, prop, operationMode):
    """
    (DEPRECATED)
    DEPRECATED. Use the Qt-based custom user interfaces, via simxCallScriptFunction instead.
    """

    return c_SetUIButtonProperty(clientID, uiHandle, uiButtonID, prop, operationMode)

def simxAddStatusbarMessage(clientID, message, operationMode):
    """
    (regular API equivalent: sim.addStatusbarMessage)
    Adds a message to the status bar.
    number returnCode=simxAddStatusbarMessage(number clientID,string message,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param message: the message to display
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    if (sys.version_info[0] == 3) and (type(message) is str):
        message=message.encode('utf-8')
    return c_AddStatusbarMessage(clientID, message, operationMode)

def simxAuxiliaryConsoleOpen(clientID, title, maxLines, mode, position, size, textColor, backgroundColor, operationMode):
    """
    (regular API equivalent: sim.auxiliaryConsoleOpen)
    Opens an auxiliary console window for text display. This console window is different from the application main console window. Console window handles are shared across all simulator scenes. See also simxAuxiliaryConsolePrint, simxAuxiliaryConsoleShow and simxAuxiliaryConsoleClose.
    number returnCode,number consoleHandle=simxAuxiliaryConsoleOpen(number clientID,string title,number maxLines,number mode,array position,array size,array textColor,array backgroundColor,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param title: the title of the console window
    :param maxLines: the number of text lines that can be displayed and buffered
    :param mode: bit-coded value. Bit0 set indicates that the console window will   automatically close at simulation end, bit1 set   indicates that lines will be wrapped, bit2 set indicates that the user   can close the console window, bit3 set indicates that the console will   automatically be hidden during simulation pause, bit4 set indicates that   the console will not automatically hide when the user switches to   another scene.
    :param position: the initial position of the console window (x and y value). Can be None for default values.
    :param size: the initial size of the console window (x and y value). Can be None for default values.
    :param textColor: the color of the text (rgb values, 0-1). Can be None for default values.
    :param backgroundColor: the background color of the console window (rgb values, 0-1). Can be None for default values.
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return consoleHandle: the handle of the created console
    """

    consoleHandle = ct.c_int()
    if (sys.version_info[0] == 3) and (type(title) is str):
        title=title.encode('utf-8')
    if position != None:
        c_position = (ct.c_int*2)(*position)
    else:
        c_position = None
    if size != None:
        c_size = (ct.c_int*2)(*size)
    else:
        c_size = None
    if textColor != None:
        c_textColor = (ct.c_float*3)(*textColor)
    else:
        c_textColor = None
    if backgroundColor != None:
        c_backgroundColor = (ct.c_float*3)(*backgroundColor)
    else:
        c_backgroundColor = None
    return c_AuxiliaryConsoleOpen(clientID, title, maxLines, mode, c_position, c_size, c_textColor, c_backgroundColor, ct.byref(consoleHandle), operationMode), consoleHandle.value

def simxAuxiliaryConsoleClose(clientID, consoleHandle, operationMode):
    """
    (regular API equivalent: sim.auxiliaryConsoleClose)
    Closes an auxiliary console window. See also simxAuxiliaryConsoleOpen.
    number returnCode=simxAuxiliaryConsoleClose(number clientID,number consoleHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param consoleHandle: the handle of the console window, previously returned by the simxAuxiliaryConsoleOpen command
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    return c_AuxiliaryConsoleClose(clientID, consoleHandle, operationMode)

def simxAuxiliaryConsolePrint(clientID, consoleHandle, txt, operationMode):
    """
    (regular API equivalent: sim.auxiliaryConsolePrint)
    Prints to an auxiliary console window. See also simxAuxiliaryConsoleOpen.
    number returnCode=simxAuxiliaryConsolePrint(number clientID,number consoleHandle,string txt,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param consoleHandle: the handle of the console window, previously returned by the simxAuxiliaryConsoleOpen command
    :param txt: the text to append, or "None" to clear the console window
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    """

    if (sys.version_info[0] == 3) and (type(txt) is str):
        txt=txt.encode('utf-8')
    return c_AuxiliaryConsolePrint(clientID, consoleHandle, txt, operationMode)

def simxAuxiliaryConsoleShow(clientID, consoleHandle, showState, operationMode):
    """
    (regular API equivalent: sim.auxiliaryConsoleShow)
    Shows or hides an auxiliary console window. See also simxAuxiliaryConsoleOpen and simxAuxiliaryConsoleClose.
    number returnCode=simxAuxiliaryConsoleShow(number clientID,number consoleHandle,number showState,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param consoleHandle: the handle of the console window, previously returned by the simxAuxiliaryConsoleOpen command
    :param showState: indicates whether the console should be hidden (0) or shown (!=0)
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    """

    return c_AuxiliaryConsoleShow(clientID, consoleHandle, showState, operationMode)

def simxGetObjectOrientation(clientID, objectHandle, relativeToObjectHandle, operationMode):
    """
    (regular API equivalent: sim.getObjectOrientation)
    Retrieves the orientation (Euler angles) of an object. See also simxSetObjectOrientation, simxGetObjectQuaternion, simxGetObjectPosition and simxGetObjectGroupData.
    number returnCode,array eulerAngles=simxGetObjectOrientation(number clientID,number objectHandle,number relativeToObjectHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param relativeToObjectHandle: indicates relative to which reference frame we want the orientation.   Specify -1 to retrieve the absolute orientation, sim_handle_parent to   retrieve the orientation relative to the object's parent, or an object   handle relative to whose reference frame you want the orientation
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return eulerAngles: the Euler angles (alpha, beta and gamma)
    """
    eulerAngles = (ct.c_float*3)()
    ret = c_GetObjectOrientation(clientID, objectHandle, relativeToObjectHandle, eulerAngles, operationMode)
    arr = []
    for i in range(3):
        arr.append(eulerAngles[i])
    return ret, arr

def simxGetObjectQuaternion(clientID, objectHandle, relativeToObjectHandle, operationMode):
    """
    (regular API equivalent: sim.getObjectQuaternion)
    Retrieves the quaternion  of an object. See also simxSetObjectQuaternion.
    number returnCode,array quat=simxGetObjectQuaternion(number clientID,number objectHandle,number relativeToObjectHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param relativeToObjectHandle: indicates relative to which reference frame we want the quaternion.   Specify -1 to retrieve the absolute quaternion, sim_handle_parent to   retrieve the quaternion relative to the object's parent, or an object   handle relative to whose reference frame you want the quaternion
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return quat: the quaternion (x, y, z, w)
    """
    quaternion = (ct.c_float*4)()
    ret = c_GetObjectQuaternion(clientID, objectHandle, relativeToObjectHandle, quaternion, operationMode)
    arr = []
    for i in range(4):
        arr.append(quaternion[i])
    return ret, arr

def simxGetObjectPosition(clientID, objectHandle, relativeToObjectHandle, operationMode):
    """
    (regular API equivalent: sim.getObjectPosition)
    Retrieves the position  of an object. See also simxSetObjectPosition,  simxGetObjectOrientation, simxGetObjectQuaternion and simxGetObjectGroupData.
    number returnCode,array position=simxGetObjectPosition(number clientID,number objectHandle,number relativeToObjectHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param relativeToObjectHandle: indicates relative to which reference frame we want the position.   Specify -1 to retrieve the absolute position, sim_handle_parent to   retrieve the position relative to the object's parent, or an object   handle relative to whose reference frame you want the position
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return position: the position (x,y,z)
    """
    position = (ct.c_float*3)()
    ret = c_GetObjectPosition(clientID, objectHandle, relativeToObjectHandle, position, operationMode)
    arr = []
    for i in range(3):
        arr.append(position[i])
    return ret, arr

def simxSetObjectOrientation(clientID, objectHandle, relativeToObjectHandle, eulerAngles, operationMode):
    """
    (regular API equivalent: sim.setObjectOrientation)
    Sets the orientation (Euler angles) of an object. Dynamically simulated objects will implicitely be reset before the command is applied (i.e. similar to calling sim.resetDynamicObject just before). See also simxGetObjectOrientation, simxSetObjectQuaternion and simxSetObjectPosition.
    number returnCode=simxSetObjectOrientation(number clientID,number objectHandle,number relativeToObjectHandle,array eulerAngles,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param relativeToObjectHandle: indicates relative to which reference frame the orientation is specified. Specify -1 to set the absolute orientation, sim_handle_parent to set the orientation relative to the object's parent, or an object handle relative to whose reference frame the orientation is specified.
    :param eulerAngles: Euler angles (alpha, beta and gamma)
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    angles = (ct.c_float*3)(*eulerAngles)
    return c_SetObjectOrientation(clientID, objectHandle, relativeToObjectHandle, angles, operationMode)

def simxSetObjectQuaternion(clientID, objectHandle, relativeToObjectHandle, quaternion, operationMode):
    """
    (regular API equivalent: sim.setObjectQuaternion)
    Sets the orientation of an object as quaternion. Dynamically simulated objects will implicitely be reset before the command is applied (i.e. similar to calling  sim.resetDynamicObject just before). See also simxGetObjectQuaternion.
    number returnCode=simxSetObjectQuaternion(number clientID,number objectHandle,number relativeToObjectHandle,array quat,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param relativeToObjectHandle: indicates relative to which reference frame the quaternion is specified. Specify -1 to set the absolute quaternion, sim_handle_parent to set the quaternion relative to the object's parent, or an object handle relative to whose reference frame the quaternion is specified.
    :param quat: the quaternion values (x, y, z, w)
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    quat = (ct.c_float*4)(*quaternion)
    return c_SetObjectQuaternion(clientID, objectHandle, relativeToObjectHandle, quat, operationMode)

def simxSetObjectPosition(clientID, objectHandle, relativeToObjectHandle, position, operationMode):
    """
    (regular API equivalent: sim.setObjectPosition)
    Sets the position of an object. Dynamically simulated objects will implicitely be reset before the command is applied (i.e. similar to calling  sim.resetDynamicObject just before). See also simxGetObjectPosition, simxSetObjectQuaternion and simxSetObjectOrientation.
    number returnCode=simxSetObjectPosition(number clientID,number objectHandle,number relativeToObjectHandle,array position,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param relativeToObjectHandle: indicates relative to which reference frame the position is specified. Specify -1 to set the absolute position, sim_handle_parent to set the position relative to the object's parent, or an object handle relative to whose reference frame the position is specified.
    :param position: the position values (x, y and z)
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    c_position = (ct.c_float*3)(*position)
    return c_SetObjectPosition(clientID, objectHandle, relativeToObjectHandle, c_position, operationMode)

def simxSetObjectParent(clientID, objectHandle, parentObject, keepInPlace, operationMode):
    """
    (regular API equivalent: sim.setObjectParent)
    Sets an object's parent object. See also simxGetObjectParent.
    number returnCode=simxSetObjectParent(number clientID,number objectHandle,number parentObject,boolean keepInPlace,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object that will become child of the parent object.  Can be combined with sim_handleflag_assembly, if the two objects can be assembled via a predefined assembly transformation (refer to the assembling option in the object common properties). In that case, parentObject can't be -1, and keepInPlace should be set to false.
    :param parentObject: handle of the object that will become parent, or -1 if the object should become parentless
    :param keepInPlace: indicates whether the object's absolute position and orientation should stay same
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot or simx_opmode_blocking depending on the intent

    :return returnCode: a remote API function return code
    """

    return c_SetObjectParent(clientID, objectHandle, parentObject, keepInPlace, operationMode)

def simxSetUIButtonLabel(clientID, uiHandle, uiButtonID, upStateLabel, downStateLabel, operationMode):
    """
    (DEPRECATED)
    DEPRECATED. Use the Qt-based custom user interfaces, via simxCallScriptFunction instead.
    """

    if sys.version_info[0] == 3:
        if type(upStateLabel) is str:
            upStateLabel=upStateLabel.encode('utf-8')
        if type(downStateLabel) is str:
            downStateLabel=downStateLabel.encode('utf-8')
    return c_SetUIButtonLabel(clientID, uiHandle, uiButtonID, upStateLabel, downStateLabel, operationMode)

def simxGetLastErrors(clientID, operationMode):
    """
    (regular API equivalent: sim.getLastError)
    Retrieves the last 50 errors that occured on the server side, and clears the error buffer there. Only errors that occured because of this client will be reported.
    number returnCode,array errorStrings=simxGetLastErrors(number clientID,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls) when not debugging. For debugging purposes, use simx_opmode_blocking.

    :return returnCode: a remote API function return code
    :return errorStrings: the error strings
    """
    errors =[]
    errorCnt = ct.c_int()
    errorStrings = ct.POINTER(ct.c_char)()
    ret = c_GetLastErrors(clientID, ct.byref(errorCnt), ct.byref(errorStrings), operationMode)
    if ret == 0:
        s = 0
        for i in range(errorCnt.value):
            a = bytearray()
            while errorStrings[s] != b'\0':
                if sys.version_info[0] == 3:
                    a.append(int.from_bytes(errorStrings[s],'big'))
                else:
                    a.append(errorStrings[s])
                s += 1
            s += 1 #skip null
            if sys.version_info[0] == 3:
                errors.append(str(a,'utf-8'))
            else:
                errors.append(str(a))

    return ret, errors

def simxGetArrayParameter(clientID, paramIdentifier, operationMode):
    """
    (regular API equivalent: sim.getArrayParameter)
    Retrieves 3 values from an array. See the array parameter identifiers. See also simxSetArrayParameter, simxGetBooleanParameter, simxGetIntegerParameter, simxGetFloatingParameter and simxGetStringParameter.
    number returnCode,array paramValues=simxGetArrayParameter(number clientID,number paramIdentifier,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param paramIdentifier: an array parameter identifier
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking (if not called on a regular basis)

    :return returnCode: a remote API function return code
    :return paramValues: an array containing 3 values
    """
    paramValues = (ct.c_float*3)()
    ret = c_GetArrayParameter(clientID, paramIdentifier, paramValues, operationMode)
    arr = []
    for i in range(3):
        arr.append(paramValues[i])
    return ret, arr

def simxSetArrayParameter(clientID, paramIdentifier, paramValues, operationMode):
    """
    (regular API equivalent: sim.setArrayParameter)
    Sets 3 values of an array parameter. See also simxGetArrayParameter, simxSetBooleanParameter, simxSetIntegerParameter and simxSetFloatingParameter.
    number returnCode=simxSetArrayParameter(number clientID,number paramIdentifier,array paramValues,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param paramIdentifier: an array parameter identifier
    :param paramValues: the array containing the 3 values to set
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    c_paramValues = (ct.c_float*3)(*paramValues)
    return c_SetArrayParameter(clientID, paramIdentifier, c_paramValues, operationMode)

def simxGetBooleanParameter(clientID, paramIdentifier, operationMode):
    """
    (regular API equivalent: sim.getBoolParameter)
    Retrieves a boolean value. See the Boolean parameter identifiers. See also simxSetBooleanParameter, simxGetIntegerParameter, simxGetFloatingParameter, simxGetArrayParameter and simxGetStringParameter.
    number returnCode,boolean paramValue=simxGetBooleanParameter(number clientID,number paramIdentifier,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param paramIdentifier: a Boolean parameter identifier
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking (if not called on a regular basis)

    :return returnCode: a remote API function return code
    :return paramValue: the boolean value
    """

    paramValue = ct.c_ubyte()
    return c_GetBooleanParameter(clientID, paramIdentifier, ct.byref(paramValue), operationMode), bool(paramValue.value!=0)

def simxSetBooleanParameter(clientID, paramIdentifier, paramValue, operationMode):
    """
    (regular API equivalent: sim.setBoolParameter)
    Sets a boolean parameter. See also simxGetBooleanParameter, simxSetIntegerParameter, simxSetArrayParameter and simxSetFloatingParameter.
    number returnCode=simxSetBooleanParameter(number clientID,number paramIdentifier,boolean paramValue,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param paramIdentifier: a Boolean parameter identifier
    :param paramValue: the parameter value
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    return c_SetBooleanParameter(clientID, paramIdentifier, paramValue, operationMode)

def simxGetIntegerParameter(clientID, paramIdentifier, operationMode):
    """
    (regular API equivalent: sim.getInt32Parameter)
    Retrieves an integer value. See the integer parameter identifiers. See also simxSetIntegerParameter, simxGetBooleanParameter, simxGetFloatingParameter, simxGetArrayParameter and simxGetStringParameter.
    number returnCode,number paramValue=simxGetIntegerParameter(number clientID,number paramIdentifier,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param paramIdentifier: an integer parameter identifier
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking (if not called on a regular basis)

    :return returnCode: a remote API function return code
    :return paramValue: the parameter value
    """

    paramValue = ct.c_int()
    return c_GetIntegerParameter(clientID, paramIdentifier, ct.byref(paramValue), operationMode), paramValue.value

def simxSetIntegerParameter(clientID, paramIdentifier, paramValue, operationMode):
    """
    (regular API equivalent: sim.setInt32Parameter)
    Sets an integer parameter. See also simxGetIntegerParameter, simxSetBooleanParameter, simxSetArrayParameter and simxSetFloatingParameter.
    number returnCode=simxSetIntegerParameter(number clientID,number paramIdentifier,number paramValue,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param paramIdentifier: an integer parameter identifier
    :param paramValue: the parameter value
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    return c_SetIntegerParameter(clientID, paramIdentifier, paramValue, operationMode)

def simxGetFloatingParameter(clientID, paramIdentifier, operationMode):
    """
    (regular API equivalent: sim.getFloatParameter)
    Retrieves a floating point value. See the floating-point parameter identifiers. See also simxSetFloatingParameter, simxGetBooleanParameter, simxGetIntegerParameter, simxGetArrayParameter and simxGetStringParameter.
    number returnCode,number paramValue=simxGetFloatingParameter(number clientID,number paramIdentifier,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param paramIdentifier: a floating parameter identifier
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking (if not called on a regular basis)

    :return returnCode: a remote API function return code
    :return paramValue: a pointer that will receive the parameter value
    """

    paramValue = ct.c_float()
    return c_GetFloatingParameter(clientID, paramIdentifier, ct.byref(paramValue), operationMode), paramValue.value

def simxSetFloatingParameter(clientID, paramIdentifier, paramValue, operationMode):
    """
    (regular API equivalent: sim.setFloatParameter)
    Sets a floating point parameter. See also simxGetFloatingParameter, simxSetBooleanParameter, simxSetArrayParameter and simxSetIntegerParameter.
    number returnCode=simxSetFloatingParameter(number clientID,number paramIdentifier,number paramValue,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param paramIdentifier: a floating parameter identifier
    :param paramValue: the parameter value
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    return c_SetFloatingParameter(clientID, paramIdentifier, paramValue, operationMode)

def simxGetStringParameter(clientID, paramIdentifier, operationMode):
    """
    (regular API equivalent: sim.getStringParameter)
    Retrieves a string value. See the string parameter identifiers. See also simxGetBooleanParameter, simxGetIntegerParameter, simxGetArrayParameter and simxGetFloatingParameter.
    number returnCode,string paramValue=simxGetStringParameter(number clientID,number paramIdentifier,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param paramIdentifier: a string parameter identifier
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking (if not called on a regular basis)

    :return returnCode: a remote API function return code
    :return paramValue: the string.
    """
    paramValue = ct.POINTER(ct.c_char)()
    ret = c_GetStringParameter(clientID, paramIdentifier, ct.byref(paramValue), operationMode)

    a = bytearray()
    if ret == 0:
        i = 0
        while paramValue[i] != b'\0':
            if sys.version_info[0] == 3:
                a.append(int.from_bytes(paramValue[i],'big'))
            else:
                a.append(paramValue[i])
            i=i+1
    if sys.version_info[0] == 3:
        a=str(a,'utf-8')
    else:
        a=str(a)
    return ret, a

def simxGetCollisionHandle(clientID, collisionObjectName, operationMode):
    """
    (regular API equivalent: sim.getCollisionHandle)
    Retrieves a collision  object handle based on its name. If the client application is launched from a child script, then you could also let the child script figure out what handle correspond to what collision object, and send the handles as additional arguments to the client application during its launch. See also simxGetObjectGroupData.
    number returnCode,number handle=simxGetCollisionHandle(number clientID,string collisionObjectName,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param collisionObjectName: name of the collision object. If possibe, don't rely on the automatic name adjustment mechanism, and always specify the full collision object name, including the #: if the collision object is "myCollision", specify "myCollision#", if the collision object is "myCollision#0", specify "myCollision#0", etc.
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return handle: the collision handle
    """

    handle = ct.c_int()
    if (sys.version_info[0] == 3) and (type(collisionObjectName) is str):
        collisionObjectName=collisionObjectName.encode('utf-8')
    return c_GetCollisionHandle(clientID, collisionObjectName, ct.byref(handle), operationMode), handle.value

def simxGetCollectionHandle(clientID, collectionName, operationMode):
    """
    (regular API equivalent: sim.getCollectionHandle)
    Retrieves a collection handle based on its name. If the client application is launched from a child script, then you could also let the child script figure out what handle correspond to what collection, and send the handles as additional arguments to the client application during its launch. See also simxGetObjectGroupData.
    number returnCode,number handle=simxGetCollectionHandle(number clientID,string collectionName,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param collectionName: name of the collection. If possibe, don't rely on the automatic name adjustment mechanism, and always specify the full collection name, including the #: if the collection is "myCollection", specify "myCollection#", if the collection is "myCollection#0", specify "myCollection#0", etc.
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return handle: the collision handle
    """

    handle = ct.c_int()
    if (sys.version_info[0] == 3) and (type(collectionName) is str):
        collectionName=collectionName.encode('utf-8')
    return c_GetCollectionHandle(clientID, collectionName, ct.byref(handle), operationMode), handle.value

def simxGetDistanceHandle(clientID, distanceObjectName, operationMode):
    """
    (regular API equivalent: sim.getDistanceHandle)
    Retrieves a distance  object handle based on its name. If the client application is launched from a child script, then you could also let the child script figure out what handle correspond to what distance object, and send the handles as additional arguments to the client application during its launch. See also simxGetObjectGroupData.
    number returnCode,number handle=simxGetDistanceHandle(number clientID,string distanceObjectName,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param distanceObjectName: name of the distance object. If possibe, don't rely on the automatic name adjustment mechanism, and always specify the full distance object name, including the #: if the distance object is "myDistance", specify "myDistance#", if the distance object is "myDistance#0", specify "myDistance#0", etc.
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return handle: handle of the distance object
    """

    handle = ct.c_int()
    if (sys.version_info[0] == 3) and (type(distanceObjectName) is str):
        distanceObjectName=distanceObjectName.encode('utf-8')
    return c_GetDistanceHandle(clientID, distanceObjectName, ct.byref(handle), operationMode), handle.value

def simxReadCollision(clientID, collisionObjectHandle, operationMode):
    """
    (regular API equivalent: sim.readCollision)
    Reads the collision state of a registered collision object. This function doesn't perform collision detection, it merely reads the result from a previous call to sim.handleCollision (sim.handleCollision is called in the default main script). See also simxGetObjectGroupData.
    number returnCode,boolean collisionState=simxReadCollision(number clientID,number collisionObjectHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param collisionObjectHandle: handle of the collision object
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return collisionState: the collision state
    """
    collisionState = ct.c_ubyte()
    return c_ReadCollision(clientID, collisionObjectHandle, ct.byref(collisionState), operationMode), bool(collisionState.value!=0)

def simxReadDistance(clientID, distanceObjectHandle, operationMode):
    """
    (regular API equivalent: sim.readDistance)
    Reads the distance that a  registered distance object measured. This function doesn't perform minimum distance calculation, it merely reads the result from a previous call to sim.handleDistance (sim.handleDistance is called in the default main script). See also simxGetObjectGroupData.
    number returnCode,number minimumDistance=simxReadDistance(number clientID,number distanceObjectHandle, number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param distanceObjectHandle: handle of the distance object
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return minimumDistance: the minimum distance.  If the distance object wasn't handled yet, the distance value will be larger than 1e36.
    """

    minimumDistance = ct.c_float()
    return c_ReadDistance(clientID, distanceObjectHandle, ct.byref(minimumDistance), operationMode), minimumDistance.value

def simxRemoveObject(clientID, objectHandle, operationMode):
    """
    (regular API equivalent: sim.removeObject)
    Removes a scene object. See also simxRemoveModel.
    number returnCode=simxRemoveObject(number clientID,number objectHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object to remove
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot (or simx_opmode_blocking)

    :return returnCode: a remote API function return code
    """

    return c_RemoveObject(clientID, objectHandle, operationMode)

def simxRemoveModel(clientID, objectHandle, operationMode):
    """
    (regular API equivalent: sim.removeModel)
    Removes a model from the scene. See also simxRemoveObject.
    number returnCode=simxRemoveModel(number clientID,number objectHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the model to remove (object should be flagged as model base).
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot (or simx_opmode_blocking)

    :return returnCode: a remote API function return code
    """

    return c_RemoveModel(clientID, objectHandle, operationMode)

def simxRemoveUI(clientID, uiHandle, operationMode):
    """
    (DEPRECATED)
    DEPRECATED. Use the Qt-based custom user interfaces, via simxCallScriptFunction instead.
    """

    return c_RemoveUI(clientID, uiHandle, operationMode)

def simxCloseScene(clientID, operationMode):
    """
    (regular API equivalent: simCloseScene)
    Closes current scene, and switches to another open scene. If there is no other open scene, a new scene is then created. Should only be called when simulation is not running and is only executed by continuous remote API server services. See also simxLoadScene.
    number returnCode=simxCloseScene(number clientID,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    """

    return c_CloseScene(clientID, operationMode)

def simxGetObjects(clientID, objectType, operationMode):
    """
    (regular API equivalent: sim.getObjects)
    Retrieves object handles of a given type, or of all types (i.e. all object handles). See also simxGetObjectGroupData.
    number returnCode,array objectHandles=simxGetObjects(number clientID,number objectType,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectType: object type (sim_object_shape_type, sim_object_joint_type, etc., or sim_handle_all for any type of object
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return objectHandles: an object handle array.
    """

    objectCount = ct.c_int()
    objectHandles = ct.POINTER(ct.c_int)()

    ret = c_GetObjects(clientID, objectType, ct.byref(objectCount), ct.byref(objectHandles), operationMode)
    handles = []
    if ret == 0:
        for i in range(objectCount.value):
            handles.append(objectHandles[i])

    return ret, handles


def simxDisplayDialog(clientID, titleText, mainText, dialogType, initialText, titleColors, dialogColors, operationMode):
    """
    (regular API equivalent: sim.displayDialog)
    Displays a generic dialog box during simulation (and only during simulation!). Use in conjunction with simxGetDialogResult, simxGetDialogInput and simxEndDialog. Use custom user interfaces instead if a higher customization level is required.
    number returnCode,number dialogHandle,number uiHandle=simxDisplayDialog(number clientID,string titleText,string mainText,number dialogType,string initialText,array titleColors,array dialogColors,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param titleText: Title bar text
    :param mainText: Information text
    :param dialogType: a generic dialog style
    :param initialText: Initial text in the edit box if the dialog is of type sim_dlgstyle_input. Cannot be None.
    :param titleColors: Title bar color (6 values for RGB for background and foreground). Can be None for default values.
    :param dialogColors: Dialog color (6 values for RGB for background and foreground). Can be None for default Values.
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return dialogHandle: handle of the generic dialog (different from OpenGl-based custom UI handle!! (see hereafter)). This handle should be used with the following functions: simxGetDialogResult, simxGetDialogInput and simxEndDialog.
    :return uiHandle: the handle of the corresponding OpenGl-based custom UI
    """
    if titleColors != None:
        c_titleColors  = (ct.c_float*6)(*titleColors)
    else:
        c_titleColors  = None
    if dialogColors != None:
        c_dialogColors  = (ct.c_float*6)(*dialogColors)
    else:
        c_dialogColors  = None

    c_dialogHandle = ct.c_int()
    c_uiHandle = ct.c_int()
    if sys.version_info[0] == 3:
        if type(titleText) is str:
            titleText=titleText.encode('utf-8')
        if type(mainText) is str:
            mainText=mainText.encode('utf-8')
        if type(initialText) is str:
            initialText=initialText.encode('utf-8')
    return c_DisplayDialog(clientID, titleText, mainText, dialogType, initialText, c_titleColors, c_dialogColors, ct.byref(c_dialogHandle), ct.byref(c_uiHandle), operationMode), c_dialogHandle.value, c_uiHandle.value

def simxEndDialog(clientID, dialogHandle, operationMode):
    """
    (regular API equivalent: sim.endDialog)
    Closes and releases resource from a previous call to simxDisplayDialog. Even if the dialog is not visible anymore, you should release resources by using this function (however at the end of a simulation, all dialog resources are automatically released).
    number returnCode=simxEndDialog(number clientID,number dialogHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param dialogHandle: handle of generic dialog (return value of simxDisplayDialog)
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    return c_EndDialog(clientID, dialogHandle, operationMode)

def simxGetDialogInput(clientID, dialogHandle, operationMode):
    """
    (regular API equivalent: sim.getDialogInput)
    Queries the text the user entered into a  generic dialog box of style sim_dlgstyle_input. To be used after simxDisplayDialog was called and after simxGetDialogResult returned sim_dlgret_ok.
    number returnCode,string inputText=simxGetDialogInput(number clientID,number dialogHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param dialogHandle: handle of generic dialog (return value of simxDisplayDialog)
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return inputText: the string the user entered.
    """
    inputText = ct.POINTER(ct.c_char)()
    ret = c_GetDialogInput(clientID, dialogHandle, ct.byref(inputText), operationMode)

    a = bytearray()
    if ret == 0:
        i = 0
        while inputText[i] != b'\0':
            if sys.version_info[0] == 3:
                a.append(int.from_bytes(inputText[i],'big'))
            else:
                a.append(inputText[i])
            i = i+1

    if sys.version_info[0] == 3:
        a=str(a,'utf-8')
    else:
        a=str(a)
    return ret, a


def simxGetDialogResult(clientID, dialogHandle, operationMode):
    """
    (regular API equivalent: sim.getDialogResult)
    Queries the result of a dialog box. To be used after simxDisplayDialog was called.
    number returnCode,number result=simxGetDialogResult(number clientID,number dialogHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param dialogHandle: handle of generic dialog (return value of simxDisplayDialog)
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    :return result: the result value.
    :return
    :return Note. If the result is sim_dlgret_still_open, the dialog was not closed and no button was pressed. Otherwise, you should free resources with simxEndDialog (the dialog might not be visible anymore, but is still present)
    """
    result = ct.c_int()
    return c_GetDialogResult(clientID, dialogHandle, ct.byref(result), operationMode), result.value

def simxCopyPasteObjects(clientID, objectHandles, operationMode):
    """
    (regular API equivalent: sim.copyPasteObjects)
    Copies and pastes objects, together with all their associated calculation objects and child scripts. To copy and paste whole models, you can simply copy and paste the model base object.
    number returnCode,array newObjectHandles=simxCopyPasteObjects(number clientID,array objectHandles,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandles: an array containing the handles of the objects to copy
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return newObjectHandles: an array containing the handles of newly created objects. Individual objects of a new model are not returned, but only the model base.
    """
    c_objectHandles  = (ct.c_int*len(objectHandles))(*objectHandles)
    c_objectHandles = ct.cast(c_objectHandles,ct.POINTER(ct.c_int)) # IronPython needs this
    newObjectCount   = ct.c_int()
    newObjectHandles = ct.POINTER(ct.c_int)()
    ret = c_CopyPasteObjects(clientID, c_objectHandles, len(objectHandles), ct.byref(newObjectHandles), ct.byref(newObjectCount), operationMode)

    newobj = []
    if ret == 0:
        for i in range(newObjectCount.value):
            newobj.append(newObjectHandles[i])

    return ret, newobj


def simxGetObjectSelection(clientID, operationMode):
    """
    (regular API equivalent: sim.getObjectSelection)
    Retrieves all selected object's handles. See also simxSetObjectSelection.
    number returnCode,array objectHandles=simxGetObjectSelection(number clientID,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls), or simx_opmode_blocking depending on the intent.

    :return returnCode: a remote API function return code
    :return objectHandles: an object handle array.
    """
    objectCount   = ct.c_int()
    objectHandles = ct.POINTER(ct.c_int)()
    ret = c_GetObjectSelection(clientID, ct.byref(objectHandles), ct.byref(objectCount), operationMode)

    newobj = []
    if ret == 0:
        for i in range(objectCount.value):
            newobj.append(objectHandles[i])

    return ret, newobj



def simxSetObjectSelection(clientID, objectHandles, operationMode):
    """
    Sets the selection state for objects. See also simxGetObjectSelection.
    number returnCode=simxSetObjectSelection(number clientID,array objectHandles,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandles: an array of object handles
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot or simx_opmode_blocking depending on the intent.

    :return returnCode: a remote API function return code
    """

    c_objectHandles  = (ct.c_int*len(objectHandles))(*objectHandles)
    return c_SetObjectSelection(clientID, c_objectHandles, len(objectHandles), operationMode)

def simxClearFloatSignal(clientID, signalName, operationMode):
    """
    (regular API equivalent: sim.clearFloatSignal)
    Clears a float signal (removes it). See also simxSetFloatSignal, simxClearIntegerSignal and simxClearStringSignal.
    number returnCode=simxClearFloatSignal(number clientID,string signalName,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal or an empty string to clear all float signals
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    if (sys.version_info[0] == 3) and (type(signalName) is str):
        signalName=signalName.encode('utf-8')
    return c_ClearFloatSignal(clientID, signalName, operationMode)

def simxClearIntegerSignal(clientID, signalName, operationMode):
    """
    (regular API equivalent: sim.clearIntegerSignal)
    Clears an integer signal (removes it). See also simxSetIntegerSignal, simxClearFloatSignal and simxClearStringSignal.
    number returnCode=simxClearIntegerSignal(number clientID,string signalName,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal or an empty string to clear all integer signals
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    if (sys.version_info[0] == 3) and (type(signalName) is str):
        signalName=signalName.encode('utf-8')
    return c_ClearIntegerSignal(clientID, signalName, operationMode)

def simxClearStringSignal(clientID, signalName, operationMode):
    """
    (regular API equivalent: sim.clearStringSignal)
    Clears a string signal (removes it). See also simxSetStringSignal, simxClearIntegerSignal and simxClearFloatSignal.
    number returnCode=simxClearStringSignal(number clientID,string signalName,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal or an empty string to clear all string signals
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    if (sys.version_info[0] == 3) and (type(signalName) is str):
        signalName=signalName.encode('utf-8')
    return c_ClearStringSignal(clientID, signalName, operationMode)

def simxGetFloatSignal(clientID, signalName, operationMode):
    """
    (regular API equivalent: sim.getFloatSignal)
    Gets the value of a float signal. Signals are cleared at simulation start. See also simxSetFloatSignal, simxClearFloatSignal, simxGetIntegerSignal and simxGetStringSignal.
    number returnCode,number signalValue=simxGetFloatSignal(number clientID,string signalName,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return signalValue: the value of the signal
    """

    signalValue = ct.c_float()
    if (sys.version_info[0] == 3) and (type(signalName) is str):
        signalName=signalName.encode('utf-8')
    return c_GetFloatSignal(clientID, signalName, ct.byref(signalValue), operationMode), signalValue.value

def simxGetIntegerSignal(clientID, signalName, operationMode):
    """
    (regular API equivalent: sim.getIntegerSignal)
    Gets the value of an integer signal. Signals are cleared at simulation start. See also simxSetIntegerSignal, simxClearIntegerSignal, simxGetFloatSignal and simxGetStringSignal.
    number returnCode,number signalValue=simxGetIntegerSignal(number clientID,string signalName,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return signalValue: the value of the signal
    """

    signalValue = ct.c_int()
    if (sys.version_info[0] == 3) and (type(signalName) is str):
        signalName=signalName.encode('utf-8')
    return c_GetIntegerSignal(clientID, signalName, ct.byref(signalValue), operationMode), signalValue.value

def simxGetStringSignal(clientID, signalName, operationMode):
    """
    (regular API equivalent: sim.getStringSignal)
    Gets the value of a string signal. Signals are cleared at simulation start. To pack/unpack integers/floats into/from a string, refer to simxPackInts, simxPackFloats, simxUnpackInts and simxUnpackFloats. See also simxSetStringSignal, simxReadStringStream, simxClearStringSignal, simxGetIntegerSignal and simxGetFloatSignal.
    number returnCode,string signalValue=simxGetStringSignal(number clientID,string signalName,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return signalValue: the value of the signal.
    """

    signalLength = ct.c_int();
    signalValue = ct.POINTER(ct.c_ubyte)()
    if (sys.version_info[0] == 3) and (type(signalName) is str):
        signalName=signalName.encode('utf-8')
    ret = c_GetStringSignal(clientID, signalName, ct.byref(signalValue), ct.byref(signalLength), operationMode)

    a = bytearray()
    if ret == 0:
        for i in range(signalLength.value):
            a.append(signalValue[i])
    if sys.version_info[0] != 3:
        a=str(a)

    return ret, a

def simxGetAndClearStringSignal(clientID, signalName, operationMode):
    """
    DEPRECATED. Refer to simxReadStringStream instead.Gets the value of a string signal, then clears it.  Useful to retrieve continuous data from the server. To pack/unpack integers/floats into/from a string, refer to simxPackInts, simxPackFloats, simxUnpackInts and simxUnpackFloats. See also simxGetStringSignal.
    number returnCode,string signalValue=simxGetAndClearStringSignal(number clientID,string signalName,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal
    :param operationMode: a remote API function operation mode. Since this function will clear a read signal, and we cannot afford to wait for a reply (well, we could, but that would mean a blocking operation), the function operates in a special mode and should be used as in following example:
    :param
    :param
    :param '''Initialization phase:'''
    :param err,signal=vrep.simxGetAndClearStringSignal(
    :param     clientID,"sig",vrep.simx_opmode_streaming)
    :param
    :param '''while we are connected:'''
    :param while vrep.simxGetConnectionId(clientID) != -1:
    :param   err,signal=vrep.simxGetAndClearStringSignal(
    :param     clientID,"sig",vrep.simx_opmode_buffer)
    :param   if (err==vrep.simx_return_ok):
    :param     '''A signal was retrieved.'''
    :param     '''Enable streaming again (was automatically disabled with the positive event):'''
    :param     err,signal=vrep.simxGetAndClearStringSignal(
    :param         clientID,"sig",vrep.simx_opmode_streaming)
    :param
    :param   ..

    :return returnCode: a remote API function return code
    :return signalValue: the value of the signal.
    """

    signalLength = ct.c_int();
    signalValue = ct.POINTER(ct.c_ubyte)()
    if (sys.version_info[0] == 3) and (type(signalName) is str):
        signalName=signalName.encode('utf-8')
    ret = c_GetAndClearStringSignal(clientID, signalName, ct.byref(signalValue), ct.byref(signalLength), operationMode)

    a = bytearray()
    if ret == 0:
        for i in range(signalLength.value):
            a.append(signalValue[i])
    if sys.version_info[0] != 3:
        a=str(a)

    return ret, a

def simxReadStringStream(clientID, signalName, operationMode):
    """
    Gets the value of a string signal, then clears it.  Useful to retrieve continuous data from the server. To pack/unpack integers/floats into/from a string, refer to simxPackInts, simxPackFloats, simxUnpackInts and simxUnpackFloats. See also simxWriteStringStream.
    number returnCode,string signalValue=simxReadStringStream(number clientID,string signalName,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls). simx_opmode_blocking is forbidden. Use a construction like following in order to continuously exchange data with V-REP:
    :param
    :param Remote API client side:
    :param
    :param '''Initialization phase:'''
    :param err,signal=vrep.simxReadStringStream(
    :param     clientID,"toClient",vrep.simx_opmode_streaming)
    :param
    :param '''while we are connected:'''
    :param while vrep.simxGetConnectionId(clientID) != -1:
    :param   err,signal=vrep.simxReadStringStream(
    :param     clientID,"toClient",vrep.simx_opmode_buffer)
    :param   if (err==vrep.simx_return_ok):
    :param     '''Data produced by the child script was retrieved! Send it back to the child script:'''
    :param     vrep.simxWriteStringStream(clientID,"fromClient",signal,vrep.simx_opmode_oneshot)
    :param
    :param
    :param Server side (V-REP), from a non-threaded child script:
    :param
    :param function sysCall_init()
    :param     -- initialization phase:
    :param     i=0
    :param     lastReceived=-1
    :param end
    :param
    :param function sysCall_actuation()
    :param     -- First send a stream of integers that count up:
    :param     dat=sim.getStringSignal('toClient')
    :param     if not dat then
    :param         dat=''
    :param     end
    :param     dat=dat..sim.packInt32Table({i})
    :param     i=i+1
    :param     sim.setStringSignal('toClient',dat)
    :param
    :param     -- Here receive the integer stream in return and check if each number is correct:
    :param     dat=sim.getStringSignal('fromClient')
    :param     if dat then
    :param         sim.clearStringSignal('fromClient')
    :param         dat=sim.unpackInt32Table(dat)
    :param         for j=1,#dat,1 do
    :param             if (dat[j]~=lastReceived+1) then
    :param                 print('Error')
    :param             else
    :param                 io.write('.')
    :param                 lastReceived=dat[j]
    :param             end
    :param         end
    :param     end
    :param end

    :return returnCode: a remote API function return code
    :return signalValue: the value of the signal.
    """

    signalLength = ct.c_int();
    signalValue = ct.POINTER(ct.c_ubyte)()
    if (sys.version_info[0] == 3) and (type(signalName) is str):
        signalName=signalName.encode('utf-8')
    ret = c_ReadStringStream(clientID, signalName, ct.byref(signalValue), ct.byref(signalLength), operationMode)

    a = bytearray()
    if ret == 0:
        for i in range(signalLength.value):
            a.append(signalValue[i])
    if sys.version_info[0] != 3:
        a=str(a)

    return ret, a

def simxSetFloatSignal(clientID, signalName, signalValue, operationMode):
    """
    (regular API equivalent: sim.setFloatSignal)
    Sets the value of a float signal. If that signal is not yet present, it is added. See also simxGetFloatSignal, simxClearFloatSignal, simxSetIntegerSignal and simxSetStringSignal.
    number returnCode=simxSetFloatSignal(number clientID,string signalName,number signalValue,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal
    :param signalValue: value of the signal
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    if (sys.version_info[0] == 3) and (type(signalName) is str):
        signalName=signalName.encode('utf-8')
    return c_SetFloatSignal(clientID, signalName, signalValue, operationMode)

def simxSetIntegerSignal(clientID, signalName, signalValue, operationMode):
    """
    (regular API equivalent: sim.setIntegerSignal)
    Sets the value of an integer signal. If that signal is not yet present, it is added. See also simxGetIntegerSignal, simxClearIntegerSignal, simxSetFloatSignal and simxSetStringSignal.
    number returnCode=simxSetIntegerSignal(number clientID,string signalName,number signalValue,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal
    :param signalValue: value of the signal
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    if (sys.version_info[0] == 3) and (type(signalName) is str):
        signalName=signalName.encode('utf-8')
    return c_SetIntegerSignal(clientID, signalName, signalValue, operationMode)

def simxSetStringSignal(clientID, signalName, signalValue, operationMode):
    """
    (regular API equivalent: sim.setStringSignal)
    Sets the value of a string signal. If that signal is not yet present, it is added. To pack/unpack integers/floats into/from a string, refer to simxPackInts, simxPackFloats, simxUnpackInts and simxUnpackFloats. See also simxWriteStringStream, simxGetStringSignal, simxClearStringSignal, simxSetIntegerSignal and simxSetFloatSignal.
    number returnCode=simxSetStringSignal(number clientID,string signalName,string signalValue,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal
    :param signalValue: value of the signal (which may contain any value, including embedded zeros)
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    sigV=signalValue
    if sys.version_info[0] == 3:
        if type(signalName) is str:
            signalName=signalName.encode('utf-8')
        if type(signalValue) is bytearray:
            sigV  = (ct.c_ubyte*len(signalValue))(*signalValue)
        if type(signalValue) is str:
            signalValue=signalValue.encode('utf-8')
            sigV  = (ct.c_ubyte*len(signalValue))(*signalValue)
    else:
        if type(signalValue) is bytearray:
            sigV = (ct.c_ubyte*len(signalValue))(*signalValue)
        if type(signalValue) is str:
            signalValue=bytearray(signalValue)
            sigV = (ct.c_ubyte*len(signalValue))(*signalValue)
    sigV=ct.cast(sigV,ct.POINTER(ct.c_ubyte)) # IronPython needs this
    return c_SetStringSignal(clientID, signalName, sigV, len(signalValue), operationMode)

def simxAppendStringSignal(clientID, signalName, signalValue, operationMode):
    """
    DEPRECATED. Refer to simxWriteStringStream instead.Appends a string to a string signal. If that signal is not yet present, it is added. To pack/unpack integers/floats into/from a string, refer to simxPackInts, simxPackFloats, simxUnpackInts and simxUnpackFloats. See also simxSetStringSignal.
    number returnCode=simxAppendStringSignal(number clientID,string signalName,string signalValueToAppend,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal
    :param signalValueToAppend: value to append to the  signal. That value may contain any value, including embedded zeros.
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    sigV=signalValue
    if sys.version_info[0] == 3:
        if type(signalName) is str:
            signalName=signalName.encode('utf-8')
        if type(signalValue) is bytearray:
            sigV  = (ct.c_ubyte*len(signalValue))(*signalValue)
        if type(signalValue) is str:
            signalValue=signalValue.encode('utf-8')
            sigV  = (ct.c_ubyte*len(signalValue))(*signalValue)
    else:
        if type(signalValue) is bytearray:
            sigV = (ct.c_ubyte*len(signalValue))(*signalValue)
        if type(signalValue) is str:
            signalValue=bytearray(signalValue)
            sigV = (ct.c_ubyte*len(signalValue))(*signalValue)
    sigV=ct.cast(sigV,ct.POINTER(ct.c_ubyte)) # IronPython needs this
    return c_AppendStringSignal(clientID, signalName, sigV, len(signalValue), operationMode)

def simxWriteStringStream(clientID, signalName, signalValue, operationMode):
    """
    Appends a string to a string signal. If that signal is not yet present, it is added. To pack/unpack integers/floats into/from a string, refer to simxPackInts, simxPackFloats, simxUnpackInts and simxUnpackFloats. See also simxReadStringStream.
    number returnCode=simxWriteStringStream(number clientID,string signalName,string signalValueToAppend,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal
    :param signalValueToAppend: value to append to the  signal. That value may contain any value, including embedded zeros.
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    sigV=signalValue
    if sys.version_info[0] == 3:
        if type(signalName) is str:
            signalName=signalName.encode('utf-8')
        if type(signalValue) is bytearray:
            sigV  = (ct.c_ubyte*len(signalValue))(*signalValue)
        if type(signalValue) is str:
            signalValue=signalValue.encode('utf-8')
            sigV  = (ct.c_ubyte*len(signalValue))(*signalValue)
    else:
        if type(signalValue) is bytearray:
            sigV = (ct.c_ubyte*len(signalValue))(*signalValue)
        if type(signalValue) is str:
            signalValue=bytearray(signalValue)
            sigV = (ct.c_ubyte*len(signalValue))(*signalValue)
    sigV=ct.cast(sigV,ct.POINTER(ct.c_ubyte)) # IronPython needs this
    return c_WriteStringStream(clientID, signalName, sigV, len(signalValue), operationMode)

def simxGetObjectFloatParameter(clientID, objectHandle, parameterID, operationMode):
    """
    (regular API equivalent: sim.getObjectFloatParameter)
    Retrieves a floating-point parameter of a object. See also simxSetObjectFloatParameter and simxGetObjectIntParameter.
    number returnCode,number parameterValue=simxGetObjectFloatParameter(number clientID,number objectHandle,number parameterID,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param parameterID: identifier of the parameter to retrieve. See the list of all possible object parameter identifiers
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls), or simx_opmode_blocking (depending on the intended usage)

    :return returnCode: a remote API function return code
    :return parameterValue: the value of the parameter
    """

    parameterValue = ct.c_float()
    return c_GetObjectFloatParameter(clientID, objectHandle, parameterID, ct.byref(parameterValue), operationMode), parameterValue.value

def simxSetObjectFloatParameter(clientID, objectHandle, parameterID, parameterValue, operationMode):
    """
    (regular API equivalent: sim.setObjectFloatParameter)
    Sets a floating-point parameter of a object. See also simxGetObjectFloatParameter and simxSetObjectIntParameter.
    number returnCode=simxSetObjectFloatParameter(number clientID,number objectHandle,number parameterID,number parameterValue,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param parameterID: identifier of the parameter to set. See the list of all possible object parameter identifiers
    :param parameterValue: the desired value of the parameter
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    return c_SetObjectFloatParameter(clientID, objectHandle, parameterID, parameterValue, operationMode)

def simxGetObjectIntParameter(clientID, objectHandle, parameterID, operationMode):
    """
    (regular API equivalent: sim.getObjectInt32Parameter)
    Retrieves an integer parameter of a object. See also simxSetObjectIntParameter and simxGetObjectFloatParameter.
    number returnCode,number parameterValue=simxGetObjectIntParameter(number clientID,number objectHandle,number parameterID,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param parameterID: identifier of the parameter to retrieve. See the list of all possible object parameter identifiers
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls), or simx_opmode_blocking (depending on the intended usage)

    :return returnCode: a remote API function return code
    :return parameterValue: the value of the parameter
    """

    parameterValue = ct.c_int()
    return c_GetObjectIntParameter(clientID, objectHandle, parameterID, ct.byref(parameterValue), operationMode), parameterValue.value

def simxSetObjectIntParameter(clientID, objectHandle, parameterID, parameterValue, operationMode):
    """
    (regular API equivalent: sim.setObjectInt32Parameter)
    Sets an integer parameter of a object. See also simxGetObjectIntParameter and simxSetObjectFloatParameter.
    number returnCode=simxSetObjectIntParameter(number clientID,number objectHandle,number parameterID,number parameterValue,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param parameterID: identifier of the parameter to set. See the list of all possible object parameter identifiers
    :param parameterValue: the desired value of the parameter
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    return c_SetObjectIntParameter(clientID, objectHandle, parameterID, parameterValue, operationMode)

def simxGetModelProperty(clientID, objectHandle, operationMode):
    """
    (regular API equivalent: sim.getModelProperty)
    Retrieves the properties of a model. See also simxSetModelProperty.
    number returnCode,number prop=simxGetModelProperty(number clientID,number objectHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls), or simx_opmode_blocking (depending on the intended usage)

    :return returnCode: a remote API function return code
    :return prop: the model property value
    """
    prop = ct.c_int()
    return c_GetModelProperty(clientID, objectHandle, ct.byref(prop), operationMode), prop.value

def simxSetModelProperty(clientID, objectHandle, prop, operationMode):
    """
    (regular API equivalent: sim.setModelProperty)
    Sets the properties of a model. See also simxGetModelProperty.
    number returnCode=simxSetModelProperty(number clientID,number objectHandle,number prop,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param prop: a model property value
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    return c_SetModelProperty(clientID, objectHandle, prop, operationMode)

def simxStart(connectionAddress, connectionPort, waitUntilConnected, doNotReconnectOnceDisconnected, timeOutInMs, commThreadCycleInMs):
    """
    Starts a communication thread with the server (i.e. V-REP). A same client may start several communication threads  (but only one communication thread for a given IP and port). This should be the very first remote API function called on the client side. Make sure to start an appropriate remote API server service on the server side, that will wait for a connection. See also simxFinish. This is a remote API helper function.
    number clientID=simxStart(string connectionAddress,number connectionPort,boolean waitUntilConnected,boolean doNotReconnectOnceDisconnected,number timeOutInMs,number commThreadCycleInMs)

    :param connectionAddress: the ip address where the server is located (i.e. V-REP)
    :param connectionPort: the port number where to connect. Specify a negative port number in order to use shared memory, instead of socket communication.
    :param waitUntilConnected: if True, then the function blocks until connected (or timed out).
    :param doNotReconnectOnceDisconnected: if True, then the communication thread will not attempt a second connection if a connection was lost.
    :param timeOutInMs:
    :param  if positive: the connection time-out in milliseconds for the first connection attempt. In that case, the time-out for blocking function calls is 5000 milliseconds.
    :param  if negative: its positive value is the time-out for blocking function calls. In that case, the connection time-out for the first connection attempt is 5000 milliseconds.
    :param commThreadCycleInMs: indicates how often data packets are sent back and forth. Reducing this number improves responsiveness, and a default value of 5 is recommended.

    :return clientID: the client ID, or -1 if the connection to the server was not possible (i.e. a timeout was reached). A call to simxStart should always be followed at the end with a call to simxFinish if simxStart didn't return -1
    """

    if (sys.version_info[0] == 3) and (type(connectionAddress) is str):
        connectionAddress=connectionAddress.encode('utf-8')
    return c_Start(connectionAddress, connectionPort, waitUntilConnected, doNotReconnectOnceDisconnected, timeOutInMs, commThreadCycleInMs)

def simxFinish(clientID):
    """
    Ends the communication thread. This should be the very last remote API function called on the client side. simxFinish should only be called after a successfull call to simxStart. This is a remote API helper function.
    simxFinish(number clientID)

    :param clientID: the client ID. refer to simxStart.  Can be -1 to end all running communication threads.

    :return none
    """

    return c_Finish(clientID)

def simxGetPingTime(clientID):
    """
    Retrieves the time needed for a command to be sent to the server, executed, and sent back. That time depends on various factors like the client settings, the network load, whether a simulation is running, whether the simulation is real-time, the simulation time step, etc. The function is blocking. This is a remote API helper function.
    number returnCode,number pingTime=simxGetPingTime(number clientID)

    :param clientID: the client ID. refer to simxStart.

    :return returnCode: a remote API function return code
    :return pingTime: a pointer to a simxInt value accepting the ping time in milliseconds.
    """
    pingTime = ct.c_int()
    return c_GetPingTime(clientID, ct.byref(pingTime)), pingTime.value

def simxGetLastCmdTime(clientID):
    """
    Retrieves the simulation time of the last fetched command (i.e. when the last fetched command was processed on the server side). The function can be used to verify how "fresh" a command reply is, or whether a command reply was recently updated. For example:


data=vrep.simxGetVisionSensorImage(clientID,handle,0,vrep.simx_opmode_buffer)
if data[0] == vrep.simx_return_ok :
    imageAcquisitionTime=vrep.simxGetLastCmdTime(clientID)


If some streaming commands are running, simxGetLastCmdTime will always retrieve the current simulation time, otherwise, only the simulation time of the last command that retrieved data from V-REP. This is a remote API helper function.
    number cmdTime=simxGetLastCmdTime(number clientID)

    :param clientID: the client ID. refer to simxStart.

    :return cmdTime: the simulation time in milliseconds when the command reply was generated, or 0 if simulation was not running.
    """

    return c_GetLastCmdTime(clientID)

def simxSynchronousTrigger(clientID):
    """
    Sends a synchronization  trigger signal to the server. The function is blocking. The server needs to be previously enabled for synchronous operation via the simxSynchronous function. The trigger signal will inform V-REP to execute the next simulation step (i.e. to call simHandleMainScript). While in synchronous operation mode, the client application is in charge of triggering the next simulation step, otherwise simulation will stall. See also this section. This is a remote API helper function.
    number returnCode=simxSynchronousTrigger(number clientID)

    :param clientID: the client ID. refer to simxStart.

    :return returnCode: a remote API function return code
    """

    return c_SynchronousTrigger(clientID)

def simxSynchronous(clientID, enable):
    """
    Enables or disables the synchronous operation mode for the remote API server service that the client is connected to. The function is blocking. While in synchronous operation mode, the client application is in charge of triggering the next simulation step. Only pre-enabled remote API server services will successfully execute this function. See also simxSynchronousTrigger and this section. This is a remote API helper function.
    number returnCode=simxSynchronous(number clientID,boolean enable)

    :param clientID: the client ID. refer to simxStart.
    :param enable: the enable state of the synchronous operation

    :return returnCode: a remote API function return code
    """

    return c_Synchronous(clientID, enable)

def simxPauseCommunication(clientID, enable):
    """
    Allows to temporarily halt the communication thread from sending data. This can be useful if you need to send several values to V-REP that should be received and evaluated at the same time. This is a remote API helper function.
    number returnCode=simxPauseCommunication(number clientID,boolean pause)

    :param clientID: the client ID. refer to simxStart.
    :param pause: whether the communication thread should pause or run normally.
    :param
    :param
    :param Usage example:
    :param
    :param vrep.simxPauseCommunication(clientID,True)
    :param vrep.simxSetJointPosition(clientID,joint1Handle,joint1Value,vrep.simx_opmode_oneshot)
    :param vrep.simxSetJointPosition(clientID,joint2Handle,joint2Value,vrep.simx_opmode_oneshot)
    :param vrep.simxSetJointPosition(clientID,joint3Handle,joint3Value,vrep.simx_opmode_oneshot)
    :param vrep.simxPauseCommunication(clientID,False)
    :param
    :param '''Above's 3 joints will be received and set on the V-REP side at the same time'''

    :return returnCode: 0 in case of operation success.
    """

    return c_PauseCommunication(clientID, enable)

def simxGetInMessageInfo(clientID, infoType):
    """
    Retrieves information about the last received message from the server. This is a remote API helper function. See also simxGetOutMessageInfo.

If the client didn't receive any command reply from the server for a while, the data retrieved with this function won't be up-to-date. In order to avoid this, you should start at least one streaming command, which will guarantee regular message income.
    number result,number info=simxGetInMessageInfo(number clientID,number infoType)

    :param clientID: the client ID. refer to simxStart.
    :param infoType: an inbox message info type

    :return result: -1 in case of an error
    :return info: the requested information
    """
    info = ct.c_int()
    return c_GetInMessageInfo(clientID, infoType, ct.byref(info)), info.value

def simxGetOutMessageInfo(clientID, infoType):
    """
    Retrieves information about the next message to send to the server. This is a remote API helper function. See also simxGetInMessageInfo.
    number result,number info=simxGetOutMessageInfo(number clientID,number infoType)

    :param clientID: the client ID. refer to simxStart.
    :param infoType: an outbox message info type

    :return result:-1 in case of an error
    :return info: the requested information
    """
    info = ct.c_int()
    return c_GetOutMessageInfo(clientID, infoType, ct.byref(info)), info.value

def simxGetConnectionId(clientID):
    """
    Returns the ID of the current connection. Use this function to track the connection state to the server. See also simxStart. This is a remote API helper function.
    number connectionId=simxGetConnectionId(number clientID)

    :param clientID: the client ID. refer to simxStart.

    :return connectionId: a connection ID, or -1 if the client is not connected to the server. Different connection IDs indicate temporary disconections in-between.
    """

    return c_GetConnectionId(clientID)

def simxCreateBuffer(bufferSize):
    """
    (regular API equivalent: simCreateBuffer)
    Creates a buffer. The buffer needs to be released with simxReleaseBuffer except otherwise explicitly specified. This is a remote API helper function.
    charPointer buffer=simxCreateBuffer(number bufferSize)

    :param bufferSize: size of the buffer in bytes

    :return buffer: the created buffer
    """

    return c_CreateBuffer(bufferSize)

def simxReleaseBuffer(buffer):
    """
    (regular API equivalent: simReleaseBuffer)
    Releases a buffer previously created with simxCreateBuffer or a buffer returned by a remote API function. This is a remote API helper function.
    simxReleaseBuffer(charPointer buffer)

    :param buffer: buffer to be released

    :return none
    """

    return c_ReleaseBuffer(buffer)

def simxTransferFile(clientID, filePathAndName, fileName_serverSide, timeOut, operationMode):
    """
    Allows transferring a file from the client to the server. This function is used by several other functions internally (e.g. simxLoadModel). See also simxEraseFile. This is a remote API helper function.
    number returnCode=simxTransferFile(number clientID,string filePathAndName,string fileName_serverSide,number timeOut,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param filePathAndName: the local file name and path (i.e. on the client side)
    :param fileName_serverSide: a file name under which the transferred file will be saved on the server side. For now, do not specify a path (the file will be saved in the remote API plugin directory)
    :param timeOut: a timeout value in milliseconds
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    """

    if (sys.version_info[0] == 3) and (type(filePathAndName) is str):
        filePathAndName=filePathAndName.encode('utf-8')
    return c_TransferFile(clientID, filePathAndName, fileName_serverSide, timeOut, operationMode)

def simxEraseFile(clientID, fileName_serverSide, operationMode):
    """
    Erases a file on the server side. This function is used by several other functions internally (e.g. simxLoadModel). See also simxTransferFile. This is a remote API helper function.
    number returnCode=simxEraseFile(number clientID,string fileName_serverSide,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param fileName_serverSide: the file to erase on the server side. For now, do not specify a path (the file will be erased in the remote API plugin directory)
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_oneshot

    :return returnCode: a remote API function return code
    """

    if (sys.version_info[0] == 3) and (type(fileName_serverSide) is str):
        fileName_serverSide=fileName_serverSide.encode('utf-8')
    return c_EraseFile(clientID, fileName_serverSide, operationMode)

def simxCreateDummy(clientID, size, color, operationMode):
    """
    (regular API equivalent: sim.createDummy)
    Creates a dummy in the scene.
    number returnCode,number dummyHandle=simxCreateDummy(number clientID,number size,array colors,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param size: the size of the dummy.
    :param colors: 4*3 bytes (0-255) for ambient_diffuse RGB, 3 reserved values (set to zero), specular RGB and emissive RGB. Can be None for default colors.
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return dummyHandle: handle of the created dummy.
    """

    handle = ct.c_int()
    if color != None:
        c_color = (ct.c_ubyte*12)(*color)
    else:
        c_color = None
    return c_CreateDummy(clientID, size, c_color, ct.byref(handle), operationMode), handle.value

def simxQuery(clientID, signalName, signalValue, retSignalName, timeOutInMs):
    """
    DEPRECATED. Refer to simxCallScriptFunction instead.Sends a query string to V-REP, and waits for a reply string. Query and reply strings can be accessed via string signals. This function allows for instance to have a child script, another remote API client or a ROS node handle special requests coming from this remote API client, then send a reply back. To pack/unpack integers/floats into/from a string, refer to simxPackInts, simxPackFloats, simxUnpackInts and simxUnpackFloats.


Usage example where a child script handles a request:

# Following is the remote API client side:
res,replyData=vrep.simxQuery(clientID,'request','send me a 42','reply',5000)
if res==vrep.simx_return_ok:
    print "The reply is: %s" % replyData


-- This is the child script side. The child script is non-threaded and
-- following part executed at each simulation pass:
req=sim.getStringSignal("request")
if (req) then
    sim.clearStringSignal("request")
    if (req=="send me a 42") then
        sim.setStringSignal("reply","42\0") -- will be automatically cleared by the client
    end
end
    number returnCode,string retSignalValue=simxQuery(number clientID,string signalName,string signalValue,string retSignalName,number timeOutInMs)

    :param clientID: the client ID. refer to simxStart.
    :param signalName: name of the signal that contains the request string
    :param signalValue: the request string.
    :param retSignalName: name of the signal that contains the reply string
    :param timeOutInMs: the maximum time in milliseconds that the function will wait for a reply.

    :return returnCode: a remote API function return code
    :return retSignalValue: the reply string
    """

    retSignalLength = ct.c_int();
    retSignalValue = ct.POINTER(ct.c_ubyte)()

    sigV=signalValue
    if sys.version_info[0] == 3:
        if type(signalName) is str:
            signalName=signalName.encode('utf-8')
        if type(retSignalName) is str:
            retSignalName=retSignalName.encode('utf-8')
        if type(signalValue) is bytearray:
            sigV  = (ct.c_ubyte*len(signalValue))(*signalValue)
        if type(signalValue) is str:
            signalValue=signalValue.encode('utf-8')
            sigV  = (ct.c_ubyte*len(signalValue))(*signalValue)
    else:
        if type(signalValue) is bytearray:
            sigV = (ct.c_ubyte*len(signalValue))(*signalValue)
        if type(signalValue) is str:
            signalValue=bytearray(signalValue)
            sigV = (ct.c_ubyte*len(signalValue))(*signalValue)
    sigV=ct.cast(sigV,ct.POINTER(ct.c_ubyte)) # IronPython needs this

    ret = c_Query(clientID, signalName, sigV, len(signalValue), retSignalName, ct.byref(retSignalValue), ct.byref(retSignalLength), timeOutInMs)

    a = bytearray()
    if ret == 0:
        for i in range(retSignalLength.value):
            a.append(retSignalValue[i])
    if sys.version_info[0] != 3:
        a=str(a)

    return ret, a

def simxGetObjectGroupData(clientID, objectType, dataType, operationMode):
    """
    Simultaneously retrieves data of various objects in a V-REP scene.
    number returnCode,array handles,array intData,array floatData,array stringData=simxGetObjectGroupData(number clientID,number objectType,number dataType,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectType: a scene object type, sim_appobj_object_type for all scene objects, or a collection handle.
    :param dataType: the type of data that is desired:
    :param 0: retrieves the object names (in stringData.)
    :param 1: retrieves the object types (in intData)
    :param 2: retrieves the parent object handles (in intData)
    :param 3: retrieves the absolute object positions (in floatData. There are 3 values for each object (x,y,z))
    :param 4: retrieves the local object positions (in floatData. There are 3 values for each object (x,y,z))
    :param 5: retrieves the absolute object orientations as Euler angles (in floatData. There are 3 values for each object (alpha,beta,gamma))
    :param 6: retrieves the local object orientations as Euler angles (in floatData. There are 3 values for each object (alpha,beta,gamma))
    :param 7: retrieves the absolute object orientations as quaternions (in floatData. There are 4 values for each object (qx,qy,qz,qw))
    :param 8: retrieves the local object orientations as quaternions (in floatData. There are 4 values for each object (qx,qy,qz,qw))
    :param 9: retrieves the absolute object positions and orientations (as Euler angles) (in floatData. There are 6 values for each object (x,y,z,alpha,beta,gamma))
    :param 10: retrieves the local object positions and orientations (as Euler angles) (in floatData. There are 6 values for each object (x,y,z,alpha,beta,gamma))
    :param 11: retrieves the absolute object positions and orientations (as quaternions) (in floatData. There are 7 values for each object (x,y,z,qx,qy,qz,qw))
    :param 12: retrieves the local object positions and orientations (as quaternions) (in floatData. There are 7 values for each object (x,y,z,qx,qy,qz,qw))
    :param 13: retrieves proximity sensor data (in intData (2 values): detection state, detected object handle. In floatData (6 values): detected point (x,y,z) and detected surface normal (nx,ny,nz))
    :param 14: retrieves force sensor data (in intData (1 values): force sensor state. In floatData (6 values): force (fx,fy,fz) and torque (tx,ty,tz))
    :param 15: retrieves joint state data (in floatData (2 values): position, force/torque)
    :param 16: retrieves joint properties data (in intData (2 values): joint type, joint mode (bit16=hybid operation). In floatData (2 values): joint limit low, joint range (-1.0 if joint is cyclic))
    :param 17: retrieves the object linear velocity (in floatData. There are 3 values for each object (vx,vy,vz))
    :param 18: retrieves the object angular velocity as Euler angles per seconds (in floatData. There are 3 values for each object (dAlpha,dBeta,dGamma))
    :param 19: retrieves the object linear and angular velocity (in floatData. There are 6 values for each object (vx,vy,vz,dAlpha,dBeta,dGamma))
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking or simx_opmode_streaming.

    :return returnCode: a remote API function return code
    :return handles: the object handles.
    :return intData: the integer values.
    :return floatData: the float values.
    :return stringData: the string values.
    """

    handles =[]
    intData =[]
    floatData =[]
    stringData =[]
    handlesC = ct.c_int()
    handlesP = ct.POINTER(ct.c_int)()
    intDataC = ct.c_int()
    intDataP = ct.POINTER(ct.c_int)()
    floatDataC = ct.c_int()
    floatDataP = ct.POINTER(ct.c_float)()
    stringDataC = ct.c_int()
    stringDataP = ct.POINTER(ct.c_char)()
    ret = c_GetObjectGroupData(clientID, objectType, dataType, ct.byref(handlesC), ct.byref(handlesP), ct.byref(intDataC), ct.byref(intDataP), ct.byref(floatDataC), ct.byref(floatDataP), ct.byref(stringDataC), ct.byref(stringDataP), operationMode)

    if ret == 0:
        for i in range(handlesC.value):
            handles.append(handlesP[i])
        for i in range(intDataC.value):
            intData.append(intDataP[i])
        for i in range(floatDataC.value):
            floatData.append(floatDataP[i])
        s = 0
        for i in range(stringDataC.value):
            a = bytearray()
            while stringDataP[s] != b'\0':
                if sys.version_info[0] == 3:
                    a.append(int.from_bytes(stringDataP[s],'big'))
                else:
                    a.append(stringDataP[s])
                s += 1
            s += 1 #skip null
            if sys.version_info[0] == 3:
                a=str(a,'utf-8')
            else:
                a=str(a)
            stringData.append(a)

    return ret, handles, intData, floatData, stringData

def simxCallScriptFunction(clientID, scriptDescription, options, functionName, inputInts, inputFloats, inputStrings, inputBuffer, operationMode):
    """
    (regular API equivalent: sim.callScriptFunction)
    Remotely calls a V-REP script function. When calling simulation scripts, then simulation must be running (and threaded scripts must still be running, i.e. not ended yet). Refer to this section for additional details.
    number returnCode,array outInts,array outFloats,array outStrings,string outBuffer=simxCallScriptFunction(number clientID,string scriptDescription,number scriptHandleOrType,string functionName,array inInts,array inFloats,array inStrings,string inBuffer,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param scriptDescription: the name of the scene object where the script is attached to, or an empty string if the script has no associated scene object.
    :param scriptHandleOrType: the handle of the script, otherwise the type of the script:
    :param sim_scripttype_mainscript (0): the main script will be called.
    :param sim_scripttype_childscript (1): a child script will be called.
    :param sim_scripttype_customizationscript (6): a customization script will be called.
    :param functionName: the name of the Lua function to call in the specified script.
    :param inInts: the input integer values that are handed over to the script function. Can be [].
    :param inFloats: the input floating-point values that are handed over to the script function. Can be [].
    :param inStrings: the input strings that are handed over to the script function. Can be [].
    :param inBuffer: the input buffer that is handed over to the script function. Should be a bytearray.
    :param operationMode: a remote API function operation mode. Recommended operation mode for this function is simx_opmode_blocking

    :return returnCode: a remote API function return code
    :return outInts: the returned integer values.
    :return outFloats: the returned floating-point values.
    :return outStrings: the returned strings.
    :return outBuffer: the returned buffer.
    """

    inputBufferV=inputBuffer
    if sys.version_info[0] == 3:
        if type(scriptDescription) is str:
            scriptDescription=scriptDescription.encode('utf-8')
        if type(functionName) is str:
            functionName=functionName.encode('utf-8')
        if type(inputBuffer) is bytearray:
            inputBufferV  = (ct.c_ubyte*len(inputBuffer))(*inputBuffer)
        if type(inputBuffer) is str:
            inputBuffer=inputBuffer.encode('utf-8')
            inputBufferV  = (ct.c_ubyte*len(inputBuffer))(*inputBuffer)
    else:
        if type(inputBuffer) is bytearray:
            inputBufferV = (ct.c_ubyte*len(inputBuffer))(*inputBuffer)
        if type(inputBuffer) is str:
            inputBuffer=bytearray(inputBuffer)
            inputBufferV = (ct.c_ubyte*len(inputBuffer))(*inputBuffer)
    inputBufferV=ct.cast(inputBufferV,ct.POINTER(ct.c_ubyte)) # IronPython needs this

    c_inInts  = (ct.c_int*len(inputInts))(*inputInts)
    c_inInts = ct.cast(c_inInts,ct.POINTER(ct.c_int)) # IronPython needs this
    c_inFloats  = (ct.c_float*len(inputFloats))(*inputFloats)
    c_inFloats = ct.cast(c_inFloats,ct.POINTER(ct.c_float)) # IronPython needs this

    concatStr=''.encode('utf-8')
    for i in range(len(inputStrings)):
        a=inputStrings[i]
        a=a+'\0'
        if type(a) is str:
            a=a.encode('utf-8')
        concatStr=concatStr+a
    c_inStrings  = (ct.c_char*len(concatStr))(*concatStr)

    intDataOut =[]
    floatDataOut =[]
    stringDataOut =[]
    bufferOut =bytearray()

    intDataC = ct.c_int()
    intDataP = ct.POINTER(ct.c_int)()
    floatDataC = ct.c_int()
    floatDataP = ct.POINTER(ct.c_float)()
    stringDataC = ct.c_int()
    stringDataP = ct.POINTER(ct.c_char)()
    bufferS = ct.c_int()
    bufferP = ct.POINTER(ct.c_ubyte)()

    ret = c_CallScriptFunction(clientID,scriptDescription,options,functionName,len(inputInts),c_inInts,len(inputFloats),c_inFloats,len(inputStrings),c_inStrings,len(inputBuffer),inputBufferV,ct.byref(intDataC),ct.byref(intDataP),ct.byref(floatDataC),ct.byref(floatDataP),ct.byref(stringDataC),ct.byref(stringDataP),ct.byref(bufferS),ct.byref(bufferP),operationMode)

    if ret == 0:
        for i in range(intDataC.value):
            intDataOut.append(intDataP[i])
        for i in range(floatDataC.value):
            floatDataOut.append(floatDataP[i])
        s = 0
        for i in range(stringDataC.value):
            a = bytearray()
            while stringDataP[s] != b'\0':
                if sys.version_info[0] == 3:
                    a.append(int.from_bytes(stringDataP[s],'big'))
                else:
                    a.append(stringDataP[s])
                s += 1
            s += 1 #skip null
            if sys.version_info[0] == 3:
                a=str(a,'utf-8')
            else:
                a=str(a)
            stringDataOut.append(a)
        for i in range(bufferS.value):
            bufferOut.append(bufferP[i])
    if sys.version_info[0] != 3:
        bufferOut=str(bufferOut)

    return ret, intDataOut, floatDataOut, stringDataOut, bufferOut

def simxGetObjectVelocity(clientID, objectHandle, operationMode):
    """
    (regular API equivalent: sim.getObjectVelocity)
    Retrieves the linear and angular velocity of an object. See also simxGetObjectPosition,  simxGetObjectOrientation and simxGetObjectGroupData.
    number returnCode,array linearVelocity,array angularVelocity=simxGetObjectVelocity(number clientID,number objectHandle,number operationMode)

    :param clientID: the client ID. refer to simxStart.
    :param objectHandle: handle of the object
    :param operationMode: a remote API function operation mode. Recommended operation modes for this function are simx_opmode_streaming (the first call) and simx_opmode_buffer (the following calls)

    :return returnCode: a remote API function return code
    :return linearVelocity: the linear velocity (vx, vy, vz)
    :return angularVelocity: the angular velocity (dAlpha, dBeta, dGamma)
    """
    linearVel  = (ct.c_float*3)()
    angularVel = (ct.c_float*3)()
    ret = c_GetObjectVelocity(clientID, objectHandle, linearVel, angularVel, operationMode)
    arr1 = []
    for i in range(3):
        arr1.append(linearVel[i])
    arr2 = []
    for i in range(3):
        arr2.append(angularVel[i])
    return ret, arr1, arr2

def simxPackInts(intList):
    """
    Packs an array of integers into a string.  This is a remote API helper function. See also simxUnpackInts and simxPackFloats.
    string packedData=simxPackInts(array intValues)

    :param intValues: an array of numbers we wish to pack as integers

    :return packedData: a string that contains the packed values. Each values takes exactly 4 bytes in the string.
    """

    if sys.version_info[0] == 3:
        s=bytes()
        for i in range(len(intList)):
            s=s+struct.pack('<i',intList[i])
        s=bytearray(s)
    else:
        s=''
        for i in range(len(intList)):
            s+=struct.pack('<i',intList[i])
    return s

def simxUnpackInts(intsPackedInString):
    """
    Unpacks a string into an array of integers.  This is a remote API helper function. See also simxPackInts and simxUnpackFloats.
    array intValues=simxUnpackInts(string packedData)

    :param packedData: a string that contains the packed values. Each values takes exactly 4 bytes in the string.

    :return intValues: an array of numbers that were unpacked as integers
    """
    b=[]
    for i in range(int(len(intsPackedInString)/4)):
        b.append(struct.unpack('<i',intsPackedInString[4*i:4*(i+1)])[0])
    return b

def simxPackFloats(floatList):
    """
    Packs an array of floats into a string.  This is a remote API helper function. See also simxUnpackFloats and simxPackInts.
    string packedData=simxPackFloats(array floatValues)

    :param floatValues: an array of numbers we wish to pack as floats

    :return packedData: a string that contains the packed values. Each values takes exactly 4 bytes in the string.
    """

    if sys.version_info[0] == 3:
        s=bytes()
        for i in range(len(floatList)):
            s=s+struct.pack('<f',floatList[i])
        s=bytearray(s)
    else:
        s=''
        for i in range(len(floatList)):
            s+=struct.pack('<f',floatList[i])
    return s

def simxUnpackFloats(floatsPackedInString):
    """
    Unpacks a string into an array of floats.  This is a remote API helper function. See also simxPackFloats and simxUnpackInts.
    array floatValues=simxUnpackFloats(string packedData)

    :param packedData: a string that contains the packed values. Each values takes exactly 4 bytes in the string.

    :return floatValues: an array of numbers that were unpacked as floats
    """
    b=[]
    for i in range(int(len(floatsPackedInString)/4)):
        b.append(struct.unpack('<f',floatsPackedInString[4*i:4*(i+1)])[0])
    return b
