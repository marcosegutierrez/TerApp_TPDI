def query(mysql, data2):
    cur = mysql.connection.cursor()
    cur.execute('''
            UPDATE sala_espera
            SET en_espera = %s
            WHERE id = 1
        ''', [data2])
    mysql.connection.commit()

def waiting(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sala_espera')
    data = cur.fetchall()
    return data

def waiting_changes(mysql, change):
    data = waiting(mysql)
    espera = int(data[0][1])+change
    espera2 = str(espera)
    query(mysql, espera2)

def waiting_update(mysql):
    waiting_changes(mysql, 1)

def waiting_delete(mysql):
    waiting_changes(mysql, -1)

def waiting_reset(mysql):
    espera = str(0)
    query(mysql, espera)
