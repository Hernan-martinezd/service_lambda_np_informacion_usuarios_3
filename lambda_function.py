import random
import awsgi
from flask import Flask, jsonify

app = Flask(__name__)

def simulate_error():
    """Simula un error con una probabilidad del 2%."""
    return random.random() < 0.02

@app.route('/health')
def health_data():
    """Endpoint para obtener los datos de salud."""
    if simulate_error():
        return jsonify(status=500, error="Internal Server Error")
    else:
        health_metrics = {
            "frecuencia cardíaca": 72,        # bpm 
            "potencia umbral funcional": 250,  # en watts 
            "saturación de oxígeno": 98,       # Porcentaje
            "velocidad": 5.5,                  # en km/h
            "distancia recorrida": 10.2        # en km
        }
        return jsonify(status=200, data=health_metrics)

def lambda_handler(event, context):
    """Handler para AWS Lambda."""
    return awsgi.response(app, event, context, base64_content_types={"image/png"})
