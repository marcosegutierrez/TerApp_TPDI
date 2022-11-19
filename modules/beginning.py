def Beginning(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sala_espera')
    data = cur.fetchall()
    print(data)
    return data