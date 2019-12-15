from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id



@app.route("/")
@app.route("/home")
@app.route("/root")
def home():
    return render_template("home.html")

@app.route("/resume")
def about():
    return render_template("about.html")

@app.route("/github")
def github():
    return render_template("github.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
    

if __name__ == '__main__':
    app.run(debug=True)