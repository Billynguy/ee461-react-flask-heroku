import os
from flask import Flask, send_from_directory, jsonify, after_this_request

app = Flask(__name__, static_url_path='', static_folder='ui/build/')


@app.route('/')
def index():
    return send_from_directory('ui/build/', 'index.html')

@app.route('/joinProject/<projectid>')
def joinProject(projectid):
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    return projectid


@app.route('/leaveProject/<projectid>')
def leaveProject(projectid):
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    return projectid


@app.route('/checkIn/<projectid>/<qty>')
def checkIn_hardware(projectid, qty):
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    jsonResp = {'name': projectid, 'qty': qty}
    return jsonResp


@app.route('/checkOut/<projectid>/<qty>')
def checkOut_hardware(projectid, qty):
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    jsonResp = {'name': projectid, 'qty': qty}
    return jsonResp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
