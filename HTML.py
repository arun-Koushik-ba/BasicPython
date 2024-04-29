# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:31:13 2024

@author: arunk
"""

from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def show_students():
    #d
    students=[
        {"name":"Hazelwood","age":20},
        {"name":"Cummins","age":20},
        {"name":"Green","age":20},
        {"name":"Maxwell","age":20},
        {"name":"Travis","age":20},
        ]
    return render_template('info.html', students=students)
app.run(port=6001)