from bottle import route, run, template, error
import mariadb
import identifier.identify as ident

co = mariadb.connect(
    user= ident.user(),
    password=ident.password(),
    host='localhost',
    port=3306,
    database='todoList'
    )
co.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
co.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
co.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
co.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
co.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
co.commit()

@route('/todo')
def get():
    return 'this should display the list of items'
@route('/new')
def post():
    return 'this should display a form to add a new item'
@route('/edit/<id>')
def put(id ='0'):
    return template('this should show the item of id : {{id}}', id=id)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host='localhost', port=8080)
