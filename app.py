import os
import json
import pyautogui
import time
#import apscheduler

from flask import Flask


import requests

# Inicialziación de variables
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

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


app = Flask(__name__)


@app.route('/', methods=['GET'])
def json_example():
    # return 'JSON Object Example'
    url = 'http://127.0.0.1:8000/api/message/'  # LOCAL
    # url = 'https://baxterassistant2.pythonanywhere.com/api/message/' CERT
    # url = 'https://baxterassistant.pythonanywhere.com/api/message/' PROD
    var_get = requests.get(url)  # Me devuelve el Response del request (objeto)

    if 'json' in var_get.headers.get('Content-Type'):
        js_string = var_get.json()  # Convierto en JSON mi response. Viene en forma de list

    else:
        print('Response content is not in JSON format.')
        js_string = 'spam'

    id_message = js_string[-1]['id']
    last_json = js_string[-1]['message']
    replace_simple_quotation = str(last_json).replace("'", '"')
    replace_none_values = str(replace_simple_quotation).replace(" None", '""')
    replace_true_value = str(replace_none_values).replace(" True", '"True"')

    # Convierto a JSON mi str
    last_json = json.loads(replace_true_value)
    print(last_json)

    print(last_json['accion'])
    # print(last_json.get('accion'))
    # print(id_message)
    if (last_json['confirmacion'] == 'True'):
        if(last_json['accion'] == 'tomar'):
            # escribirterminal("python tomarfoto.py")
            print("escribí 'python tomarfoto.py' en la terminal ")
            # time.sleep(1)
            # escribirterminal("python mov_arms.py")
            print("escribí 'python mov_arms.py' en la terminal ")
        if(last_json['accion'] == "mover"):
            #escribirterminal("python pose.py")
            print("escribí 'python pose.py' en la terminal ")
        if(last_json['accion'] == "guardar"):
            print("guardé los valores en txts")
            # os.rename("movimientosleft.txt", "Programas/" +
            #             str(datos['nombre_programa'])+"l.txt")
            # os.rename("movimientosright.txt", "Programas/" +
            #             str(datos['nombre_programa'])+"r.txt")
        if(last_json['accion'] == "ejecutar"):  # pendiente
            # escribirterminal("python programas_guardadas.py")
            print("escribí 'python programas_guardadas.py' en la terminal ")
        if(last_json['accion'] == "posicionar"):
            # escribirterminal("python TCI.py")
            print("escribí 'python TCI.py' en la terminal ")
            # time.sleep(3)
            # datos = open("pos_actual.txt", "r")
            # valores = eval(datos.read())
            # return(valores['estado'])
        # time.sleep(10)
        # escribirterminal("python obtener_pos.py")
        # datos = open("pos_actual.txt", "r")
        # valores = eval(datos.read())
        # return(valores)

        if (last_json["accion"] == "iniciar"):
            # abrirterminal()
            print('Se ejecuta todo lo respectivo a INICIAR')
            # escribirterminal("cd ros_ws")
            # escribirterminal(". baxter.sh")
            # escribirterminal("rosrun baxter_tools enable_robot.py -e")
            # time.sleep(10)
            # escribirterminal("python obtener_pos.py")
        if (last_json["accion"] == "set"):
            print('Se ejecuta todo lo respectivo a SET')
            # escribirterminal("rosrun baxter_tools tuck_arms.py -u")
            # borrar_registros()
            # time.sleep(5)
            # escribirterminal("python obtener_pos.py")
        if(last_json["accion"] == "apagar"):
            print('Se ejecuta todo lo respectivo a APAGAR')
            # escribirterminal("rosrun baxter_tools tuck_arms.py -t")
            # escribirterminal("exit")
            # escribirterminal("exit")
            # borrar_registros()
        # print(payload["accion"])
        # datos = open("pos_actual.txt", "r")
        # #valores=eval(datos.read())
        # return (datos.read())

    else:
        # escribirterminal("python obtener_pos.py")
        print("escribí 'python obtener_pos.py' en la terminal ")
        # datos = open("pos_actual.txt", "r")
        # return (datos.read()) #Retornaba json con los valores de cada articulación del brazo

    return str(js_string)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
