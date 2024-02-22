import awsgi
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def intex():
    return jsonify(status=200, message='OK')

@app.route('/monitor')
def monitor():
    return jsonify(status= 200, message= 'Echo: I\'m good')

@app.route('/health')
def health_data():
    health_metrics = {
        "frecuencia cardíaca": 72,  # bpm 
        "ftp": 250,                 # Functional Threshold Power en watts 
        "saturación": 98,           # Porcentaje de saturación de oxígeno
        "velocidad": 5.5,           # km/h
        "distancia recorrida": 10.2 # Km
    }

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})

if __name__ == "__lambda_function__":
    app.run()