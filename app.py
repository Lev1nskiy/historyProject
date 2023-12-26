from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = 'bara bara bara bere bere bere'


@app.route('/')
@app.route('/main')
def main_page():
    return render_template('main.html')


@app.route('/main/<string:name>')
def petr(name):
    if name == 'petr':
        return render_template("petr.html")
    elif name == 'alex':
        return render_template("alex.html")
    elif name == 'chehov':
        return render_template("4eh.html")
    elif name == 'bogudonia':
        return render_template("bogudonia.html")
    elif name == 'kdom':
        return render_template("kdom.html")
    elif name == 'Kukolnik':
        return render_template("Kukolnik.html")
    elif name == 'kvartal':
        return render_template("kvartal.html")
    elif name == 'muzey':
        return render_template("muzey.html")
    elif name == 'parovoz':
        return render_template("parovoz.html")
    elif name == 'main':
        return render_template("main.html")

    elif name == 'Firt_BFG':
        return 'Oh, it`s me. But you mast not be here! Get out!'
    elif name == 'other':
        return 'В разработке...'
    else:
        return 'page is not exist. Maybe it will be added tater. Your Firt_BFG, love you'


if __name__ == '__main__':
    app.run(debug=True)
