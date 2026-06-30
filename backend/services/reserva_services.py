from database import get_connection

def obtener_reservas():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_reserva,
               fecha_reserva,
               hora,
               num_personas,
               estado,
               id_cliente,
               id_mesa,
               id_scrsal
        FROM reserva
        ORDER BY id_reserva;
    """)

    reservas = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for reserva in reservas:
        resultado.append({
            "id_reserva": reserva[0],
            "fecha_reserva": str(reserva[1]),
            "hora": str(reserva[2]),
            "num_personas": reserva[3],
            "estado": reserva[4],
            "id_cliente": reserva[5],
            "id_mesa": reserva[6],
            "id_scrsal": reserva[7]
        })

    return resultado


def obtener_reserva_por_id(id_reserva):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_reserva,
               fecha_reserva,
               hora,
               num_personas,
               estado,
               id_cliente,
               id_mesa,
               id_scrsal
        FROM reserva
        WHERE id_reserva = %s;
    """, (id_reserva,))

    reserva = cursor.fetchone()

    cursor.close()
    conexion.close()

    if reserva is None:
        return {
            "estado": "ERROR",
            "mensaje": "Reserva no encontrada"
        }

    return {
        "id_reserva": reserva[0],
        "fecha_reserva": str(reserva[1]),
        "hora": str(reserva[2]),
        "num_personas": reserva[3],
        "estado": reserva[4],
        "id_cliente": reserva[5],
        "id_mesa": reserva[6],
        "id_scrsal": reserva[7]
    }


def crear_reserva(fecha_reserva, hora, num_personas, estado, id_cliente, id_mesa, id_scrsal):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO reserva
        (fecha_reserva, hora, num_personas, estado, id_cliente, id_mesa, id_scrsal)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id_reserva;
    """, (fecha_reserva, hora, num_personas, estado, id_cliente, id_mesa, id_scrsal))

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Reserva creada correctamente",
        "id_reserva": nuevo_id
    }


def actualizar_reserva(id_reserva, fecha_reserva, hora, num_personas, estado, id_cliente, id_mesa, id_scrsal):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE reserva
        SET fecha_reserva = %s,
            hora = %s,
            num_personas = %s,
            estado = %s,
            id_cliente = %s,
            id_mesa = %s,
            id_scrsal = %s
        WHERE id_reserva = %s;
    """, (fecha_reserva, hora, num_personas, estado, id_cliente, id_mesa, id_scrsal, id_reserva))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Reserva no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Reserva actualizada correctamente"
    }


def eliminar_reserva(id_reserva):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM reserva
        WHERE id_reserva = %s;
    """, (id_reserva,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Reserva no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Reserva eliminada correctamente"
    }