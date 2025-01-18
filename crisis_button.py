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

    def find_description(category_data, target):
        if isinstance(category_data, dict):
            for key, value in category_data.items():
                if key == target:
                    return value
                elif isinstance(value, dict):
                    result = find_description(value, target)
                    if result:
                        return result
        return None

    description = find_description(DISASTER_TYPES, subcategory)
    return jsonify({"description": description or "No description available."})

@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

if __name__ == "__main__":
    app.run(debug=True)
