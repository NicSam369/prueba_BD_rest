from database import get_connection


def obtener_productos_jsonb(filtro=None, valor=None):
    conexion = get_connection()
    cursor = conexion.cursor()

    base_query = """
        SELECT
            p.nombre,
            c.nombre AS categoria,
            p.precio,
            p.datos_extra -> 'nivel_picante' AS picante,
            p.datos_extra -> 'nutricion' ->> 'calorias' AS calorias,
            p.datos_extra -> 'etiquetas' AS etiquetas
        FROM PRODUCTO p
        LEFT JOIN CATEGORIA c ON p.id_categoria = c.id_categoria
        WHERE p.datos_extra IS NOT NULL
    """

    params = []

    # filtro=etiqueta&valor=sin gluten  -> busca dentro del arreglo de etiquetas
    if filtro == "etiqueta" and valor:
        base_query += " AND p.datos_extra -> 'etiquetas' ? %s"
        params.append(valor)

    # filtro=alergeno&valor=pescado -> busca dentro del arreglo de alergenos
    elif filtro == "alergeno" and valor:
        base_query += " AND p.datos_extra -> 'alergenos' ? %s"
        params.append(valor)

    # filtro=picante&valor=medio -> busca por nivel de picante exacto
    elif filtro == "picante" and valor:
        base_query += " AND p.datos_extra ->> 'nivel_picante' = %s"
        params.append(valor)

    base_query += " ORDER BY p.nombre;"

    cursor.execute(base_query, params)
    filas = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []
    for fila in filas:
        resultado.append({
            "nombre": fila[0],
            "categoria": fila[1],
            "precio": float(fila[2]) if fila[2] is not None else None,
            "picante": fila[3].strip('"') if isinstance(fila[3], str) else fila[3],
            "calorias": fila[4],
            "etiquetas": fila[5] if fila[5] else []
        })

    return resultado
