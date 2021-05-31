from aaaabottle.bottle import route, run, static_file


@route('/')
def myhome():
    return static_file('index.html', root='.')


run(host='localhost', port=9999)
