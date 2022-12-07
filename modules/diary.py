from flask import flash, render_template

def agenda(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM agenda')
    data = cur.fetchall()
    return data

def add_turno(mysql, request):
    if request.method == 'POST':
        nombre_apellido = request.form['nombre_apellido']
        fecha = request.form['fecha']
        hora = request.form['hora']
        observaciones = request.form['observaciones']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO agenda (nombre_apellido, fecha, hora, observaciones) VALUES (%s, %s,%s, %s)',
                    (nombre_apellido, fecha, hora, observaciones))
        mysql.connection.commit()
        flash('Turno agregado con éxito')
        #return redirect(url_for('agenda'))

def get_turno(mysql, id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM agenda WHERE id = %s', [id])
    data = cur.fetchall()
    return data

def update_turno(mysql, id, request):
    if request.method == 'POST':
        nombre_apellido = request.form['nombre_apellido']
        fecha = request.form['fecha']
        hora = request.form['hora']
        observaciones = request.form['observaciones']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE agenda
            SET nombre_apellido = %s,
                fecha = %s,
                hora = %s,
                observaciones = %s
            WHERE id = %s  
            """, (nombre_apellido, fecha, hora, observaciones, id))
        mysql.connection.commit()
        flash('Turno editado con éxito')

def delete_turno(mysql, id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM agenda WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Turno removido con éxito')

# ------------------------BUSCADOR de Agenda------------------------------

