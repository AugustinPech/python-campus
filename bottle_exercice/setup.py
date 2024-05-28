from bottle import route, run, template, error,TEMPLATE_PATH, request
import mariadb
import identifier.ident as ident
import sys

TEMPLATE_PATH.insert(0,'/home/augustin/Desktop/python_campus/bottle_exercice/')


try :
    co = mariadb.connect(
        user= ident.user(),
        password=ident.password(),
        host='localhost',
        port=3306,
        database='todoList'
        )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
cur = co.cursor()
cur.execute("DROP TABLE IF EXISTS todoList.todo")
cur.execute("CREATE TABLE IF NOT EXISTS todoList.todo (id  int(11) NOT NULL AUTO_INCREMENT, task char(100), status bool, PRIMARY KEY(id))ENGINE = InnoDB;")
cur.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
cur.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
cur.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
cur.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
co.commit()



def todo_list():
    
    cur = co.cursor()
    cur.execute("SELECT * FROM todo")
    result = cur.fetchall()
    cur.close()
    output = template('make_table', rows=result)
    print(output)
    return output
def new_item():
    if request.GET.save:
        new = request.GET.task.strip()

        
        c = co.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid

        co.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else :
        return template('new_task.tpl')

def edit_item(no):

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'open':
            status = 1
        else:
            status = 0
        c = co.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        co.commit()

        return '<p>The item number %s was successfully updated</p>' % no
    else:
        c = co.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
        cur_data = c.fetchone()

        return template('edit_task', old=cur_data, no=no)

def show_item(item):
    
    c = co.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (item,))
    result = c.fetchall()
    c.close()
    if not result:
        return 'This item number does not exist!'
    else:
        return 'Task: %s' % result[0]

def show_json(json):
    c = co.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (json,))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task': 'This item number does not exist!'}
    else:
        return {'task': result[0]}