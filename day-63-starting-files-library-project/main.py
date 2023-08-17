from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

db = SQLAlchemy()
db.init_app(app)

# all_books = []

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # new_book = {
        #     "title": request.form["title"],
        #     "author": request.form["author"],
        #
        #     "rating": request.form["rating"]
        # }
        new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        # all_books.append(new_book)
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route('/edit/float:<book_id>', methods=["GET", "POST"])
def edit_rating(book_id):
    if request.method == 'POST':
        # book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["updated_rating"]
        db.session.commit()
        return redirect(url_for('home'))
    # book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book = db.get_or_404(Book, book_id)
    return render_template('edit_ratings.html', book=book)


@app.route('/delete/float:<book_id>')
def delete(book_id):
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(debug=True)

