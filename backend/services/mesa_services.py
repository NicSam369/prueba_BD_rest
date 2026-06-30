from database import get_connection

def obtener_mesas():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_mesa,
               id_scrsal,
               numero,
               capacidad,
               estado
        FROM mesa
        ORDER BY id_mesa;
    """)

    mesas = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for mesa in mesas:
        resultado.append({
            "id_mesa": mesa[0],
            "id_scrsal": mesa[1],
            "numero": mesa[2],
            "capacidad": mesa[3],
            "estado": mesa[4]
        })

    return resultado

def obtener_mesa_por_id(id_mesa):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_mesa,
               id_scrsal,
               numero,
               capacidad,
               estado
        FROM mesa
        WHERE id_mesa = %s;
    """, (id_mesa,))

    mesa = cursor.fetchone()

    cursor.close()
    conexion.close()

    if mesa is None:
        return {
            "estado": "ERROR",
            "mensaje": "Mesa no encontrada"
        }

    return {
            "id_mesa": mesa[0],
            "id_scrsal": mesa[1],
            "numero": mesa[2],
            "capacidad": mesa[3],
            "estado": mesa[4]
    }

def crear_mesa(id_scrsal, numero, capacidad, estado):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO mesa
        (id_scrsal, numero, capacidad, estado)
        VALUES (%s, %s, %s, %s)
        RETURNING id_mesa;
    """, (id_scrsal, numero, capacidad, estado))

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Mesa creada correctamente",
        "id_mesa": nuevo_id
    }

def actualizar_mesa(id_mesa, id_scrsal, numero, capacidad, estado):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE mesa
        SET id_scrsal = %s,
            numero = %s,
            capacidad = %s,
            estado = %s
        WHERE id_mesa = %s;
    """, (id_scrsal, numero, capacidad, estado, id_mesa))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Mesa no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Mesa actualizada correctamente"
    }

def eliminar_mesa(id_mesa):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM mesa
        WHERE id_mesa = %s;
    """, (id_mesa,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Mesa no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Mesa eliminada correctamente"
    }