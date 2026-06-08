from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("domovni.htm")

@app.route("/index")
def domovni():
    return render_template("index.htm")

@app.route("/kontakt", methods=["GET", "POST"])
def kontakt():
    if request.method == "POST":
        jmeno = request.form.get('jmeno')
        email = request.form.get('email')
        zprava = request.form.get('zprava')
        data = {'jmeno': jmeno, 'email': email, 'zprava': zprava}
        print('Přijato (form):', data)
        return 'ok', 200
    return render_template("kontakt.htm")

@app.route("/lore")
def lore():
    return render_template("lore.htm")

@app.route("/varianti")
def varianti():
    return render_template("varianti.htm")

if __name__ == "__main__":
    app.run(debug=True)