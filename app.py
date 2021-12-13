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
    last_json = json.loads(replace_simple_quotation)  # Convierto a JSON mi str

    print('+++++++')
    print(last_json)
    print(type(last_json))

    print(last_json['accion'])
    print(last_json.get('accion'))
    print(id_message)

    if last_json.get('accion') == 'mover ':
        escribirterminal("python pose.py")
        print("escribí en la terminal: python pose.py ")

    if last_json.get('accion') == 'Tomar ':
        escribirterminal("python tomarfoto.py")
        time.sleep(1)
        escribirterminal("python mov_arms.py")
        print("escribí en la terminal: python tomarfoto.py && python mov_arms.py ")

    if last_json.get('accion') == 'Posicionar ':
        escribirterminal("python TCI.py")
        time.sleep(3)
        print('escribí en la terminal: python TCI.py ')
        # datos = open("pos_actual.txt", "r")
        # valores = eval(datos.read())
        # return(valores['estado'])

    if last_json.get('accion') == 'iniciar':  # Home
        print('inicié programa guardado')
        # abrirterminal()
        # escribirterminal("cd ros_ws")
        # escribirterminal(". baxter.sh")
        # escribirterminal("rosrun baxter_tools enable_robot.py -e")
        # time.sleep(10)
        # escribirterminal("python obtener_pos.py")

    if last_json.get('accion') == 'set':  # Set
        print('seteé posición')
        # escribirterminal("rosrun baxter_tools tuck_arms.py -u")
        # borrar_registros()
        # time.sleep(5)
        # escribirterminal("python obtener_pos.py")

    if last_json.get('accion') == 'save':  # Guardar
        print('guardé la información')
        # os.rename("movimientosleft.txt", "Programas/" +
        #           str(datos['nombre_programa'])+"l.txt")
        # os.rename("movimientosright.txt", "Programas/" +
        #           str(datos['nombre_programa'])+"r.txt")

    if last_json.get('accion') == 'apagar':  # Apagar
        print('me apagué')
        # escribirterminal("rosrun baxter_tools tuck_arms.py -t")
        # escribirterminal("exit")
        # escribirterminal("exit")
        # borrar_registros()

    return str(js_string)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
