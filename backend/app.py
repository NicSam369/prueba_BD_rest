from flask import Flask
from flask_cors import CORS
from database import get_connection

from routes.cliente_routes import cliente_bp
from routes.sucursal_routes import sucursal_bp
from routes.categoria_routes import categoria_bp
from routes.proveedor_routes import proveedor_bp
from routes.producto_routes import producto_bp
from routes.empleado_routes import empleado_bp
from routes.mesa_routes import mesa_bp
from routes.pedido_routes import pedido_bp
from routes.detalle_pedido_routes import detalle_pedido_bp
from routes.pago_routes import pago_bp
from routes.reserva_routes import reserva_bp
from routes.factura_routes import factura_bp
from routes.compra_routes import compra_bp
from routes.detalle_compra_routes import detalle_compra_bp
from routes.promocion_routes import promocion_bp
from routes.producto_jsonb_routes import producto_jsonb_bp
from routes.reporte_routes import reporte_bp

app = Flask(__name__)
CORS(app)

# Registrar Blueprints
app.register_blueprint(cliente_bp)
app.register_blueprint(sucursal_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(proveedor_bp)
app.register_blueprint(producto_bp)
app.register_blueprint(empleado_bp)
app.register_blueprint(mesa_bp)
app.register_blueprint(pedido_bp)
app.register_blueprint(detalle_pedido_bp)
app.register_blueprint(pago_bp)
app.register_blueprint(reserva_bp)
app.register_blueprint(factura_bp)
app.register_blueprint(compra_bp)
app.register_blueprint(detalle_compra_bp)
app.register_blueprint(promocion_bp)
app.register_blueprint(producto_jsonb_bp)
app.register_blueprint(reporte_bp)

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