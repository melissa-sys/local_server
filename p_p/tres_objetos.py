import rospy 

from positions import izq,der 

import baxter_interface 

from baxter_interface import CHECK_VERSION 


def principal():

	rospy.init_node('limpiar') 
	
	print("Obteniendo el estado del robot... ") 
	baxter_interface.RobotEnable(CHECK_VERSION).state().enabled 
	print("Habilitando motores... ") 
	baxter_interface.RobotEnable(CHECK_VERSION).enable() 

	brazo_izquierdo = baxter_interface.Limb('left') 
	brazo_izquierdo.set_joint_position_speed(1.0) 

	brazo_derecho = baxter_interface.Limb('right')
	brazo_derecho.set_joint_position_speed(1.0)

	brazo_derecho.move_to_joint_positions(der[0],10.0, 0.09) 
	brazo_izquierdo.move_to_joint_positions(izq[0],10.0, 0.09)

	cabeza = baxter_interface.Head() 

	cabeza.set_pan(0.7)
	grip_izq = baxter_interface.Gripper('left')  
	grip_izq.calibrate() 

	cabeza.set_pan(-0.8)
	grip_der = baxter_interface.Gripper('right')
	grip_der.calibrate()



#beginning of movements

	#object 1

	cabeza.set_pan(0.2)

	brazo_izquierdo.move_to_joint_positions(izq[1],10.0,0.1)
	brazo_izquierdo.move_to_joint_positions(izq[2],10.0,0.050)
	brazo_izquierdo.move_to_joint_positions(izq[3],10.0,0.008)
	grip_izq.close() 
	rospy.sleep(1) 
	brazo_izquierdo.move_to_joint_positions(izq[4],10.0,0.1)
	
	cabeza.set_pan(-0.7)

	brazo_derecho.move_to_joint_positions(der[1],10.0,0.008)
	grip_der.close() 
	rospy.sleep(1) 
	brazo_derecho.move_to_joint_positions(der[2],10.0,0.1)

	cabeza.set_pan(0.2)


	brazo_derecho.move_to_joint_positions(der[3],10.0,0.1)
	brazo_derecho.move_to_joint_positions(der[4],10.0,0.1)
	brazo_derecho.move_to_joint_positions(der[5],10.0,0.1)
	brazo_derecho.move_to_joint_positions(der[6],10.0,0.1)
	brazo_derecho.move_to_joint_positions(der[7],10.0,0.1)
	brazo_derecho.move_to_joint_positions(der[8],10.0,0.1)
	brazo_derecho.move_to_joint_positions(der[9],10.0,0.1)

	brazo_izquierdo.move_to_joint_positions(izq[3],10.0,0.01)
	grip_izq.open() 
	rospy.sleep(1)

	#object 2
	brazo_izquierdo.move_to_joint_positions(izq[2],10.0,0.1)
	brazo_izquierdo.move_to_joint_positions(izq[5],10.0,0.1)

	cabeza.set_pan(-0.5)

	brazo_izquierdo.move_to_joint_positions(izq[6],10.0,0.050)
	brazo_izquierdo.move_to_joint_positions(izq[7],10.0,0.008)
	grip_izq.close() 
	rospy.sleep(1) 
	brazo_izquierdo.move_to_joint_positions(izq[8],10.0,0.01)

	brazo_derecho.move_to_joint_positions(der[10],10.0,0.1)	
	brazo_derecho.move_to_joint_positions(der[11],10.0,0.1)		
	brazo_derecho.move_to_joint_positions(der[12],10.0,0.1)	
	brazo_derecho.move_to_joint_positions(der[13],10.0,0.1)	

	brazo_izquierdo.move_to_joint_positions(izq[7],10.0,0.008)
	grip_izq.open() 
	rospy.sleep(1)

	#object 3

	brazo_izquierdo.move_to_joint_positions(izq[8],10.0,0.1)

	cabeza.set_pan(0)

	brazo_izquierdo.move_to_joint_positions(izq[9],10.0,0.050)
	brazo_izquierdo.move_to_joint_positions(izq[10],10.0,0.01)
	brazo_izquierdo.move_to_joint_positions(izq[11],10.0,0.008)
	grip_izq.command_position(40) 
	rospy.sleep(1)
	brazo_izquierdo.move_to_joint_positions(izq[12],10.0,0.1)
	brazo_izquierdo.move_to_joint_positions(izq[13],10.0,0.1)

	cabeza.set_pan(0.45)

	brazo_izquierdo.move_to_joint_positions(izq[14],10.0,0.1)
	grip_izq.open() 
	rospy.sleep(1)
	brazo_izquierdo.move_to_joint_positions(izq[0],10.0, 0.09)

	cabeza.set_pan(0)

	brazo_derecho.move_to_joint_positions(der[14],10.0,0.1)	
	brazo_derecho.move_to_joint_positions(der[15],10.0,0.1)		
	brazo_derecho.move_to_joint_positions(der[16],10.0,0.1)	
	brazo_derecho.move_to_joint_positions(der[17],10.0,0.1)
	brazo_derecho.move_to_joint_positions(der[18],10.0,0.1)
	brazo_derecho.move_to_joint_positions(der[15],10.0,0.1)	
	brazo_derecho.move_to_joint_positions(der[14],10.0,0.1)	
	brazo_derecho.move_to_joint_positions(der[19],10.0,0.1)	
	brazo_derecho.move_to_joint_positions(der[1],10.0,0.01)
	grip_der.open() 
	rospy.sleep(1) 
	brazo_derecho.move_to_joint_positions(der[0],10.0,0.1)

	print("FIN DEL PROGRAMA") 
	print("Deshabilitando Motores... ") 
	baxter_interface.RobotEnable(CHECK_VERSION).disable() 



if __name__ == '__main__': 
	principal()
