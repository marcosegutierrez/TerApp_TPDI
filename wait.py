def waiting(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sala_espera')
    data = cur.fetchall()
    print(data)
    return data

def waiting_update(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sala_espera')
    data = cur.fetchall()
    espera = int(data[0][1])+1
    espera2 = str(espera)
    cur.execute('''
            UPDATE sala_espera
            SET en_espera = %s
            WHERE id = 1
        ''', [espera2])
    mysql.connection.commit()
    return 

def waiting_update2(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sala_espera')
    data = cur.fetchall()
    espera = int(data[0][1])+1
    espera2 = str(espera)
    cur.execute('''
            UPDATE sala_espera
            SET en_espera = %s
            WHERE id = 1
        ''', [espera2])
    mysql.connection.commit()

def waiting_delete(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sala_espera')
    data = cur.fetchall()
    espera = int(data[0][1])-1
    espera2 = str(espera)
    cur.execute('''
                UPDATE sala_espera
                SET en_espera = %s
                WHERE id = 1
            ''', [espera2])
    mysql.connection.commit()

def waiting_reset(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sala_espera')
    data = cur.fetchall()
    espera = 0
    espera2 = str(espera)
    cur.execute('''
                UPDATE sala_espera
                SET en_espera = %s
                WHERE id = 1
            ''', [espera2])
    mysql.connection.commit()