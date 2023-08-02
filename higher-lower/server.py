from flask import Flask
import random


correct_number = random.randint(0, 9)
print(correct_number)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1>Guess number between 0-9</h1>' \
           '<img src="https://media.giphy.com/media/26gs9hWZig4XobSTe/giphy.gif">'


@app.route('/<int:guess>')
def guess_number(guess):
    if guess < correct_number:
        return '<h1 style="color: blue">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess > correct_number:
        return '<h1 style="color: red">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)