#coding=utf-8
# General module imports
import rospy
import cv2 as cv
import cv_bridge

from baxter_interface.camera import (
    CameraController,  # defino el tipo de mensaje
)
from sensor_msgs.msg import (
    Image,  # este es el mensaje
)

# Le pasamos el nombre de la cámara, y valor de la resolución como tupla


def open_camera(camera, resolution):
    if not any((resolution[0] == r[0] and resolution[1] == r[1]) for r in CameraController.MODES):
        rospy.logerr('Invalid resolution provided.')
    # clase que me permite crear objeto sin tener que usar consola
    cam = CameraController(camera)
    cam.resolution = resolution  # se debe setear la resolucion
    cam.open()

# Cerramos la cámara


def close_camera(camera):
    cam = CameraController(camera)
    cam.close()

# Aquí se cambia el formato de la imagen a OpenCV


def limb_cam_show_image_callback(ros_img):
    cv_image = cv_bridge.CvBridge().imgmsg_to_cv2(
        ros_img, desired_encoding="passthrough")
    print(type(cv_image))
    cv.imshow('Image', cv_image)
    # como tengo muchas imágenes, que son el video, lo ejecuto cada 1ms
    cv.waitKey(1)


if __name__ == '__main__':
    rospy.init_node('Camera_Subscriber', anonymous=True)
    rospy.Subscriber('/cameras/head_camera/image',
                     Image, limb_cam_show_image_callback)  # nombre_topic(probamos brazo izq), mensaje_importadoa_arriba, funcion_callback: retorna las imágenes a cierta frecuencia. Es como un servidor.
    rospy.spin()  # delay
    cv.destroyAllWindows()
