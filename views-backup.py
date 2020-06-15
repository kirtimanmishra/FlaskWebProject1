"""
Routes and views for the flask application.
"""

from datetime import datetime
from FlaskWebProject1 import app
from flask import Flask, redirect, url_for, request, render_template

import pandas as pd

from FlaskWebProject1.workflow import KaliClass

#these are the list of message holders
#kali_msg_list = []

wf_datalog = KaliClass.WF_Datalogger()

@app.route('/kali',methods = ['POST', 'GET'])
def mykali() :

    global wf_datalog
    
    if request.method == 'POST':

        mydata = {}
        mydata['wfid'] = request.form['wfid']
        mydata['status'] = 'pending'
        mydata['node'] = request.form['node']
        mydata['data'] = request.form['data']

        wf_datalog.add(mydata)
        
        return 'post success'

    else:

        mydata = {}
        mydata['wfid'] = request.args.get('wfid')
        mydata['status'] = 'pending'
        mydata['node'] = request.args.get('node')
        mydata['data'] = request.args.get('data')

        wf_datalog.add(mydata)
    
        return 'get success'

@app.route('/kali/display')
def display() :
    return render_template('wf_render.html',mydf=wf_datalog.debug_getdf())

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/test/<name>')
def test(name):
    return 'test input %s ' % name

