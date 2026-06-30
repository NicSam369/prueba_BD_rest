from database import get_connection

def obtener_detalles_pedido():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_detalle,
               id_pedido,
               id_producto,
               cantidad,
               precio_unitario,
               subtotal
        FROM detalle_pedido
        ORDER BY id_detalle;
    """)

    detalles = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for detalle in detalles:
        resultado.append({
            "id_detalle": detalle[0],
            "id_pedido": detalle[1],
            "id_producto": detalle[2],
            "cantidad": float(detalle[3]),
            "precio_unitario": float(detalle[4]),
            "subtotal": float(detalle[5]) if detalle[5] is not None else None
        })

    return resultado


def obtener_detalle_por_id(id_detalle):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_detalle,
               id_pedido,
               id_producto,
               cantidad,
               precio_unitario,
               subtotal
        FROM detalle_pedido
        WHERE id_detalle = %s;
    """, (id_detalle,))

    detalle = cursor.fetchone()

    cursor.close()
    conexion.close()

    if detalle is None:
        return {
            "estado": "ERROR",
            "mensaje": "Detalle de pedido no encontrado"
        }

    return {
        "id_detalle": detalle[0],
        "id_pedido": detalle[1],
        "id_producto": detalle[2],
        "cantidad": float(detalle[3]),
        "precio_unitario": float(detalle[4]),
        "subtotal": float(detalle[5]) if detalle[5] is not None else None
    }


def crear_detalle(id_pedido, id_producto, cantidad, precio_unitario, subtotal):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO detalle_pedido
        (id_pedido, id_producto, cantidad, precio_unitario, subtotal)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_detalle;
    """, (id_pedido, id_producto, cantidad, precio_unitario, subtotal))

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Detalle de pedido creado correctamente",
        "id_detalle": nuevo_id
    }


def actualizar_detalle(id_detalle, id_pedido, id_producto, cantidad, precio_unitario, subtotal):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE detalle_pedido
        SET id_pedido = %s,
            id_producto = %s,
            cantidad = %s,
            precio_unitario = %s,
            subtotal = %s
        WHERE id_detalle = %s;
    """, (id_pedido, id_producto, cantidad, precio_unitario, subtotal, id_detalle))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Detalle de pedido no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Detalle de pedido actualizado correctamente"
    }


def eliminar_detalle(id_detalle):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM detalle_pedido
        WHERE id_detalle = %s;
    """, (id_detalle,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Detalle de pedido no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Detalle de pedido eliminado correctamente"
    }