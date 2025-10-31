#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

@app.route("/sum/<int:a>")
def sum(a):
    b = 15
    return f'This is a sum {b}'

@app.route('/hello')
def greeting():
    print("HERE I AM HELLO")
    return 'Hello, World'

