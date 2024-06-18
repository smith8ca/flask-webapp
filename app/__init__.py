import flask

app = flask.Flask(__name__)

# For running with SSL enabled:
# app.run(ssl_context=('ssl/cert.pem', 'ssl/key.pem'))
