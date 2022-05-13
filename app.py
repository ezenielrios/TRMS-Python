from flask import Flask
from controllers import front_controller
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


front_controller.route(app)


if __name__ == '__main__':
    app.run(debug=True)
