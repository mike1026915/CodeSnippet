import time
import random
import flask


app = flask.Flask(__name__)

@app.route("/stream")
def stream():
    """
    Reference: https://medium.com/code-zen/python-generator-and-html-server-sent-events-3cdf14140e56
    """
    def eventStream():
        i = 1
        while True:
            time.sleep(1)
            yield "data: random number: {}\n\n".format(i)
            i = random.randint(0, 10000)

    return flask.wrappers.Response(eventStream(), mimetype="text/event-stream")

@app.route("/stream_numer")
def stream_numer():
    """
    Reference: https://medium.com/code-zen/python-generator-and-html-server-sent-events-3cdf14140e56
    """
    def eventStream():
        i = 1
        while True:
            time.sleep(1)
            yield "data: {}\n\n".format(i)
            i = random.randint(0, 10000)

    return flask.wrappers.Response(eventStream(), mimetype="text/event-stream")

@app.route('/hello_world')
def hello_world():
    return flask.render_template("test.html")
