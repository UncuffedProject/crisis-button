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
    if not category:
        return jsonify({"error": "Category not provided"}), 400

    subcategories = DISASTER_TYPES.get(category, {})
    if isinstance(subcategories, dict):  # Check if it's a nested dictionary
        return jsonify({"subcategories": list(subcategories.keys())})
    elif isinstance(subcategories, list):  # If it's already a flat list
        return jsonify({"subcategories": subcategories})
    else:
        return jsonify({"subcategories": []})  # Default empty list

@app.route("/get_description", methods=["POST"])
def get_description():
    subcategory = request.json.get("subcategory")
    if not subcategory:
        return jsonify({"error": "Subcategory not provided"}), 400

    def find_description(data, target):
        for key, value in data.items():
            if key == target:
                return value
            if isinstance(value, dict):
                result = find_description(value, target)
                if result:
                    return result
        return None

    description = find_description(DISASTER_DESCRIPTIONS, subcategory)
    return jsonify({"description": description or "No description available."})

@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

if __name__ == "__main__":
    app.run(debug=True)
