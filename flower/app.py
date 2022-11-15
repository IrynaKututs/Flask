from flask import Flask, render_template, url_for,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flowers.db'
db = SQLAlchemy(app)


class Flower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Flower %r>' % self.id


class Flower_no(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Flower_no %r>' % self.id


@app.route('/')
@app.route('/home')
def info():
    return render_template('info.html')


@app.route('/1')
def one():
    flowers_no = Flower_no.query.all()
    return render_template('1.html', flowers_no=flowers_no)


@app.route('/2')
def two():
    flowers = Flower.query.all()
    return render_template('2.html', flowers=flowers)


@app.route('/1/<int:id>')
def one_id(id):
    flower_no_id = Flower_no.query.get(id)
    return render_template('1_id.html', flower_no_id=flower_no_id)

@app.route('/2/<int:id>')
def two_id(id):
    flower_id = Flower.query.get(id)
    return render_template('2_id.html', flower_id=flower_id)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create_flower', methods=['POST','GET'])
def create_flower():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        flower = Flower(title=title, text=text)
        try:
            db.session.add(flower)
            db.session.commit()
            return redirect('/2')
        except:
            return "При добавлении произошла ошибка"
    else:
        return render_template('create-flower.html')


@app.route('/create_flower_no', methods=['POST','GET'])
def create_flower_no():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        flower_no = Flower_no(title=title, text=text)
        try:
            db.session.add(flower_no)
            db.session.commit()
            return redirect('/1')
        except:
            return "При добавлении произошла ошибка"
    else:
        return render_template('create-flower-no.html')


@app.route('/1/<int:id>/update', methods=['POST','GET'])
def one_update(id):
    flower_no_id = Flower_no.query.get(id)
    if request.method == 'POST':
        flower_no_id.title = request.form['title']
        flower_no_id.text = request.form['text']
        try:
            db.session.commit()
            return redirect('/1')
        except:
            return 'При обновлении произошла ошибка'
    else:
        return render_template('1_id_update.html', flower_no_id=flower_no_id)


@app.route('/2/<int:id>/update', methods=['POST','GET'])
def two_update(id):
    flower_id = Flower.query.get(id)
    if request.method == 'POST':
        flower_id.title = request.form['title']
        flower_id.text = request.form['text']
        try:
            db.session.commit()
            return redirect('/2')
        except:
            return 'При обновлении произошла ошибка'
    else:
        return render_template('2_id_update.html',  flower_id=flower_id)


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0')