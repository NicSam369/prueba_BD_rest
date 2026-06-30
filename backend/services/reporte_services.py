from database import get_connection


def obtener_reporte_categorias():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            c.nombre AS categoria,
            p.nombre AS producto,
            COUNT(DISTINCT dp.id_pedido) AS num_pedidos,
            SUM(dp.cantidad) AS total_unidades,
            SUM(dp.cantidad * dp.precio_unitario) AS ingreso_total
        FROM CATEGORIA c
        JOIN PRODUCTO p ON p.id_categoria = c.id_categoria
        JOIN DETALLE_PEDIDO dp ON dp.id_producto = p.id_producto
        JOIN PEDIDO ped ON ped.id_pedido = dp.id_pedido
        GROUP BY c.nombre, p.nombre
        HAVING SUM(dp.cantidad) > 0
        ORDER BY ingreso_total DESC;
    """)

    filas = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []
    for fila in filas:
        resultado.append({
            "categoria": fila[0],
            "producto": fila[1],
            "num_pedidos": fila[2],
            "total_unidades": float(fila[3]),
            "ingreso_total": float(fila[4])
        })

    return resultado
