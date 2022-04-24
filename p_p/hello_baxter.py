import rospy 

import baxter_interface 

from baxter_interface import CHECK_VERSION 

rospy.init_node('Hello')

print("Obteniendo el estado del robot... ") 
baxter_interface.RobotEnable(CHECK_VERSION).state().enabled 
print("Habilitando... ") 
baxter_interface.RobotEnable(CHECK_VERSION).enable() 

limb = baxter_interface.Limb('right') 
limb2 = baxter_interface.Limb('left')

angles = limb.joint_angles()

print (angles )

angles['right_s0']=0.0 
angles['right_s1']=0.0 
angles['right_e0']=0.0 
angles['right_e1']=0.0 
angles['right_w0']=0.0 
angles['right_w1']=0.0 
angles['right_w2']=0.0 

print (angles )

limb.move_to_joint_positions(angles) 

pos1 = {'right_s0': -0.459, 'right_s1': -0.202, 'right_e0': 1.807, 'right_e1': 1.714, 'right_w0': -0.906, 'right_w1': -1.545, 'right_w2': -0.276} 

pos2 = {'right_s0': -0.395, 'right_s1': -0.202, 'right_e0': 1.831, 'right_e1': 1.981, 'right_w0': -1.979, 'right_w1': -1.100, 'right_w2': -0.448} 

pos3 = {'left_w0': 0, 'left_w1': 0, 'left_w2': 0, 'left_e0': 0, 'left_e1': 0, 'left_s0': 0, 'left_s1': 0}

for _move in range(2): 
	limb.move_to_joint_positions(pos1) 
	limb.move_to_joint_positions(pos2) 
	limb2.move_to_joint_positions(pos3) 

print ("fin del programa")

print("Obteniendo el estado del robot... ") 
baxter_interface.RobotEnable(CHECK_VERSION).state().enabled
print("Deshabilitando... ") 
baxter_interface.RobotEnable(CHECK_VERSION).disable() 

