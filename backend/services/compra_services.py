from database import get_connection

def obtener_compras():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_compra,
               fecha,
               total,
               estado,
               id_scrsal,
               id_prvdor
        FROM compra
        ORDER BY id_compra;
    """)

    compras = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for compra in compras:
        resultado.append({
            "id_compra": compra[0],
            "fecha": str(compra[1]),
            "total": float(compra[2]),
            "estado": compra[3],
            "id_scrsal": compra[4],
            "id_prvdor": compra[5]
        })

    return resultado


def obtener_compra_por_id(id_compra):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_compra,
               fecha,
               total,
               estado,
               id_scrsal,
               id_prvdor
        FROM compra
        WHERE id_compra = %s;
    """, (id_compra,))

    compra = cursor.fetchone()

    cursor.close()
    conexion.close()

    if compra is None:
        return {
            "estado": "ERROR",
            "mensaje": "Compra no encontrada"
        }

    return {
        "id_compra": compra[0],
        "fecha": str(compra[1]),
        "total": float(compra[2]),
        "estado": compra[3],
        "id_scrsal": compra[4],
        "id_prvdor": compra[5]
    }


def crear_compra(fecha, total, estado, id_scrsal, id_prvdor):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO compra
        (fecha, total, estado, id_scrsal, id_prvdor)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_compra;
    """, (fecha, total, estado, id_scrsal, id_prvdor))

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Compra creada correctamente",
        "id_compra": nuevo_id
    }


def actualizar_compra(id_compra, fecha, total, estado, id_scrsal, id_prvdor):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE compra
        SET fecha = %s,
            total = %s,
            estado = %s,
            id_scrsal = %s,
            id_prvdor = %s
        WHERE id_compra = %s;
    """, (fecha, total, estado, id_scrsal, id_prvdor, id_compra))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Compra no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Compra actualizada correctamente"
    }


def eliminar_compra(id_compra):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM compra
        WHERE id_compra = %s;
    """, (id_compra,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Compra no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Compra eliminada correctamente"
    }