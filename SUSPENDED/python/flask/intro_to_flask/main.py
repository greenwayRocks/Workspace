from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sign', methods=['GET', 'POST'])
def sign():
    if request.method == 'POST':
        # do sth
        name = request.form.get('inputName')
        comment = request.form.get('comment')
        return render_template('index.html', name=name, comment=comment)
        # return '{} -> {}'.format(name, comment)
        # return redirect(url_for('index'))
    return render_template('sign.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
