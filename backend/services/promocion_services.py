from database import get_connection

def obtener_promociones():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_promocion,
               nombre,
               descuento_pct,
               fecha_inicio,
               fecha_fin,
               id_scrsal
        FROM promocion
        ORDER BY id_promocion;
    """)

    promociones = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for promocion in promociones:
        resultado.append({
            "id_promocion": promocion[0],
            "nombre": promocion[1],
            "descuento_pct": float(promocion[2]),
            "fecha_inicio": str(promocion[3]),
            "fecha_fin": str(promocion[4]),
            "id_scrsal": promocion[5]
        })

    return resultado


def obtener_promocion_por_id(id_promocion):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_promocion,
               nombre,
               descuento_pct,
               fecha_inicio,
               fecha_fin,
               id_scrsal
        FROM promocion
        WHERE id_promocion = %s;
    """, (id_promocion,))

    promocion = cursor.fetchone()

    cursor.close()
    conexion.close()

    if promocion is None:
        return {
            "estado": "ERROR",
            "mensaje": "Promoción no encontrada"
        }

    return {
        "id_promocion": promocion[0],
        "nombre": promocion[1],
        "descuento_pct": float(promocion[2]),
        "fecha_inicio": str(promocion[3]),
        "fecha_fin": str(promocion[4]),
        "id_scrsal": promocion[5]
    }


def crear_promocion(nombre, descuento_pct, fecha_inicio, fecha_fin, id_scrsal):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO promocion
        (nombre, descuento_pct, fecha_inicio, fecha_fin, id_scrsal)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_promocion;
    """, (nombre, descuento_pct, fecha_inicio, fecha_fin, id_scrsal))

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Promoción creada correctamente",
        "id_promocion": nuevo_id
    }


def actualizar_promocion(id_promocion, nombre, descuento_pct, fecha_inicio, fecha_fin, id_scrsal):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE promocion
        SET nombre = %s,
            descuento_pct = %s,
            fecha_inicio = %s,
            fecha_fin = %s,
            id_scrsal = %s
        WHERE id_promocion = %s;
    """, (nombre, descuento_pct, fecha_inicio, fecha_fin, id_scrsal, id_promocion))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Promoción no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Promoción actualizada correctamente"
    }


def eliminar_promocion(id_promocion):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM promocion
        WHERE id_promocion = %s;
    """, (id_promocion,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Promoción no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Promoción eliminada correctamente"
    }