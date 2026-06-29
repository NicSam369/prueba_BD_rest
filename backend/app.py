from flask import Flask
from flask_cors import CORS
from database import get_connection

from routes.cliente_routes import cliente_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(cliente_bp)

@app.route("/")
def inicio():
    return {
        "mensaje": "API RESTAURANTE funcionando correctamente",
        "estado": "OK"
    }

@app.route("/api/test-db")
def test_db():
    try:
        conexion = get_connection()
        cursor = conexion.cursor()

        cursor.execute("SELECT NOW();")
        fecha = cursor.fetchone()

        cursor.close()
        conexion.close()

        return {
            "estado": "OK",
            "mensaje": "Conexión exitosa a PostgreSQL",
            "servidor": str(fecha[0])
        }

    except Exception as e:
        return {
            "estado": "ERROR",
            "mensaje": str(e)
        }, 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)