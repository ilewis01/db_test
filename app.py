from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "This is some bull-shit!"

if __name__ == '__main__':
	app.config['DEBUG'] = True
	app.run()