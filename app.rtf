{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AppleColorEmoji;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request, send_file\
from datetime import datetime\
import requests\
\
app = Flask(__name__)\
\
@app.route(\'91/logo\'92)\
def tracker():\
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)\
    user_agent = request.headers.get('User-Agent')\
    fecha = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')\
\
    # Geolocalizaci\'f3n (opcional)\
    geo = requests.get(f"http://ip-api.com/json/\{ip\}").json()\
    ciudad = geo.get('city', 'desconocida')\
    pais = geo.get('country', 'desconocido')\
\
    # Guardar en log\
    with open('logs.txt', 'a') as f:\
        f.write(f"Fecha: \{fecha\} | IP: \{ip\} | Ciudad: \{ciudad\} | Pa\'eds: \{pais\} | User-Agent: \{user_agent\}\\n")\
\
    return send_file('pixel.png', mimetype='image/png')\
\
@app.route('/')\
def home():\
    return 'Pixel funcionando 
\f1 \uc0\u9989 
\f0 '\
\
if __name__ == '__main__':\
    app.run(host='0.0.0.0', port=10000)}