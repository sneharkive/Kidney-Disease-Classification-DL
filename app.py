from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline



os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

clApp = ClientApp()

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')




# @app.route("/train", methods=['GET','POST'])
# @cross_origin()
# def trainRoute():
#     # os.system("python main.py")
#     os.system("dvc repro")
#     return "Training done successfully!"



# @app.route("/predict", methods=['POST'])
# @cross_origin()
# def predictRoute():
#     # image = request.json['image']
#     try:
#         data = request.get_json()
#
#         if data is None or 'image' not in data:
#             return jsonify({"error": "No image found in request"}), 400
#
#         image = data['image']
#
#         decodeImage(image, clApp.filename)
#         result = clApp.classifier.predict()
#         return jsonify(result)
#     except Exception as e:
#         return jsonify({
#             "error": str(e)
#         }), 500


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        # Case 1: JSON (Base64)
        data = request.get_json(silent=True)
        if data and "image" in data:
            image = data["image"]
            decodeImage(image, clApp.filename)

        # Case 2: File upload (form-data)
        elif "file" in request.files:
            file = request.files["file"]
            file.save(clApp.filename)

        else:
            return jsonify({"error": "No image provided"}), 400

        result = clApp.classifier.predict()
        return jsonify(result)

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

