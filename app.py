from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def ui_index():
    return render_template("index.html", title="VRSA")

@app.get("/wardrobe")
def ui_wardrobe():
    return render_template("wardrobe.html", title="Wardrobe • VRSA")

@app.get("/outfit")
def ui_outfit():
    return render_template("outfit.html", title="Outfit • VRSA")

@app.get("/history")
def ui_history():
    return render_template("history.html", title="History • VRSA")

@app.get("/login")
def ui_login():
    return render_template("login.html", title="Login • VRSA")

@app.get("/register")
def ui_register():
    return render_template("register.html", title="Register • VRSA")

if __name__ == "__main__":
    app.run(debug=True)