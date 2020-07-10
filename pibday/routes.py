from flask import render_template, redirect, url_for, session
from pibday import app
from pibday.forms import BdayForm
from pibday.pi_check import Pi


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = BdayForm()
    if form.validate_on_submit():
        data = [form.month.data,
                form.day.data,
                form.year.data]
        bday = Pi(*data)
        bday.set_bday()
        bday.set_string()
        session['check'] = bday.check_pi()
        session['bday'] = bday.str_bday
        return redirect('/results')
    return render_template('index.html', form=form)


@app.route('/results', methods=['GET'])
def results():
    check = session.get('check')
    bday = session.get('bday')
    if check:
        title = 'Woo!'
    else:
        title = 'Aww'
    context = {
        'check': check,
        'title': title,
        'bday': bday
    }
    return render_template('results.html', **context)


@app.route('/pi_digits')
def pi_digits():
    with open('pi_million.txt', 'r') as pi:
        lines = (line.strip() for line in pi)
        context = {
            'title': 'Million Digits of Pi',
            'lines': lines
        }
        return render_template('pi_digits.html', **context)

