from flask import Flask, render_template
app = Flask (__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.htm")

@app.route("/menu")
def menu():
    return render_template("menu.htm")

@app.route("/head")
def head():
    return render_template("head.htm")

@app.route("/footer")
def footer():
    return render_template("footer.htm")

if __name__ == "__main__":
    app.run(debug=True) 
    