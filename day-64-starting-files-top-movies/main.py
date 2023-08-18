from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap5(app)

db = SQLAlchemy()
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating =  db.Column(db.Float, nullable=True)
    ranking =  db.Column(db.Integer, nullable=True)
    review =  db.Column(db.String(100), nullable=True)
    img_url = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

class Edit_Form(FlaskForm):
    rating = FloatField(label='Your rating out of 10 eg. 7.5')
    review = StringField(label="Your Review")
    submit = SubmitField("Done")



@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.title))
    movies = result.scalars()
    return render_template("index.html", movies=movies)


@app.route("/edit/int:<movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = Edit_Form()
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie)

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
