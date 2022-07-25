
from flask import render_template, request, flash

from rainfall import app
from rainfall.models import Model
import numpy as np
import pandas as pd

model = Model()

# Route
@app.route("/", methods=['GET', 'POST'])
def index():
	data_kemarin = None
	prediksi = None
	if len(request.form) > 0:
		try:
			data_kemarin = float(request.form["kemarin"])

			data_arr = np.array([data_kemarin])

			dataframe = pd.DataFrame(data_arr, columns=["curah_hujan"])
			dataframe = model.dataframe[["curah_hujan"]].append(dataframe)

			data_input = model.scalar.fit_transform(dataframe)
			data_input = data_input.reshape((data_input.shape[0], data_input.shape[1], model.features))

			prediksi = model.models.predict(data_input, verbose=0)

			prediksi = model.scalar.inverse_transform(prediksi)
			prediksi = prediksi[-1][0]
		except:
			flash("Input Error or Cant get Models")

	return render_template('home.html', kemarin=data_kemarin, hasil=prediksi)


