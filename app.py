import pandas as pd
from jcopml.utils import load_model
from flask import Flask, render_template, request

app = Flask(__name__)
model = load_model("model/model_datapelamar.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template( "upload.html")
    elif request.method == "POST":
        excel_file = request.files.get("file")
        X_test = pd.read_excel(excel_file)
        X_test["Tahapan"] = model.predict(X_test)
        return X_test.to_html()

if __name__ == "__main__":
    app.run(debug=True)