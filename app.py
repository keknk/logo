from flask import Flask, request, send_file
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/tracker')
def tracker():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    fecha = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    # Geolocalización (opcional)
    geo = requests.get(f"http://ip-api.com/json/{ip}").json()
    ciudad = geo.get('city', 'desconocida')
    pais = geo.get('country', 'desconocido')

    # Guardar en log
    with open('logs.txt', 'a') as f:
        f.write(f"Fecha: {fecha} | IP: {ip} | Ciudad: {ciudad} | País: {pais} | User-Agent: {user_agent}\n")

    return send_file('pixel.png', mimetype='image/png')

@app.route('/')
def home():
    return 'Pixel funcionando ✅'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
