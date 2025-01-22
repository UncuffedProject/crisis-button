from flask import Flask, render_template, request, jsonify

import requests

from google_api_utils import get_location_name, get_place_details, search_resources, geocode_location, search_places

from disasters.disaster_types import DISASTER_TYPES
from disasters.disaster_descriptions import DISASTER_DESCRIPTIONS

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the main HTML page.
    """
    return render_template("index.html")

@app.route("/get_categories", methods=["GET"])
def get_categories():
    """
    Endpoint to fetch top-level categories (e.g., Natural Disasters, Medical Emergencies).
    """
    return jsonify({"categories": list(DISASTER_TYPES.keys())})

@app.route("/get_subcategories", methods=["POST"])
def get_subcategories():
    """
    Endpoint to fetch subcategories for a given category.
    Supports nested dictionaries or flat lists in DISASTER_TYPES.
    """
    category = request.json.get("category")
    if not category:
        return jsonify({"error": "Category not provided"}), 400

    # Navigate through DISASTER_TYPES to find subcategories
    def find_subcategories(data, target):
        if target in data:
            return data[target]
        for key, value in data.items():
            if isinstance(value, dict):
                result = find_subcategories(value, target)
                if result:
                    return result
        return None

    subcategories = find_subcategories(DISASTER_TYPES, category)
    if isinstance(subcategories, dict):  # Nested dictionary
        return jsonify({"subcategories": list(subcategories.keys())})
    elif isinstance(subcategories, list):  # Flat list
        return jsonify({"subcategories": subcategories})
    else:  # If no match found
        return jsonify({"subcategories": []})

@app.route("/get_description", methods=["POST"])
def get_description():
    """
    Endpoint to fetch the description for a specific subcategory and find local resources.
    """
    subcategory = request.json.get("subcategory")
    latitude = request.json.get("latitude")
    longitude = request.json.get("longitude")

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

    resources = []
    if latitude and longitude:
        location = f"{latitude},{longitude}"
        resources = search_places(subcategory, location)

    return jsonify({
        "description": description or "No description available.",
        "resources": resources
    })

@app.route("/geocode_location", methods=["POST"])
def geocode_location_endpoint():
    """
    Endpoint to convert a user-entered location into latitude and longitude.
    """
    location = request.json.get("location")
    if not location:
        return jsonify({"error": "Location not provided"}), 400

    coordinates = geocode_location(location)
    if not coordinates:
        return jsonify({"error": "Could not geocode location"}), 400

    return jsonify(coordinates)

if __name__ == "__main__":
    app.run(debug=True)
