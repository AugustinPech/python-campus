from bottle import route, run, template, error,TEMPLATE_PATH, request, redirect
import mariadb
import identifier.ident as ident
import sys
import os

abs_views_path= os.path.join(os.getcwd(), 'bottle_exercice')
abs_views_path= os.path.join(abs_views_path,'views')
TEMPLATE_PATH.insert(0,abs_views_path)

def connect():
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
    return co

def setupDB(co):
    
    cur = co.cursor()
    cur.execute("DROP TABLE IF EXISTS todoList.todo")
    cur.execute("CREATE TABLE IF NOT EXISTS todoList.todo (id  int(11) NOT NULL AUTO_INCREMENT, task char(100), status bool, PRIMARY KEY(id))ENGINE = InnoDB;")
    cur.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
    cur.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
    cur.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
    cur.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
    co.commit()


def todo_list(co):
    
    cur = co.cursor()
    cur.execute("SELECT * FROM todo where status = 1")
    result = cur.fetchall()
    cur.close()
    output = template('make_table', rows=result)
    return output

def new_item(co):
    if request.GET.save:
        new = request.GET.task.strip()
       
        c = co.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid
        co.commit()
        c.close()

        return redirect('/todo')
    else :
        return template('new_task.tpl')

def edit_item(co,no):

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

        return redirect('/todo')
    else:
        c = co.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
        cur_data = c.fetchone()

        return template('edit_task', old=cur_data, no=no)

def show_item(co, item):
    
    c = co.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (item,))
    result = c.fetchall()
    c.close()
    if not result:
        return 'This item number does not exist!'
    else:
        return 'Task: %s' % result[0]

def show_json(co , json):
    c = co.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (json,))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task': 'This item number does not exist!'}
    else:
        return {'task': result[0]}