from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newtest.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50))

class Lang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(50))

class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(50))

@app.route("/")
def author():
    return render_template('author.html')

@app.route("/languages")
def languages():
    return render_template('languages.html')

@app.route("/level")
def level():
    return render_template('level.html')

@app.route("/main")
def main():
    post  = User.query.all()
    post1 = Lang.query.all()
    post2 = Level.query.all()
    return render_template('main.html',post=post,post1=post1,post2=post2)


@app.route('/adduser', methods=['POST'])
def adduser():
    if request.method == 'POST':
        author = request.form['author']
        post = User(author=author)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('languages'))
    return render_template('author.html')

@app.route('/addlanguage', methods=['POST','GET'])
def addlanguage():
    if request.method == 'POST':
        language = request.form['language']
        post1 = Lang(language=language)
        db.session.add(post1)
        db.session.commit()
        return redirect(url_for('addlevel'))
    return render_template('languages.html')

@app.route('/addlevel', methods=['POST','GET'])
def addlevel():
    if request.method == 'POST':
        level = request.form['level']
        post2 = Level(level=level)
        db.session.add(post2)
        db.session.commit()
        return redirect(url_for('main'))
    return render_template('level.html')




@app.route("/resetdb")
def resetdb():
    db.drop_all()
    db.create_all()
    return redirect(url_for('author'))

if __name__ == '__main__':
    app.run(debug=True)