from flask import Flask, render_template, request, jsonify
from disaster_types import DISASTER_TYPES
from disaster_descriptions import DISASTER_DESCRIPTIONS

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_categories", methods=["GET"])
def get_categories():
    return jsonify({"categories": list(DISASTER_TYPES.keys())})

@app.route("/get_subcategories", methods=["POST"])
def get_subcategories():
    category = request.json.get("category")
    subcategories = DISASTER_TYPES.get(category, [])
    return jsonify({"subcategories": subcategories})

@app.route("/get_description", methods=["POST"])
def get_description():
    subcategory = request.json.get("subcategory")
    for category, items in DISASTER_DESCRIPTIONS.items():
        if subcategory in items:
            return jsonify({"description": items[subcategory]})
    return jsonify({"description": "No description available."})

if __name__ == "__main__":
    app.run(debug=True)
