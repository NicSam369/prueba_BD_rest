from database import get_connection

def obtener_pagos():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_pago,
               monto,
               metodo,
               fcha_pago,
               estado,
               id_pedido
        FROM pago
        ORDER BY id_pago;
    """)

    pagos = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for pago in pagos:
        resultado.append({
            "id_pago": pago[0],
            "monto": float(pago[1]),
            "metodo": pago[2],
            "fcha_pago": str(pago[3]),
            "estado": pago[4],
            "id_pedido": pago[5]
        })

    return resultado


def obtener_pago_por_id(id_pago):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_pago,
               monto,
               metodo,
               fcha_pago,
               estado,
               id_pedido
        FROM pago
        WHERE id_pago = %s;
    """, (id_pago,))

    pago = cursor.fetchone()

    cursor.close()
    conexion.close()

    if pago is None:
        return {
            "estado": "ERROR",
            "mensaje": "Pago no encontrado"
        }

    return {
        "id_pago": pago[0],
        "monto": float(pago[1]),
        "metodo": pago[2],
        "fcha_pago": str(pago[3]),
        "estado": pago[4],
        "id_pedido": pago[5]
    }


def crear_pago(monto, metodo, fcha_pago, estado, id_pedido):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO pago
        (monto, metodo, fcha_pago, estado, id_pedido)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_pago;
    """, (monto, metodo, fcha_pago, estado, id_pedido))

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Pago creado correctamente",
        "id_pago": nuevo_id
    }


def actualizar_pago(id_pago, monto, metodo, fcha_pago, estado, id_pedido):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE pago
        SET monto = %s,
            metodo = %s,
            fcha_pago = %s,
            estado = %s,
            id_pedido = %s
        WHERE id_pago = %s;
    """, (monto, metodo, fcha_pago, estado, id_pedido, id_pago))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Pago no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Pago actualizado correctamente"
    }


def eliminar_pago(id_pago):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM pago
        WHERE id_pago = %s;
    """, (id_pago,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Pago no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Pago eliminado correctamente"
    }