from bottle import route, run, template, error, static_file, debug
import setup as setup
import os

abs_views_path= os.path.join(os.getcwd(), 'bottle_exercice')
abs_views_path= os.path.join(abs_views_path,'views')
setup.setupDB(setup.connect())

@route('/todo')
def todo_list():
    return setup.todo_list(setup.connect())

@route('/new', method='GET') # http://localhost:8080/new?task=newTask
def new_item():
    return setup.new_item(setup.connect())

@route('/edit/<no:int>', method = 'GET')
def edit_item(no):
    return setup.edit_item(setup.connect(),no)

@route('/item<item:re:[0-9]+>')
def show_item(item):
    return setup.show_item(setup.connect(),item)

@route('/help')
def help():
    return static_file('help.html', root=abs_views_path)

@route('/json<json:re:[0-9]+>')
def show_json(json):
    return setup.show_json(setup.connect(),json)

@error(403)
def mistake403(code):
    return 'The parameter you passed has the wrong format!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


debug(True)
run(host='localhost', port=8080,reloader=True)
