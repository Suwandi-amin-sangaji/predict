
import os
from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler

from rainfall import app
from tensorflow import keras


class Model:
    def __init__(self):
        MODELS_PATH = os.path.join(app.config["MODELS_PATH"], 'save_model.pb')

        if os.path.exists(MODELS_PATH):
            self.models = keras.models.load_model(app.config["MODELS_PATH"])
        else:
            self.models = None

        PATH_DATA = os.path.join(app.config["STATIC_PATH"], 'hasil.csv')
        self.dataframe = read_csv(PATH_DATA)

        self.scalar = MinMaxScaler()

        self.look_back = 1
        self.features = 1


