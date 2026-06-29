from database import get_connection

def obtener_proveedores():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT 
            id_prvdor,
            nombre,
            ruc,
            telefono,
            email,
            id_scrsal
        FROM proveedor
        ORDER BY id_prvdor;
    """)

    proveedores = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for proveedor in proveedores:
        resultado.append({
            "id_prvdor": proveedor[0],
            "nombre": proveedor[1],
            "ruc": proveedor[2],
            "telefono": proveedor[3],
            "email": proveedor[4],
            "id_scrsal": proveedor[5]
        })

    return resultado

def obtener_proveedor_por_id(id_prvdor):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT 
            id_prvdor,
            nombre,
            ruc,
            telefono,
            email,
            id_scrsal
        FROM proveedor
        WHERE id_prvdor = %s;
    """, (id_prvdor,))

    proveedor = cursor.fetchone()

    cursor.close()
    conexion.close()

    if proveedor is None:
        return {
            "estado": "ERROR",
            "mensaje": "Proveedor no encontrado"
        }

    return {
        "id_prvdor": proveedor[0],
            "nombre": proveedor[1],
            "ruc": proveedor[2],
            "telefono": proveedor[3],
            "email": proveedor[4],
            "id_scrsal": proveedor[5]
    }

def crear_proveedor(nombre, ruc, telefono, email, id_scrsal):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO proveedor
        (nombre, ruc, telefono, email, id_scrsal)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_prvdor;
    """, (nombre, ruc, telefono, email, id_scrsal))

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Proveedor creado correctamente",
        "id_prvdor": nuevo_id
    }

def actualizar_proveedor(id_prvdor, nombre, ruc, telefono, email, id_scrsal):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE proveedor
        SET nombre = %s,
            ruc = %s,
            telefono = %s,
            email = %s,
            id_scrsal = %s
        WHERE id_prvdor = %s;
    """, (nombre, ruc, telefono, email, id_scrsal, id_prvdor))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Proveedor no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Proveedor actualizado correctamente"
    }

def eliminar_proveedor(id_prvdor):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM proveedor
        WHERE id_prvdor = %s;
    """, (id_prvdor,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Proveedor no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Proveedor eliminado correctamente"
    }