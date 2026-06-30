from database import get_connection

def obtener_empleados():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_empleado,
               nombre,
               apellido,
               dni,
               email,
               telefono,
               rol,
               turno,
               id_scrsal
        FROM empleado
        ORDER BY id_empleado;
    """)

    empleados = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for empleado in empleados:
        resultado.append({
            "id_empleado": empleado[0],
            "nombre": empleado[1],
            "apellido": empleado[2],
            "dni": empleado[3],
            "email": empleado[4],
            "telefono": empleado[5],
            "rol": empleado[6],
            "turno": empleado[7],
            "id_scrsal": empleado[8]
        })

    return resultado

def obtener_empleado_por_id(id_empleado):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_empleado,
               nombre,
               apellido,
               dni,
               email,
               telefono,
               rol,
               turno,
               id_scrsal
        FROM empleado
        WHERE id_empleado = %s;
    """, (id_empleado,))

    empleado = cursor.fetchone()

    cursor.close()
    conexion.close()

    if empleado is None:
        return {
            "estado": "ERROR",
            "mensaje": "Empleado no encontrado"
        }

    return {
            "id_empleado": empleado[0],
            "nombre": empleado[1],
            "apellido": empleado[2],
            "dni": empleado[3],
            "email": empleado[4],
            "telefono": empleado[5],
            "rol": empleado[6],
            "turno": empleado[7],
            "id_scrsal": empleado[8]
    }

def crear_empleado(nombre, apellido, dni, email, telefono, rol, turno, id_scrsal):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO empleado
        (nombre, apellido, dni, email, telefono, rol, turno, id_scrsal)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id_empleado;
    """, (nombre, apellido, dni, email, telefono, rol, turno, id_scrsal))

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Empleado creado correctamente",
        "id_empleado": nuevo_id
    }

def actualizar_empleado(id_empleado, nombre, apellido, dni, email, telefono, rol, turno, id_scrsal):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE empleado
        SET nombre = %s,
            apellido = %s,
            dni = %s,
            email = %s,
            telefono = %s,
            rol = %s,
            turno = %s,
            id_scrsal = %s
        WHERE id_empleado = %s;
    """, (nombre, apellido, dni, email, telefono, rol, turno, id_scrsal, id_empleado))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Empleado no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Empleado actualizado correctamente"
    }

def eliminar_empleado(id_empleado):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM empleado
        WHERE id_empleado = %s;
    """, (id_empleado,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Empleado no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Empleado eliminado correctamente"
    }