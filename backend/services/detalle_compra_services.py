from database import get_connection

def obtener_detalles_compra():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_dtlle_compra,
               cantidad,
               subtotal,
               precio_unitario,
               id_producto,
               id_compra
        FROM detalle_compra
        ORDER BY id_dtlle_compra;
    """)

    detalles = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for detalle in detalles:
        resultado.append({
            "id_dtlle_compra": detalle[0],
            "cantidad": float(detalle[1]),
            "subtotal": float(detalle[2]),
            "precio_unitario": float(detalle[3]),
            "id_producto": detalle[4],
            "id_compra": detalle[5]
        })

    return resultado


def obtener_detalle_compra_por_id(id_dtlle_compra):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_dtlle_compra,
               cantidad,
               subtotal,
               precio_unitario,
               id_producto,
               id_compra
        FROM detalle_compra
        WHERE id_dtlle_compra = %s;
    """, (id_dtlle_compra,))

    detalle = cursor.fetchone()

    cursor.close()
    conexion.close()

    if detalle is None:
        return {
            "estado": "ERROR",
            "mensaje": "Detalle de compra no encontrado"
        }

    return {
        "id_dtlle_compra": detalle[0],
        "cantidad": float(detalle[1]),
        "subtotal": float(detalle[2]),
        "precio_unitario": float(detalle[3]),
        "id_producto": detalle[4],
        "id_compra": detalle[5]
    }


def crear_detalle_compra(cantidad, subtotal, precio_unitario, id_producto, id_compra):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO detalle_compra
        (cantidad, subtotal, precio_unitario, id_producto, id_compra)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_dtlle_compra;
    """, (cantidad, subtotal, precio_unitario, id_producto, id_compra))

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Detalle de compra creado correctamente",
        "id_dtlle_compra": nuevo_id
    }


def actualizar_detalle_compra(id_dtlle_compra, cantidad, subtotal, precio_unitario, id_producto, id_compra):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE detalle_compra
        SET cantidad = %s,
            subtotal = %s,
            precio_unitario = %s,
            id_producto = %s,
            id_compra = %s
        WHERE id_dtlle_compra = %s;
    """, (cantidad, subtotal, precio_unitario, id_producto, id_compra, id_dtlle_compra))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Detalle de compra no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Detalle de compra actualizado correctamente"
    }


def eliminar_detalle_compra(id_dtlle_compra):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM detalle_compra
        WHERE id_dtlle_compra = %s;
    """, (id_dtlle_compra,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Detalle de compra no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Detalle de compra eliminado correctamente"
    }