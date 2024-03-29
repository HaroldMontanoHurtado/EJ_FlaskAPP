from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'

@app.route('/') # ruta principal de la página
def Index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM contacts')
    data = cursor.fetchall()
    return render_template('index.html', contacts= data)

@app.route('/add_contact', methods=['POST']) # sub-ruta para agregar contactos
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        mysql.connection.commit()
        
        flash('Contact Added successfully')
        
        return redirect(url_for('Index'))

@app.route('/edit') # sub-ruta para editar contacto
def edit_contact():
    return 'Edit Contact'

@app.route('/delete/<string:id>') # sub-ruta para eliminar contacto
def delete_contact(id):
    
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact removed successfully')
    return redirect(url_for('Index'))

if(__name__=='__main__'):
    app.run(port=3000, debug=True)
