from flask import flash

def add_message(mysql, request):
    if request.method == 'POST':
        nombre = request.form['nombre']    
        email = request.form['email']
        telefono = request.form['telefono']        
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contactenos (nombre, email, telefono, asunto, mensaje) VALUES (%s, %s, %s, %s, %s)',
                    (nombre, email, telefono, asunto, mensaje))
        mysql.connection.commit()
        flash('Mensaje enviado!')

#def message_List(mysql):
#    cur = mysql.connection.cursor()
#   cur.execute('SELECT * FROM contactenos')
#    data = cur.fetchall()
#    return data

#def get_message(mysql, id):
#    cur = mysql.connection.cursor()
#    cur.execute('SELECT * FROM contactenos WHERE id = %s', [id])
#    data = cur.fetchall()
#    return data

#Quedan pendientes de agregar opciones de borrado y edición de mensajes

