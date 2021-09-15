from flask import Flask

app = Flask(__name__) # Lo que va entre parentesis al instanciar Flask, es el nombre de la aplicación

@app.route('/') # Decorador route, define la ruta (entre parentesis va el recurso, el más sencillo es /). Despues del decorador va una función.
def el_que_os_de_la_gana():
    return 'Hola, mundo!'.upper()

@app.route('/bye')
def otro():
    return 'Adios mundo cruel'.upper()
