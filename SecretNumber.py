from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

def calcular_numero_secreto():
    # Obtenemos la hora local del servidor
    hora_actual = datetime.datetime.now().time()

    # Utilizamos algún algoritmo para calcular el número secreto
    # En este caso, simplemente multiplicamos la hora actual por un valor arbitrario
    numero_secreto = hora_actual.hour * 100 + hora_actual.minute

    return numero_secreto

@app.route('/webhook', methods=['POST'])
def webhook():
    # Obtenemos los datos de la solicitud
    req = request.get_json(silent=True, force=True)

    # Calculamos el número secreto
    numero_secreto = calcular_numero_secreto()

    # Construimos la respuesta
    respuesta = {
        "fulfillmentText": "El número secreto es {}".format(numero_secreto)
    }

    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)
