from flask import Flask, request, jsonify
import nltk
from pyresparser import ResumeParser
import os

nltk.download("stopwords")

app = Flask(__name__)


@app.route("/parse_resume", methods=["POST"])
def parse_resume():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(os.getcwd(), file.filename)
    file.save(file_path)

    try:
        data = ResumeParser(file_path).get_extracted_data()
        os.remove(file_path)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
