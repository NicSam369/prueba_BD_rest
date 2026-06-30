from database import get_connection


def obtener_pedidos():
    conexion = get_connection()
    cursor = conexion.cursor()

    # JOIN para traer nombre de cliente, empleado y numero de mesa
    cursor.execute("""
        SELECT
            p.id_pedido,
            c.nombre || ' ' || c.apellido AS cliente,
            e.nombre || ' ' || e.apellido AS empleado,
            m.numero AS mesa,
            p.fecha_hora,
            p.estado,
            p.total
        FROM pedido p
        JOIN cliente  c ON c.id_cliente  = p.id_cliente
        JOIN empleado e ON e.id_empleado = p.id_empleado
        JOIN mesa     m ON m.id_mesa     = p.id_mesa
        ORDER BY p.id_pedido;
    """)

    pedidos = cursor.fetchall()
    cursor.close()
    conexion.close()

    resultado = []
    for pedido in pedidos:
        resultado.append({
            "id_pedido": pedido[0],
            "cliente":   pedido[1],
            "empleado":  pedido[2],
            "mesa":      pedido[3],
            "fecha_hora": str(pedido[4]),
            "estado":    pedido[5],
            "total":     float(pedido[6]) if pedido[6] is not None else 0.0
        })

    # El frontend hace json.data, por eso envolvemos aquí
    return {"data": resultado}


def obtener_pedido_por_id(id_pedido):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_pedido, id_cliente, id_empleado, id_mesa,
               fecha_hora, estado, total
        FROM pedido
        WHERE id_pedido = %s;
    """, (id_pedido,))

    pedido = cursor.fetchone()
    cursor.close()
    conexion.close()

    if pedido is None:
        return {"estado": "ERROR", "mensaje": "Pedido no encontrado"}

    return {
        "id_pedido":  pedido[0],
        "id_cliente": pedido[1],
        "id_empleado":pedido[2],
        "id_mesa":    pedido[3],
        "fecha_hora": str(pedido[4]),
        "estado":     pedido[5],
        "total":      float(pedido[6]) if pedido[6] is not None else 0.0
    }


def crear_pedido(id_cliente, id_empleado, id_mesa, productos, estado="Pendiente"):
    if not productos:
        return {"estado": "ERROR", "mensaje": "El pedido debe incluir al menos un producto"}

    total = sum(p["cantidad"] * p["precio_unitario"] for p in productos)

    conexion = get_connection()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            INSERT INTO pedido (id_cliente, id_empleado, id_mesa, estado, total)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id_pedido;
        """, (id_cliente, id_empleado, id_mesa, estado, total))

        nuevo_id = cursor.fetchone()[0]

        for p in productos:
            subtotal = p["cantidad"] * p["precio_unitario"]
            cursor.execute("""
                INSERT INTO detalle_pedido
                (id_pedido, id_producto, cantidad, precio_unitario, subtotal)
                VALUES (%s, %s, %s, %s, %s);
            """, (nuevo_id, p["id_producto"], p["cantidad"], p["precio_unitario"], subtotal))

            # Descontar stock del producto vendido (tabla PRODUCTO)
            cursor.execute("""
                UPDATE producto
                SET stock = stock - %s
                WHERE id_producto = %s
                RETURNING stock;
            """, (p["cantidad"], p["id_producto"]))

            fila_stock = cursor.fetchone()
            if fila_stock is None:
                raise ValueError(f"El producto {p['id_producto']} no existe")
            if fila_stock[0] < 0:
                raise ValueError(
                    f"No hay stock suficiente para el producto {p['id_producto']}"
                )

        # Marcar la mesa como ocupada (tabla MESA)
        cursor.execute("""
            UPDATE mesa
            SET estado = 'Ocupada'
            WHERE id_mesa = %s;
        """, (id_mesa,))

        conexion.commit()

    except Exception as e:
        conexion.rollback()
        cursor.close()
        conexion.close()
        return {"estado": "ERROR", "mensaje": f"No se pudo crear el pedido: {str(e)}"}

    cursor.close()
    conexion.close()

    return {
        "estado":    "OK",
        "mensaje":   "Pedido creado correctamente",
        "id_pedido": nuevo_id,
        "total":     float(total)
    }


def actualizar_estado_pedido(id_pedido, estado):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE pedido SET estado = %s WHERE id_pedido = %s;
    """, (estado, id_pedido))

    conexion.commit()
    filas = cursor.rowcount
    cursor.close()
    conexion.close()

    if filas == 0:
        return {"estado": "ERROR", "mensaje": "Pedido no encontrado"}

    return {"estado": "OK", "mensaje": "Estado actualizado correctamente"}


def eliminar_pedido(id_pedido):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM pedido WHERE id_pedido = %s;", (id_pedido,))
    conexion.commit()
    filas = cursor.rowcount
    cursor.close()
    conexion.close()

    if filas == 0:
        return {"estado": "ERROR", "mensaje": "Pedido no encontrado"}

    return {"estado": "OK", "mensaje": "Pedido eliminado correctamente"}
