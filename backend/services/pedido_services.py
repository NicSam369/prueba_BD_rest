from database import get_connection

def obtener_pedidos():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_pedido,
               id_cliente,
               id_empleado,
               id_mesa,
               fecha_hora,
               estado,
               total
        FROM pedido
        ORDER BY id_pedido;
    """)

    pedidos = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for pedido in pedidos:
        resultado.append({
            "id_pedido": pedido[0],
            "id_cliente": pedido[1],
            "id_empleado": pedido[2],
            "id_mesa": pedido[3],
            "fecha_hora": str(pedido[4]),
            "estado": pedido[5],
            "total": float(pedido[6]) if pedido[6] is not None else None
        })

    return resultado

def obtener_pedido_por_id(id_pedido):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_pedido,
               id_cliente,
               id_empleado,
               id_mesa,
               fecha_hora,
               estado,
               total
        FROM pedido
        WHERE id_pedido = %s;
    """, (id_pedido,))

    pedido = cursor.fetchone()

    cursor.close()
    conexion.close()

    if pedido is None:
        return {
            "estado": "ERROR",
            "mensaje": "Pedido no encontrado"
        }

    return {
            "id_pedido": pedido[0],
            "id_cliente": pedido[1],
            "id_empleado": pedido[2],
            "id_mesa": pedido[3],
            "fecha_hora": str(pedido[4]),
            "estado": pedido[5],
            "total": float(pedido[6]) if pedido[6] is not None else None
    }

def crear_pedido(id_cliente, id_empleado, id_mesa, estado, productos):

    conexion = get_connection()
    cursor = conexion.cursor()

    try:

        # Crear pedido con total temporal = 0
        cursor.execute("""
            INSERT INTO pedido
            (id_cliente, id_empleado, id_mesa, estado, total)
            VALUES (%s,%s,%s,%s,%s)
            RETURNING id_pedido;
        """, (
            id_cliente,
            id_empleado,
            id_mesa,
            estado,
            0
        ))

        id_pedido = cursor.fetchone()[0]

        total = 0

        # Insertar cada producto
        for producto in productos:

            cantidad = producto["cantidad"]
            precio = producto["precio_unitario"]

            subtotal = cantidad * precio

            total += subtotal

            cursor.execute("""
                INSERT INTO detalle_pedido
                (
                    id_pedido,
                    id_producto,
                    cantidad,
                    precio_unitario,
                    subtotal
                )
                VALUES
                (%s,%s,%s,%s,%s);
            """, (
                id_pedido,
                producto["id_producto"],
                cantidad,
                precio,
                subtotal
            ))

        # Actualizar total del pedido
        cursor.execute("""
            UPDATE pedido
            SET total=%s
            WHERE id_pedido=%s;
        """, (
            total,
            id_pedido
        ))

        conexion.commit()

        return {
            "estado": "OK",
            "mensaje": "Pedido registrado correctamente",
            "id_pedido": id_pedido,
            "total": float(total)
        }

    except Exception as e:

        conexion.rollback()

        return {
            "estado": "ERROR",
            "mensaje": str(e)
        }

    finally:

        cursor.close()
        conexion.close()

def actualizar_pedido(id_pedido, id_cliente, id_empleado, id_mesa, fecha_hora, estado, total):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE pedido
        SET id_cliente = %s,
            id_empleado = %s,
            id_mesa = %s,
            fecha_hora = %s,
            estado = %s,
            total = %s
        WHERE id_pedido = %s;
    """, (id_cliente, id_empleado, id_mesa, fecha_hora, estado, total, id_pedido))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Pedido no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Pedido actualizado correctamente"
    }

def eliminar_pedido(id_pedido):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM pedido
        WHERE id_pedido = %s;
    """, (id_pedido,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Pedido no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Pedido eliminado correctamente"
    }
