from bottle import route, run, template, error, static_file
import setup as setup
@route('/todo')
def todo_list():
    return setup.todo_list()

@route('/new', method='GET') # http://localhost:8080/new?task=newTask
def new_item():
    return setup.new_item()


@route('/edit/<no:int>', method = 'GET')
def edit_item(no):
    return setup.edit_item(no)

@route('/item<item:re:[0-9]+>')
def show_item(item):
    return setup.show_item(item)

@route('/help')
def help():
    return static_file('help.html', root='/home/augustin/Desktop/python_campus/bottle_exercice')

@route('/json<json:re:[0-9]+>')
def show_json(json):
    return setup.show_json(json)

@error(403)
def mistake403(code):
    return 'The parameter you passed has the wrong format!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

run(host='localhost', port=8080,reloader=True)
