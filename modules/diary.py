def agenda(mysql):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM agenda')
    data = cur.fetchall()
    return data