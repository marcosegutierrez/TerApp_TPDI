from flask import flash

def My_Profile(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM profesional')
    data = cur.fetchall()
    return data

def add_professional(request, mysql):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        email = request.form['email']
        titulo = request.form['titulo']
        institucion_educativa = request.form['institucion_educativa']
        es_prestador = request.form['es_prestador']
        obra_social = request.form['obra_social']
        esta_matriculado = request.form['esta_matriculado']
        matricula = request.form['matricula']
        contraseña = request.form['contraseña']
        repetir_contraseña = request.form['repetir_contraseña']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO profesional (nombre, apellido, dni, telefono, direccion, email, titulo, institucion_educativa, es_prestador, id_obra_social, esta_matriculado, matricula, contraseña, repetir_contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (nombre, apellido, dni, telefono, direccion, email, titulo, institucion_educativa, es_prestador, obra_social, esta_matriculado, matricula, contraseña, repetir_contraseña))
        mysql.connection.commit()

def get_profesional(session, mysql):
    profesional_actual = session['profesional_actual']
    id_profesional_actual = session['profesional_actual'][0]

    cur = mysql.connection.cursor()
    # cambie (id) por [id] (agarra lista executable)
    cur.execute('SELECT * FROM profesional WHERE id_profesional = %s',
                [id_profesional_actual])
    data = cur.fetchall()
    return data

def update_professional(id, request, mysql):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        email = request.form['email']
        titulo = request.form['titulo']
        institucion_educativa = request.form['institucion_educativa']
        es_prestador = request.form['es_prestador']
        obra_social = request.form['obra_social']
        esta_matriculado = request.form['esta_matriculado']
        matricula = request.form['matricula']
        contraseña = request.form['contraseña']
        repetir_contraseña = request.form['repetir_contraseña']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE profesional
            SET nombre = %s,
                apellido = %s,
                dni = %s,
                telefono = %s,
                direccion = %s,
                email = %s,
                titulo = %s,
                institucion_educativa = %s,
                es_prestador = %s,
                id_obra_social = %s,
                esta_matriculado = %s,
                matricula = %s,
                contraseña = %s,
                repetir_contraseña = %s
            WHERE id_profesional = %s  
            """, (nombre, apellido, dni, telefono, direccion, email, titulo, institucion_educativa,
                  es_prestador, obra_social, esta_matriculado,
                  matricula, contraseña, repetir_contraseña, id))
        mysql.connection.commit()