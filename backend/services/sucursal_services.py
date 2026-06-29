from database import get_connection

def obtener_sucursales():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_scrsal,
               nombre,
               direccion,
               ciudad,
               telefono
        FROM SUCURSAL
        ORDER BY id_scrsal;
    """)

    sucursales = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for sucursal in sucursales:
        resultado.append({
            "id_scrsal": sucursal[0],
            "nombre": sucursal[1],
            "direccion": sucursal[2],
            "ciudad": sucursal[3],
            "telefono": sucursal[4]
        })

    return resultado

def obtener_sucursal_por_id(id_scrsal):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_scrsal,
               nombre,
               direccion,
               ciudad,
               telefono
        FROM SUCURSAL
        WHERE id_scrsal = %s;
    """, (id_scrsal,))

    sucursal = cursor.fetchone()

    cursor.close()
    conexion.close()

    if sucursal is None:
        return {
            "estado": "ERROR",
            "mensaje": "Sucursal no encontrada"
        }

    return {
        "id_scrsal": sucursal[0],
            "nombre": sucursal[1],
            "direccion": sucursal[2],
            "ciudad": sucursal[3],
            "telefono": sucursal[4]
    }

def crear_sucursal(nombre, direccion, ciudad, telefono):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO sucursal
            (nombre, direccion, ciudad, telefono)
            VALUES (%s, %s, %s, %s)
            RETURNING id_scrsal;
        """, (nombre, direccion, ciudad, telefono))

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Sucursal creado correctamente",
        "id_scrsal": nuevo_id
    }

def actualizar_sucursal(id_scrsal, nombre, direccion, ciudad, telefono):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE SUCURSAL
        SET nombre = %s,
            direccion = %s,
            ciudad = %s,
            telefono = %s
        WHERE id_scrsal = %s;
    """, (nombre, direccion, ciudad, telefono, id_scrsal))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Sucursal no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Sucursal actualizada correctamente"
    }

def eliminar_sucursal(id_scrsal):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM SUCURSAL
        WHERE id_scrsal = %s;
    """, (id_scrsal,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Sucursal no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Sucursal eliminada correctamente"
    }