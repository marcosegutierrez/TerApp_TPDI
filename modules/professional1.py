from flask import flash

def My_Profile(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM obra_social')
    data1 = cur.fetchall()
    return data1

def get_obra_social(session, mysql):
    obra_social_actual = session['obra_social_actual']
    id_obra_social_actual = session['obra_social_actual'][0]

    cur = mysql.connection.cursor()
    # cambia (id) por [id] (agarra lista executable)
    cur.execute('SELECT * FROM obra_social WHERE id_obra_social = %s',
                [id_obra_social_actual])
    data = cur.fetchall()
    return data

