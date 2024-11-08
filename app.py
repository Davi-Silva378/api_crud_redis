from flask import Flask
from routes.data_routes import data_controller_bp

app = Flask(__name__)

app.register_blueprint(data_controller_bp)

if __name__ == '__main__':
  app.run(debug=True)