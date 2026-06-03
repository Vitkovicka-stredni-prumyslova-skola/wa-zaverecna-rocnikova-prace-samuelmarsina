from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.htm")

@app.route("/domovni")
def domovni():
    return render_template("domovni.htm")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.htm")

@app.route("/lore")
def lore():
    return render_template("lore.htm")

@app.route("/varianti")
def varianti():
    return render_template("varianti.htm")

if __name__ == "__main__":
    app.run(debug=True)