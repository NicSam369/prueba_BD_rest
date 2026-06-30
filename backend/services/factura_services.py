from database import get_connection

def obtener_facturas():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_factura,
               numero,
               fecha_emision,
               monto_total,
               id_pago
        FROM factura
        ORDER BY id_factura;
    """)

    facturas = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for factura in facturas:
        resultado.append({
            "id_factura": factura[0],
            "numero": factura[1],
            "fecha_emision": str(factura[2]),
            "monto_total": float(factura[3]),
            "id_pago": factura[4]
        })

    return resultado


def obtener_factura_por_id(id_factura):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_factura,
               numero,
               fecha_emision,
               monto_total,
               id_pago
        FROM factura
        WHERE id_factura = %s;
    """, (id_factura,))

    factura = cursor.fetchone()

    cursor.close()
    conexion.close()

    if factura is None:
        return {
            "estado": "ERROR",
            "mensaje": "Factura no encontrada"
        }

    return {
        "id_factura": factura[0],
        "numero": factura[1],
        "fecha_emision": str(factura[2]),
        "monto_total": float(factura[3]),
        "id_pago": factura[4]
    }


def crear_factura(numero, fecha_emision, monto_total, id_pago):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO factura
        (numero, fecha_emision, monto_total, id_pago)
        VALUES (%s, %s, %s, %s)
        RETURNING id_factura;
    """, (numero, fecha_emision, monto_total, id_pago))

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Factura creada correctamente",
        "id_factura": nuevo_id
    }


def actualizar_factura(id_factura, numero, fecha_emision, monto_total, id_pago):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE factura
        SET numero = %s,
            fecha_emision = %s,
            monto_total = %s,
            id_pago = %s
        WHERE id_factura = %s;
    """, (numero, fecha_emision, monto_total, id_pago, id_factura))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Factura no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Factura actualizada correctamente"
    }


def eliminar_factura(id_factura):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM factura
        WHERE id_factura = %s;
    """, (id_factura,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Factura no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Factura eliminada correctamente"
    }