from flask import render_template
from flask import request
import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
#from a_Model import ModelIt


@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'Gene Doe',
	'tag' : 'Identifying Molecular Signatures in Stages of Breast Cancer' } # fake user
	return render_template("index.html",
       title = 'Home',
       user = user)

@app.route('/input')
def cesareans_input():
    return render_template("input.html")

@app.route('/output')
def cesareans_output():
    return render_template("output.html")
