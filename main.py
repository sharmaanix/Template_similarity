import os
import cv2
import numpy as np
from flask import Flask, request, jsonify
from src.preprocessing import segment_image, match_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def test():
    return "API Working"


@app.route("/match", methods=["GET"])
def similar_template():
    test_image_path = request.args["image_path"]
    TEMPLATE_DIR = request.args["template_folder_path"]
    template_image_file = [
        os.path.join(TEMPLATE_DIR, item) for item in os.listdir(TEMPLATE_DIR)
    ]

    image_segment = segment_image(test_image_path).compute()
    template_score = []
    template_name = []
    for template_image in template_image_file:
        template = cv2.imread(template_image)
        gray_image = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        cumul_point = 0
        for segment in image_segment:
            cumul_point = cumul_point + match_template(
                segment,
                gray_image).compute()
        template_score.append(cumul_point)
        template_name.append(template_image)

    output = {
        "input_filename": test_image_path,
        "template_file_name": template_name[np.argmax(template_score)],
    }
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
