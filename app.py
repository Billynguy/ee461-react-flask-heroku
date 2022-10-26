import os
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_url_path='', static_folder='ui/build/')


@app.route('/')
def index():
    return send_from_directory('ui/build/', 'index.html')

@app.route('/joinProject/<projectid>')
def joinProject(projectid):
    return projectid


@app.route('/leaveProject/<projectid>')
def leaveProject(projectid):
    return projectid


@app.route('/checkIn/<projectid>/<qty>')
def checkIn_hardware(projectid, qty):
    jsonResp = {'name': projectid, 'qty': qty}
    return jsonResp


@app.route('/checkOut/<projectid>/<qty>')
def checkOut_hardware(projectid, qty):
    jsonResp = {'name': projectid, 'qty': qty}
    return jsonResp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
