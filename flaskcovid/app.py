
from flask import (
    Flask,
    render_template,
    request,
    flash
    )
import pandas as pd
from test_function import test_function
from forms import InputForm


app = Flask(__name__)
app.secret_key = 'sdfjsbs'

@app.route('/')
@app.route('/main')
def main():
    user = { 'nickname': 'COSMOS' } # fake user
    return render_template('main.html',
                            user = { 'nickname': 'COSMOS' },
                            title = 'Home'
                            )

@app.route('/index')
def index():
	return render_template("index.html",
       title = 'Index')


@app.route('/input/output',methods=['GET', 'POST'])
@app.route('/input',methods=['GET', 'POST'])
def input():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        output = test_function(form.input1.data, form.input2.data)
        return render_template("output.html", output=output
                                ,title = 'Output')
    else:
        flash('Please enter a valid value', 'danger')
        return render_template("input.html", form=form
                                ,title = 'Input')

@app.route('/data')
def data():
    return render_template("data.html",
        title = 'Data')


if __name__ == '__main__':
    app.run(debug=True)
