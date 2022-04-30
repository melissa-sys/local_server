#coding=utf-8
import os
import json
import pyautogui
import time
from time import sleep
from flask_apscheduler import APScheduler
import apscheduler.schedulers.background

import flask
from flask import Flask
from flask import Response
from flask import redirect
from flask import url_for
from flask import render_template

# import cv2


import requests


global firstRequest
firstRequest = False
# Inicialización de variables
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

global prueba
#prueba = 87 #TODO quitar esto por una variable que se actualice en la primera peticion

# Funciones del RPA

def abrirterminal():
    """
    Función para abrir la terminal de linux y se ejecute
    """
    pyautogui.click(x=100, y=0, clicks=1, button='left')
    pyautogui.hotkey('Ctrl', 'Alt', 't')

def escribirterminal(comando):
    """
    Función para abrir la terminal de linux y se ejecute
    """
    pyautogui.typewrite(comando, interval=0)
    pyautogui.hotkey('ENTER')

def borrar_registros():
    """ Borra en el txt los valores de las articulaciones """
    wave1 = {str("right")+'_s0': 0, str("right")+'_s1': 0, str("right")+'_e0': 0, str("right")+'_e1': 0,
             str("right")+'_w0': 0, str("right")+'_w1': 0, str("right")+'_w2': 0}
    wave2 = {str("left")+'_s0': 0, str("left")+'_s1': 0, str("left")+'_e0': 0, str("left")+'_e1': 0,
             str("left")+'_w0': 0, str("left")+'_w1': 0, str("left")+'_w2': 0}
    with open("movimientosright.txt", 'w'):
        pass
    text_file = open("movimientosright.txt", "w")
    text_file.write(str(wave1))
    text_file.close()
    with open("movimientosleft.txt", 'w'):
        pass
    text_file = open("movimientosleft.txt", "w")
    text_file.write(str(wave2))
    text_file.close()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def json_example():
    global prueba
    global firstRequest
    url = 'http://3.93.220.15:8080/api/message/'

    # Me devuelve el Response del request (objeto)
    var_get = requests.get(url)

    if 'json' in var_get.headers.get('Content-Type'):
        js_string = var_get.json()  # Convierto en JSON mi response. Viene en forma de list

    else:
        print('Response content is not in JSON format.')
        js_string = 'spam'

    # print(js_string)
    
    id_message = js_string[-1]['id']
    print(id_message)

    if ( firstRequest == False ):
        firstRequest = True
        prueba = id_message
        print(prueba)
        a = id_message
    else:
        a = id_message


    if (a != prueba):
        prueba = a
        print("not same number")
        last_json = js_string[-1]['message']
        replace_simple_quotation = str(last_json).replace("'", '"')
        replace_none_values = str(
            replace_simple_quotation).replace(" None", '""')
        replace_true_value = str(
            replace_none_values).replace(" True", '"True"')

        # Convierto a JSON mi str
        last_json = json.loads(replace_true_value)
        print(last_json)

        print(last_json['accion'])
        # print(last_json.get('accion'))
        # print(id_message)
        if (last_json['confirmacion'] == 'True'):
            with open('datos.txt', 'w'):
                pass
            text_file = open("datos.txt", "w")
            text_file.write(str(last_json))
            text_file.close()
            if(last_json['accion'] == 'tomar'):
                escribirterminal("python tomarfoto.py")
                print("escribí 'python tomarfoto.py' en la terminal ")
                time.sleep(1)
                escribirterminal("python mov_arms.py")
                print("escribí 'python mov_arms.py' en la terminal ")
            if(last_json['accion'] == "mover"):
                escribirterminal("python pose.py")
                print("escribí 'python pose.py' en la terminal ")
            if(last_json['accion'] == "guardar"):
                print("guardé los valores en txts")
                os.rename("movimientosleft.txt", "Programas/" +
                            str(datos['nombre_programa'])+"l.txt")
                os.rename("movimientosright.txt", "Programas/" +
                            str(datos['nombre_programa'])+"r.txt")
            if(last_json['accion'] == "ejecutar"):  # pendiente
                escribirterminal("python programas_guardadas.py")
                print("escribí 'python programas_guardadas.py' en la terminal ")
            if(last_json['accion'] == "posicionar"):
                escribirterminal("python TCI.py")
                print("escribí 'python TCI.py' en la terminal ")
                time.sleep(3) 
            if (last_json["accion"] == "iniciar"):
                abrirterminal()
                print('Se ejecuta todo lo respectivo a INICIAR')
                escribirterminal("cd ros_ws")
                escribirterminal(". baxter.sh")
                escribirterminal("rosrun baxter_tools enable_robot.py -e")
                time.sleep(10)
                escribirterminal("python obtener_pos.py")
            if (last_json["accion"] == "set"):
                print('Se ejecuta todo lo respectivo a SET')
                escribirterminal("rosrun baxter_tools tuck_arms.py -u")
                borrar_registros()
                time.sleep(5)
                escribirterminal("python obtener_pos.py")
            if(last_json["accion"] == "apagar"):
                print('Se ejecuta todo lo respectivo a APAGAR')
                escribirterminal("rosrun baxter_tools tuck_arms.py -t")
                escribirterminal("exit")
                escribirterminal("exit")
                borrar_registros()
            time.sleep(10)
            datos = open("pos_actual.txt", "r")
            time.sleep(5)
            #escribirterminal('scp -i keypair.pem local_server/datos.txt ubuntu@ec2-3-93-220-15.compute-1.amazonaws.com:~/baxter-assistant1.0/ba_v1/chat/static')
            #time.sleep(10)
            #valores = eval(datos.read())
            return (datos.read())

        else:
            print('Existe un error!')
            return (datos.read()) #Retornaba json con los valores de cada articulación del brazo        

    else:
        print("same number")
        prueba = prueba
        js_string = {'no new data'}
        print(js_string)
        with app.test_request_context():
            print(redirect(url_for('video_example')))
            return redirect(url_for('video_example'))

    return str(js_string)

@app.route("/video", methods=['GET','POST'])
def video_example():
    print('iniciando video')
    abrirterminal()
    escribirterminal("cd ros_ws")
    escribirterminal(". baxter.sh")
    escribirterminal("rosrun baxter_tools enable_robot.py -e")
    time.sleep(10)
    escribirterminal("cd local_server")
    escribirterminal("python baxter_camera.py")
    return True

@app.route("/video_kinesis", methods=['GET', 'POST'])
def video():
   return render_template('video.html')
   
scheduler = APScheduler()
scheduler.add_job(id='Scheduled task', func=json_example,
                  trigger='interval', seconds=5, max_instances= 2)

scheduler.start()

if __name__ == '__main__':
    # run app in debug mode on port 5000
    while True:
        app.run(debug=True, use_reloader=False, port=5001)
        sleep(1)
