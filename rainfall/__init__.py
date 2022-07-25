import os
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '45270fd9edf1d068cf42565bc04cbd01'

MODELS_PATH = os.path.join(app.root_path, 'static', 'models')
if not os.path.exists(MODELS_PATH):
	os.mkdir(MODELS_PATH)
app.config['MODELS_PATH'] = MODELS_PATH

STATIC_PATH = os.path.join(app.root_path, 'static')
app.config['STATIC_PATH'] = STATIC_PATH


from rainfall import routes
