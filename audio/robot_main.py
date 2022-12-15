#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import Int32
from std_msgs.msg import Int64
from op3_walking_module_msgs.msg import
WalkingParam
from robotis_controller_msgs.msg import StatusMsg
from sensor_msgs.msg import JointState

class Model:

def __init__(self):

#Initialization Global Variable
    self.a = 0
    self.btn = 1
    self.blt = 0
    self.lock_stop_gerak = 0
    self.lock_stop_jalan = 0
    self.sg = 0
    self.sw = 0

    #ROS Subscriber
    rospy.Subscriber("/robotis/status",
    StatusMsg, self.status)
    rospy.Subscriber("/robotis/btn", Int32,
    self.button_callback)
    rospy.Subscriber("/robotis/blt", Int32,
    self.bluetooth_callback)

    #ROS Publisher

    self.pubEnCtrl=rospy.Publisher("/robotis/enable_c
    trl_module",String,queue_size=4)

    self.pubCommand=rospy.Publisher("/robotis/walking
    /command",String,queue_size=5)

    self.pubWalkParam=rospy.Publisher("/robotis/walki
    ng/set_params",WalkingParam,queue_size=5)

    self.pubActPage=rospy.Publisher("/robotis/action/
    page_num",Int32,queue_size=5)

    self.pubDxlJoint=rospy.Publisher("/robotis/direct
    _control/set_joint_states",JointState,queue_size=5
    )
    self.walkF.init_x_offset = -0.019999999553
    self.walkF.init_y_offset = 0.0450000017881
    self.walkF.init_z_offset = 0.0340000018477
    self.walkF.init_roll_offset = 0.122173048556
    self.walkF.init_pitch_offset = -
    0.0349065847695
    self.walkF.init_yaw_offset = -
    0.0174532923847
    self.walkF.period_time = 1.29999995232
    self.walkF.dsp_ratio = 0.5
    self.walkF.step_fb_ratio = 0.280000001192
    self.walkF.x_move_amplitude = 0.019999999553
    self.walkF.y_move_amplitude = 0.0
    self.walkF.z_move_amplitude =
    0.0500000007451
    self.walkF.angle_move_amplitude = -
    0.0174532923847
    self.walkF.move_aim_on = True
    self.walkF.balance_enable = True
    self.walkF.balance_hip_roll_gain =
    0.10000000149
    self.walkF.balance_knee_gain =
    0.300000011921
    self.walkF.balance_ankle_roll_gain =
    0.699999988079
    self.walkF.balance_ankle_pitch_gain =
    0.899999976158
    self.walkF.y_swap_amplitude = 0.019999999553

    self.walkF.z_swap_amplitude =
    0.0130000002682
    self.walkF.arm_swing_gain = 0.20000000298
    self.walkF.pelvis_offset = 0.00872664619237
    self.walkF.hip_pitch_offset =
    0.0872664600611
    self.walkF.p_gain = 0
    self.walkF.i_gain = 0
    self.walkF.d_gain = 0

    self.walkL1 = WalkingParam()
    self.walkL1.init_x_offset=(-0.019999999553)
    self.walkL1.init_y_offset=(0.0450000017881)
    self.walkL1.init_z_offset=(0.0250000003725)

    self.walkL1.init_roll_offset=(0.069813169539)
    self.walkL1.init_pitch_offset=(-
    0.0139626339078)
    self.walkL1.init_yaw_offset=(0.0)
    self.walkL1.period_time=(1.29999995232)
    self.walkL1.dsp_ratio=(0.5)
    self.walkL1.step_fb_ratio=(0.280000001192)

    self.walkL1.x_move_amplitude=(0.019999999553)
    self.walkL1.y_move_amplitude=(0.00)

    self.walkL1.z_move_amplitude=(0.0500000007451)
    self.walkL1.angle_move_amplitude=(-
    0.0174532923847)
    self.walkL1.move_aim_on=(True)
    self.walkL1.balance_enable=(True)

    self.walkL1.balance_hip_roll_gain=(0.34999999404)

    self.walkL1.balance_knee_gain=(0.300000011921)

    self.walkL1.balance_ankle_roll_gain=(0.6999999880
    79)

    self.walkL1.balance_ankle_pitch_gain=(0.899999976
    158)

    self.walkL1.y_swap_amplitude=(0.019999999553)

    self.walkL1.z_swap_amplitude=(0.0130000002682)
    self.walkL1.arm_swing_gain=(0.20000000298)
    self.walkL1.pelvis_offset=(0.00872664619237)

    self.walkL1.hip_pitch_offset=(0.157079637051)
    self.walkL1.p_gain=(0)
    self.walkL1.i_gain=(0)
    self.walkL1.d_gain=(0)

    self.walkL2 = WalkingParam()
    self.walkL2.init_x_offset=(-0.019999999553)
    self.walkL2.init_y_offset=(0.0450000017881)
    self.walkL2.init_z_offset=(0.0250000003725)

    self.walkL2.init_roll_offset=(0.069813169539)
    self.walkL2.init_pitch_offset=(-
    0.0139626339078)
    self.walkL2.init_yaw_offset=(0.0)
    self.walkL2.period_time=(1.29999995232)

    self.walkL2.dsp_ratio=(0.5)
    self.walkL2.step_fb_ratio=(0.280000001192)

    self.walkL2.x_move_amplitude=(0.019999999553)
    self.walkL2.y_move_amplitude=(0.00)

    self.walkL2.z_move_amplitude=(0.0500000007451)
    self.walkL2.angle_move_amplitude=(-
    0.0623598790169)
    self.walkL2.move_aim_on=(True)
    self.walkL2.balance_enable=(True)

    self.walkL2.balance_hip_roll_gain=(0.34999999404)

    self.walkL2.balance_knee_gain=(0.300000011921)

    self.walkL2.balance_ankle_roll_gain=(0.6999999880
    79)

    self.walkL2.balance_ankle_pitch_gain=(0.899999976
    158)

    self.walkL2.y_swap_amplitude=(0.019999999553)

    self.walkL2.z_swap_amplitude=(0.0130000002682)
    self.walkL2.arm_swing_gain=(0.20000000298)
    self.walkL2.pelvis_offset=(0.00872664619237)

    self.walkL2.hip_pitch_offset=(0.157079637051)
    self.walkL2.p_gain=(0)
    self.walkL2.i_gain=(0)
    self.walkL2.d_gain=(0)

    self.walkR1 = WalkingParam()
    self.walkR1.init_x_offset=(-0.019999999553)
    self.walkR1.init_y_offset=(0.0450000017881)
    self.walkR1.init_z_offset=(0.0250000003725)

    self.walkR1.init_roll_offset=(0.069813169539)
    self.walkR1.init_pitch_offset=(-
    0.0139626339078)
    self.walkR1.init_yaw_offset=(0.0)
    self.walkR1.period_time=(1.29999995232)
    self.walkR1.dsp_ratio=(0.5)
    self.walkR1.step_fb_ratio=(0.280000001192)

    self.walkR1.x_move_amplitude=(0.019999999553)
    self.walkR1.y_move_amplitude=(0.00)

    self.walkR1.z_move_amplitude=(0.0500000007451)

    self.walkR1.angle_move_amplitude=(0.0124532923847
    )
    self.walkR1.move_aim_on=(True)
    self.walkR1.balance_enable=(True)

    self.walkR1.balance_hip_roll_gain=(0.34999999404)

    self.walkR1.balance_knee_gain=(0.300000011921)

    self.walkR1.balance_ankle_roll_gain=(0.6999999880
    79)

    self.walkR1.balance_ankle_pitch_gain=(0.899999976
    158)

    self.walkR1.y_swap_amplitude=(0.019999999553)

    self.walkR1.z_swap_amplitude=(0.0130000002682)
    self.walkR1.arm_swing_gain=(0.20000000298)
    self.walkR1.pelvis_offset=(0.00872664619237)

    self.walkR1.hip_pitch_offset=(0.157079637051)
    self.walkR1.p_gain=(0)
    self.walkR1.i_gain=(0)
    self.walkR1.d_gain=(0)

    self.walkR2 = WalkingParam()
    self.walkR2.init_x_offset=(-0.019999999553)
    self.walkR2.init_y_offset=(0.0450000017881)
    self.walkR2.init_z_offset=(0.0250000003725)

    self.walkR2.init_roll_offset=(0.069813169539)
    self.walkR2.init_pitch_offset=(-
    0.0139626339078)
    self.walkR2.init_yaw_offset=(0.0)
    self.walkR2.period_time=(1.29999995232)
    self.walkR2.dsp_ratio=(0.5)
    self.walkR2.step_fb_ratio=(0.280000001192)

    self.walkR2.x_move_amplitude=(0.019999999553)
    self.walkR2.y_move_amplitude=(0.00)

    self.walkR2.z_move_amplitude=(0.0500000007451)

    self.walkR2.angle_move_amplitude=(0.0523598790169
    )

    self.walkR2.move_aim_on=(True)
    self.walkR2.balance_enable=(True)

    self.walkR2.balance_hip_roll_gain=(0.34999999404)

    self.walkR2.balance_knee_gain=(0.300000011921)

    self.walkR2.balance_ankle_roll_gain=(0.6999999880
    79)

    self.walkR2.balance_ankle_pitch_gain=(0.899999976
    158)

    self.walkR2.y_swap_amplitude=(0.019999999553)

    self.walkR2.z_swap_amplitude=(0.0130000002682)
    self.walkR2.arm_swing_gain=(0.20000000298)
    self.walkR2.pelvis_offset=(0.00872664619237)

    self.walkR2.hip_pitch_offset=(0.157079637051)
    self.walkR2.p_gain=(0)
    self.walkR2.i_gain=(0)
    self.walkR2.d_gain=(0)

    self.walkUP = WalkingParam()
    self.walkUP.init_x_offset=(-0.019999999553)
    self.walkUP.init_y_offset=(0.0450000017881)
    self.walkUP.init_z_offset=(0.0250000003725)

    self.walkUP.init_roll_offset=(0.069813169539)
    self.walkUP.init_pitch_offset=(-
    0.0139626339078)

    self.walkUP.init_yaw_offset=(0.0)
    self.walkUP.period_time=(1.29999995232)
    self.walkUP.dsp_ratio=(0.5)
    self.walkUP.step_fb_ratio=(0.280000001192)

    self.walkUP.x_move_amplitude=(0.00999999977648)
    self.walkUP.y_move_amplitude=(0.00)

    self.walkUP.z_move_amplitude=(0.0500000007451)

    self.walkUP.angle_move_amplitude=(0.05026646)
    self.walkUP.move_aim_on=(True)
    self.walkUP.balance_enable=(True)

    self.walkUP.balance_hip_roll_gain=(0.34999999404)

    self.walkUP.balance_knee_gain=(0.300000011921)

    self.walkUP.balance_ankle_roll_gain=(0.6999999880
    79)

    self.walkUP.balance_ankle_pitch_gain=(0.899999976
    158)

    self.walkUP.y_swap_amplitude=(0.019999999553)

    self.walkUP.z_swap_amplitude=(0.0130000002682)
    self.walkUP.arm_swing_gain=(0.20000000298)
    self.walkUP.pelvis_offset=(0.00872664619237)

    self.walkUP.hip_pitch_offset=(0.157079637051)
    self.walkUP.p_gain=(0)

    self.walkUP.i_gain=(0)
    self.walkUP.d_gain=(0)

    self.walkDW = WalkingParam()
    self.walkDW.init_x_offset=(-0.019999999553)
    self.walkDW.init_y_offset=(0.0450000017881)
    self.walkDW.init_z_offset=(0.0250000003725)

    self.walkDW.init_roll_offset=(0.069813169539)

    self.walkDW.init_pitch_offset=(0.0174532923847)
    self.walkDW.init_yaw_offset=(0.0)
    self.walkDW.period_time=(1.29999995232)
    self.walkDW.dsp_ratio=(0.5)
    self.walkDW.step_fb_ratio=(0.280000001192)

    self.walkDW.x_move_amplitude=(0.0130000002682)
    self.walkDW.y_move_amplitude=(0.00)

    self.walkDW.z_move_amplitude=(0.0500000007451)
    self.walkDW.angle_move_amplitude=(-
    0.0972664600611)
    self.walkDW.move_aim_on=(True)
    self.walkDW.balance_enable=(True)

    self.walkDW.balance_hip_roll_gain=(0.34999999404)

    self.walkDW.balance_knee_gain=(0.300000011921)

    self.walkDW.balance_ankle_roll_gain=(0.6999999880
    79)

    self.walkDW.balance_ankle_pitch_gain=(0.899999976
    158)

    self.walkDW.y_swap_amplitude=(0.019999999553)

    self.walkDW.z_swap_amplitude=(0.0130000002682)
    self.walkDW.arm_swing_gain=(0.20000000298)
    self.walkDW.pelvis_offset=(0.00872664619237)

    self.walkDW.hip_pitch_offset=(0.157079637051)
    self.walkDW.p_gain=(0)
    self.walkDW.i_gain=(0)
    self.walkDW.d_gain=(0)

    self.walkB = WalkingParam()
    self.walkB.init_x_offset=(-0.019999999553)
    self.walkB.init_y_offset=(0.0450000017881)
    self.walkB.init_z_offset=(0.0250000003725)
    self.walkB.init_roll_offset=(0.069813169539)

    self.walkB.init_pitch_offset=(0.0174532923847)
    self.walkB.init_yaw_offset=(0.0)
    self.walkB.period_time=(1.29999995232)
    self.walkB.dsp_ratio=(0.5)
    self.walkB.step_fb_ratio=(0.280000001192)

    self.walkB.x_move_amplitude=(0.00499999988824)
    self.walkB.y_move_amplitude=(0.00)

    self.walkB.z_move_amplitude=(0.0500000007451)

    self.walkB.angle_move_amplitude=(-
    0.0572664600611)
    self.walkB.move_aim_on=(True)
    self.walkB.balance_enable=(True)

    self.walkB.balance_hip_roll_gain=(0.34999999404)

    self.walkB.balance_knee_gain=(0.300000011921)

    self.walkB.balance_ankle_roll_gain=(0.69999998807
    9)

    self.walkB.balance_ankle_pitch_gain=(0.8999999761
    58)
    self.walkB.y_swap_amplitude=(0.019999999553)

    self.walkB.z_swap_amplitude=(0.0130000002682)
    self.walkB.arm_swing_gain=(0.20000000298)
    self.walkB.pelvis_offset=(0.00872664619237)
    self.walkB.hip_pitch_offset=(0.157079637051)
    self.walkB.p_gain=(0)
    self.walkB.i_gain=(0)
    self.walkB.d_gain=(0)

    self.walkC = WalkingParam()
    self.walkC.init_x_offset=(-0.019999999553)
    self.walkC.init_y_offset=(0.0450000017881)
    self.walkC.init_z_offset=(0.0250000003725)
    self.walkC.init_roll_offset=(0.069813169539)

    self.walkC.init_pitch_offset=(0.0174532923847)
    self.walkC.init_yaw_offset=(0.0)

    self.walkC.period_time=(1.29999995232)
    self.walkC.dsp_ratio=(0.5)
    self.walkC.step_fb_ratio=(0.280000001192)

    self.walkC.x_move_amplitude=(0.00599999988824)
    self.walkC.y_move_amplitude=(0.00)

    self.walkC.z_move_amplitude=(0.0500000007451)

    self.walkC.angle_move_amplitude=(0.0872664600611)
    self.walkC.move_aim_on=(True)
    self.walkC.balance_enable=(True)

    self.walkC.balance_hip_roll_gain=(0.34999999404)

    self.walkC.balance_knee_gain=(0.300000011921)

    self.walkC.balance_ankle_roll_gain=(0.69999998807
    9)

    self.walkC.balance_ankle_pitch_gain=(0.8999999761
    58)
    self.walkC.y_swap_amplitude=(0.019999999553)

    self.walkC.z_swap_amplitude=(0.0130000002682)
    self.walkC.arm_swing_gain=(0.20000000298)
    self.walkC.pelvis_offset=(0.00872664619237)
    self.walkC.hip_pitch_offset=(0.157079637051)
    self.walkC.p_gain=(0)
    self.walkC.i_gain=(0)
    self.walkC.d_gain=(0)

    self.walkUPLeft = WalkingParam()
    self.walkUPLeft.init_x_offset=(-
    0.019999999553)

    self.walkUPLeft.init_y_offset=(0.0450000017881)

    self.walkUPLeft.init_z_offset=(0.0250000003725)

    self.walkUPLeft.init_roll_offset=(0.069813169539)

    self.walkUPLeft.init_pitch_offset=(0.017453292384
    7)
    self.walkUPLeft.init_yaw_offset=(0.0)
    self.walkUPLeft.period_time=(1.29999995232)
    self.walkUPLeft.dsp_ratio=(0.5)

    self.walkUPLeft.step_fb_ratio=(0.280000001192)

    self.walkUPLeft.x_move_amplitude=(0.0099999997764
    8)
    self.walkUPLeft.y_move_amplitude=(0.00)

    self.walkUPLeft.z_move_amplitude=(0.0500000007451
    )
    self.walkUPLeft.angle_move_amplitude=(-
    0.0174532923847)
    self.walkUPLeft.move_aim_on=(True)
    self.walkUPLeft.balance_enable=(True)

    self.walkUPLeft.balance_hip_roll_gain=(0.34999999
    404)

    self.walkUPLeft.balance_knee_gain=(0.300000011921
    )

    self.walkUPLeft.balance_ankle_roll_gain=(0.699999
    988079)

    self.walkUPLeft.balance_ankle_pitch_gain=(0.89999
    9976158)

    self.walkUPLeft.y_swap_amplitude=(0.019999999553)

    self.walkUPLeft.z_swap_amplitude=(0.0130000002682
    )

    self.walkUPLeft.arm_swing_gain=(0.20000000298)

    self.walkUPLeft.pelvis_offset=(0.00872664619237)

    self.walkUPLeft.hip_pitch_offset=(0.157079637051)
    self.walkUPLeft.p_gain=(0)
    self.walkUPLeft.i_gain=(0)
    self.walkUPLeft.d_gain=(0)

    self.walkR3 = WalkingParam()
    self.walkR3.init_x_offset=(-0.019999999553)
    self.walkR3.init_y_offset=(0.0450000017881)
    self.walkR3.init_z_offset=(0.0250000003725)

    self.walkR3.init_roll_offset=(0.069813169539)

    self.walkR3.init_pitch_offset=(0.0174532923847)

    self.walkR3.init_yaw_offset=(0.0)
    self.walkR3.period_time=(1.29999995232)
    self.walkR3.dsp_ratio=(0.5)
    self.walkR3.step_fb_ratio=(0.280000001192)

    self.walkR3.x_move_amplitude=(0.019999999553)
    self.walkR3.y_move_amplitude=(0.00)

    self.walkR3.z_move_amplitude=(0.0500000007451)

    self.walkR3.angle_move_amplitude=(0.0723598790169
    )
    self.walkR3.move_aim_on=(True)
    self.walkR3.balance_enable=(True)

    self.walkR3.balance_hip_roll_gain=(0.34999999404)

    self.walkR3.balance_knee_gain=(0.300000011921)

    self.walkR3.balance_ankle_roll_gain=(0.6999999880
    79)

    self.walkR3.balance_ankle_pitch_gain=(0.899999976
    158)

    self.walkR3.y_swap_amplitude=(0.019999999553)

    self.walkR3.z_swap_amplitude=(0.0130000002682)
    self.walkR3.arm_swing_gain=(0.20000000298)
    self.walkR3.pelvis_offset=(0.00872664619237)

    self.walkR3.hip_pitch_offset=(0.157079637051)

    self.walkR3.p_gain=(0)
    self.walkR3.i_gain=(0)
    self.walkR3.d_gain=(0)

    self.walkL3 = WalkingParam()
    self.walkL3.init_x_offset=(-0.019999999553)
    self.walkL3.init_y_offset=(0.0450000017881)
    self.walkL3.init_z_offset=(0.0250000003725)

    self.walkL3.init_roll_offset=(0.069813169539)
    self.walkL3.init_pitch_offset=(-
    0.0139626339078)
    self.walkL3.init_yaw_offset=(0.0)
    self.walkL3.period_time=(1.29999995232)
    self.walkL3.dsp_ratio=(0.5)
    self.walkL3.step_fb_ratio=(0.280000001192)

    self.walkL3.x_move_amplitude=(0.019999999553)
    self.walkL3.y_move_amplitude=(0.00)

    self.walkL3.z_move_amplitude=(0.0500000007451)
    self.walkL3.angle_move_amplitude=(-
    0.0923598790169)
    self.walkL3.move_aim_on=(True)
    self.walkL3.balance_enable=(True)

    self.walkL3.balance_hip_roll_gain=(0.34999999404)

    self.walkL3.balance_knee_gain=(0.300000011921)

    self.walkL3.balance_ankle_roll_gain=(0.6999999880
    79)

    self.walkL3.balance_ankle_pitch_gain=(0.899999976
    158)

    self.walkL3.y_swap_amplitude=(0.019999999553)

    self.walkL3.z_swap_amplitude=(0.0130000002682)
    self.walkL3.arm_swing_gain=(0.20000000298)
    self.walkL3.pelvis_offset=(0.00872664619237)

    self.walkL3.hip_pitch_offset=(0.157079637051)
    self.walkL3.p_gain=(0)
    self.walkL3.i_gain=(0)
    self.walkL3.d_gain=(0)

    #Dynamixel Joint Action
    self.gerakan = JointState() #Angkat Tangan
    self.gerakan.name = []
    self.gerakan.position = []
    self.gerakan.velocity = []
    self.gerakan.effort = []

    def status(self,data):
        self.msg = data.status_msg
        self.modul = data.module_name

        if(self.msg=="Stop walking"):
            self.lock_stop_jalan+=1
        if(self.lock_stop_jalan > 1):
            self.lock_stop_jalan = 1

        if(self.msg=="Action_Finish"):
            self.lock_stop_gerak+=1
        if(self.lock_stop_gerak > 1):
            self.lock_stop_gerak = 1

    def counter_jalan1(self,modeWalk1,t_in1,t_walk1):
        self.pubEnCtrl.publish("walking_module")
        time.sleep(0.1)
        self.pubWalkParam.publish(modeWalk1)
        time.sleep(t_in1)
        self.pubCommand.publish("start")
        time.sleep(t_walk1)
        self.pubCommand.publish("stop")
        self.lock_stop_jalan = 0
        self.lock_stop_gerak = 0

    def counter_gerak(self,t_inAct,page):
        time.sleep(t_inAct)
        self.pubEnCtrl.publish("action_module")
        time.sleep(0.3)
        self.pubActPage.publish(page)
        self.lock_stop_jalan = 0
        self.lock_stop_gerak = 0

    #Subs Flag from Anna
    def slave_back(self,data):
        self.gerak = data.gerak
        self.jalan = data.jalan

        if(self.gerak == 1):
            self.sg = 1
        else:
            self.sg = 0

        if(self.jalan == 1):
            self.sw = 1
        else:
            self.sw = 0

    #Subs Button
    def button_callback(self,data):
        self.button_status = data.data
        if(self.button_status == 1):
            self.btn = 1

    #Subs Bluetooth
    def bluetooth_callback(self,data):
        self.bt_status = data.data
        if(self.bt_status == 1):
            self.blt = 1

    def run(self):

        #Robot Stand Up

        if(self.a == 0):
            time.sleep(2)

            self.pubEnCtrl.publish("walking_module")

            self.a = 1

        elif(self.btn == 1):

        #ZONA MULAI

        #Counter 1
            if(self.blt == 1 and self.a == 1):
                print("Bluetooth ON")
                print("START")
                self.counter_gerak(2.5,10)
                print("GERAK (ZONA MULAI)")
                self.a = 2

            #ZONA A

            #Counter 2
            elif(self.lock_stop_gerak == 1 and self.a == 2):
                self.counter_jalan1(self.walkF,1.5,2.9)
                print("JALAN 1 (ZONA A)")
                self.a = 3

            #Counter 3
            elif(self.lock_stop_jalan == 1 and self.a == 3):
                self.counter_gerak(2,10)
                print("GERAK 1 (ZONA A)")
                self.a = 4

            #Counter 4
            elif(self.lock_stop_gerak == 1 and self.a == 4):
                self.counter_jalan1(self.walkF,1.5,2.8)
                print("JALAN 2 (ZONA A)")
                self.a = 5

            #Counter 5
            elif(self.lock_stop_jalan == 1 and self.a == 5):
                self.counter_gerak(2,10)
                print("GERAK 2 (ZONA A)")
                self.a = 6

            #ZONA B

            #Counter 6
            elif(self.lock_stop_gerak == 1 and self.a == 6):
                self.counter_jalan1(self.walkR1,1.5,1.7)
                print("JALAN 1 (ZONA B)")
                self.a = 7
            #Counter 7
            elif(self.lock_stop_jalan == 1 and self.a == 7):
                self.counter_gerak(2,10)
                print("GERAK 1 (ZONA B)")
                self.a = 8

if __name__ == '__main__':#untuk terminate
    rospy.init_node('robot_one_1')
    mod = Model()
try:
    while not rospy.is_shutdown():
        mod.run()
    except rospy.ROSInterruptException():
        pass