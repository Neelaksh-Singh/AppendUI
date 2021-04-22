from flask import Flask, request, render_template
from content import *
import subprocess as sub
import ntpath


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


app = Flask("myarthUi")


@app.route('/form')
def myform():
    return render_template("basic.html")


@app.route('/data', methods=['POST', 'GET'])
def mydata():
    name = str(request.form.get('name'))
    roll = str(request.form.get('roll'))
    passed = [(name, int(roll))]
    appendSheet(passed)
    z = sub.getoutput('dir *.xlsx')
    path = path_leaf(z)
    return(path)


app.run(port=6161, debug=True)
