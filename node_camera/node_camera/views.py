from datetime import datetime
from flask import render_template
from node_camera import app
from flask import Flask, redirect, url_for, request, render_template, Response
from flask import Flask, request, jsonify, render_template
import pandas as pd
import requests
import os, sys
from importlib import import_module
import pyodbc 

cam_dir = 'D:/Projects/Implementation Workflow/IoT Workflow/FlaskWebProject1/FlaskWebProject1/nodes/node_camera/'

@app.route('/node_camera')
def GetImagePath():
    i=0
    listing = os.listdir(cam_dir)
    for file in listing:
        #print(len(file))
        #url = 'http://localhost:5000/wfe/wf/submit'
        node_url = 'http://localhost:5000/wfe/node/submit'
        myobj = {'jobid': i, 
                 'nodeid':'node_camera',
                 'wfid':'wf_AC',
                 'nstatus':'pending',
                 'img_path':cam_dir+file,
                 'count_faces':0
                 }
        #response=requests.post(url, json=myobj)
        #print('response',response)
        response1=requests.post(node_url, json=myobj)
        print('response',response1)
        try :
            conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=DESKTOP-EGSHIGA\SQLEXPRESS;"
                          "Database=DbTest;"
                          "Trusted_Connection=yes;")
            cursor = conn.cursor() 
            SQLCommand = ('INSERT INTO [DbTest].[dbo].[kali_node] (jobid,nodeid,wfid,nstatus,img_path,FaceCount) values (?,?,?,?,?,?);')
            values = [i,'node_camera','wf_AC','pending',cam_dir+file,0]
            cursor.execute(SQLCommand,values)
            conn.commit()
            conn.close()
        except :
            pass
        i=i+1
        print('database inserted')
        #break
    return 'Images Loaded'


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
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


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )