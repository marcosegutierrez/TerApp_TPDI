from flask import flash

def Login(session):
    if session.get('logueado'):
        return 'Personalized_Welcome.html'
    else:
        return 'Login.html'

    # ------------------------------LOGIN Verificación de datos--------------------------------------

def do_admin_login(request, mysql, session):
    login = request.form

    email = login['email']
    password = login['password']

    if email == '' or password == '':
        flash("Completar campos! Vuelve a intentarlo")
        return 1

    cur = mysql.connection.cursor()
    cur.execute(
        'SELECT * FROM profesional WHERE email = %s and contraseña = %s', [email, password])

    profesional = cur.fetchone()

    if profesional is None:
        flash("Ups! Vuelve a intentarlo")
        return 1

    password_db = profesional[13]  # indice de la contraseña
    session['profesional_actual'] = profesional
    session['logueado'] = (password == password_db)

    return 1
    

def logout(session):
    session['logueado'] = False
    session['profesional_actual'] = None