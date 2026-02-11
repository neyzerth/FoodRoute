from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

puntos_guardados = []

@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/guardar_punto", methods=["POST"])
def guardar_punto():
    # 1. Obtener los datos JSON que envía el JavaScript
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No se recibieron datos"}), 400

    # 2. Extraer valores individuales (opcional, para validación)
    lat = data.get('latitud')
    lng = data.get('longitud')
    timestamp = data.get('timestamp')
    
    print(f"📍 Coordenada recibida: {lat}, {lng} a las {timestamp}")

    # 3. Guardar en la lista (o aquí conectarías tu Base de Datos)
    puntos_guardados.append(data)

    # 4. Responder al cliente (JS) que todo salió bien
    return jsonify({"status": "success", "message": "Punto guardado"}), 200