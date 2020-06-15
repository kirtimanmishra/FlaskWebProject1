import pyodbc
from datetime import datetime
from flask import render_template
from node_AC import app

@app.route('/process_AC')
def process_AC():
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                    "Server=DESKTOP-EGSHIGA\SQLEXPRESS;"
                    "Database=DbTest;"
                    "Trusted_Connection=yes;")
    cursor = conn.cursor()
    qstr = "select * from [DbTest].[dbo].[kali_node] where nodeid=\'node_AC\' and nstatus=\'pending\' "
    #print ('query is',qstr)
    cursor.execute(qstr)
    print ('AC in execution')
    #begin for loop
    for row in cursor:
        jobid = row[0]
        FaceCount = row[5] 
        print ('joblist: ',jobid, 'FaceCount: ',FaceCount, ' has been sent to Actuator for Processsing')
    return 'AC Done Processing here' 

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
