from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", message="Привіт Ніколай!", message1="Йди гуляй", links="Перелік посилань:", link1="https://github.com/Prostokishyn/Practical7",
    link2="https://www.rv-it.college", link3="http://127.0.0.1:5000", link4="http://127.0.0.1:5000/about/Dima", link5="http://127.0.0.1:5000/aboutus", link6="http://127.0.0.1:5000/form")

@app.route("/about/<name>")
def name_page(name):
    return f"<h1 style=\"color:blue;\">Привіт, {name}!</h1>"

@app.route("/aboutus")
def about_us():
    return render_template("about_us.html", hello="Привіт, ця сторінка про мене", my_name="Я Простокішин Дмитро Валерійович", birthday="Народився 29.11.2004",
    country="Живу в Україні, місто Рівне", college="Навчаюсь в РФКІТ")

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return render_template('show_info.html', name=name, email=email, message=message)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)