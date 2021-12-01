import json
import pyautogui

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
    url = 'https://baxterassistant2.pythonanywhere.com/api/message/'
    var_get = requests.get(url)

    if 'json' in var_get.headers.get('Content-Type'):
        js_string = var_get.json()

    else:
        print('Response content is not in JSON format.')
        js_string = 'spam'

    id_message = js_string[-1]['id']
    last_json = js_string[-1]['message']

    print(last_json)
    print(id_message)
    return str(js_string)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
