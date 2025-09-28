import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

# Load trained model safely
try:
    model = pickle.load(open("model.pkl", "rb"))
except (FileNotFoundError, EOFError) as e:
    print(f"Error loading model: {e}")
    model = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Get data from form
            gender_str = request.form["gender"]
            hemoglobin = float(request.form["hemoglobin"])
            mch = float(request.form["mch"])
            mchc = float(request.form["mchc"])
            mcv = float(request.form["mcv"])

            # Convert gender to numeric
            gender = 0 if gender_str == "male" else 1

            # Prepare input
            input_df = pd.DataFrame([[gender, hemoglobin, mch, mchc, mcv]],
                                    columns=["Gender", "Hemoglobin", "MCH", "MCHC", "MCV"])
            
            if model:
                prediction = model.predict(input_df)
                if prediction[0] == 0:
                    result = "You don't have any Anemic Disease"
                    result_class = "normal"
                else:
                    result = "You have anemic disease"
                    result_class = "anemia"

                # Pass all form values and the result class back to the template
                return render_template("predict.html",
                                       prediction_text=f"Hence, based on calculation: {result}",
                                       result_class=result_class,
                                       gender_val=gender_str,
                                       hemoglobin_val=hemoglobin,
                                       mch_val=mch,
                                       mchc_val=mchc,
                                       mcv_val=mcv)
            else:
                return "⚠️ Model not loaded. Please train the model first.", 500

        except Exception as e:
            return f"❌ Error: {str(e)}", 500

    # GET request -> show the empty form
    return render_template("predict.html",
                           gender_val="",
                           hemoglobin_val="",
                           mch_val="",
                           mchc_val="",
                           mcv_val="")

if __name__ == "__main__":
    app.run(debug=True, port=5000)