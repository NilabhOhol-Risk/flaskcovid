
from flask import Flask, render_template
import pandas as pd

df = pd.read_csv('https://data.boston.gov/dataset/c8b8ef8c-dd31-4e4e-bf19-af7e4e0d7f36/resource/29e74884-a777-4242-9fcc-c30aaaf3fb10/download/economic-indicators.csv',
                 parse_dates=[['Year', 'Month']])
length = len(df)
app = Flask(__name__)

@app.route('/')
@app.route('/main')
def main():
    user = { 'nickname': 'COSMOS' } # fake user
    return render_template('main.html',
                            user = { 'nickname': 'COSMOS' },
                            length=length,
                            dataframe=df.to_html())

@app.route('/index')
def index():
	return render_template("index.html",
       title = 'Index')

@app.route('/input')
def input():
    return render_template("input.html",
        title = 'Input')

@app.route('/output')
def output():
    return render_template("output.html",
        title = 'Output')

@app.route('/data')
def data():
    return render_template("data.html",
        title = 'Data')




if __name__ == '__main__':
    app.run(debug=True)
