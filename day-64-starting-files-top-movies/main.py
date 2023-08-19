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

MOVIE_DATABASE_API = "f26f0f02239b60735f955e10919a884e"
MOVIE_DATABASE_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DATABASE_DETAILS_URL = "https://api.themoviedb.org/3/movie/"
MOVIE_DATABASE_IMAGE_URL = "https://image.tmdb.org/t/p/original"


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


class EditForm(FlaskForm):
    rating = FloatField(label='Your rating out of 10 eg. 7.5')
    review = StringField(label="Your Review")
    submit = SubmitField("Done")


class AddForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    movies = result.scalars().all()

    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    add_form = AddForm()
    if add_form.validate_on_submit():
        movie_title = add_form.title.data
        response = requests.get("https://api.themoviedb.org/3/search/movie", params={"api_key": MOVIE_DATABASE_API,"query":movie_title})
        movie_list = response.json()["results"]
        return render_template("select.html", movie_list=movie_list)
    return render_template("add.html", form=add_form)

@app.route('/find')
def find_movie():
    movie_id = request.args.get("movie_id")
    if movie_id:
        response = requests.get(f"{MOVIE_DATABASE_DETAILS_URL}/{movie_id}", params={"api_key": MOVIE_DATABASE_API, "language": "en-us"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split('-')[0],
            description=data["overview"],
            img_url=f"{MOVIE_DATABASE_IMAGE_URL}/{data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', movie_id=new_movie.id))

@app.route("/edit/int:<movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = EditForm()
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
