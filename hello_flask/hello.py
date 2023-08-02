from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return '<b>' + function() + '</b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return '<em>' + function() + '</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return '<u>' + function() + '</u>'
    return wrapper_function

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/wHc92cHADhpLi/giphy.gif">'
@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return'Bye!'


if __name__ == '__main__':
    # Run in debug mode to enable auto reload
    app.run(debug=True)

