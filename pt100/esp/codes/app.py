import flask

temp = 0

app = flask.Flask(__name__)
@app.route('/temp', methods=['GET', 'PUT'])
def status_handler():
    global temp
    if flask.request.method == 'GET':
        return "Current temperature: " + str(temp)
        # return {
        #     "temp": temp
        # }
    elif flask.request.method == 'PUT':
        temp = flask.request.json['temp']
        return {}
