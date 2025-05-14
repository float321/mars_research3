from flask import Flask, render_template


app = Flask(__name__)


@app.route('/choice/<planet_name>')
def choose_planet(planet_name):
    return render_template('choice.html', planet=planet_name)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return render_template('results.html', nickname=nickname, level=level, rating=rating)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
