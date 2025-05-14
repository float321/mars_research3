from flask import Flask, render_template


app = Flask(__name__)


@app.route('/choice/<planet_name>')
def choose_planet(planet_name):
    return render_template('choice.html', planet=planet_name)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
