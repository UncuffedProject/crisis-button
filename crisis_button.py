from flask import Flask, render_template, request, jsonify

from disasters.disaster_types import DISASTER_TYPES

from disasters.disaster_descriptions.natural_disaster_descriptions import geological_disasters, hydrological_disasters, meteorological_disasters, climatological_disasters, biological_disasters, space_related_disasters, other_disasters
from disasters.disaster_descriptions.man_made_disaster_descriptions import industrial_disasters, transportation_disasters, structural_failures, environmental_disasters, fires_and_explosions, war_and_conflict, cyber_and_technological_disasters, health_and_biological_disasters
from disasters.disaster_descriptions.medical_emergency_descriptions import cardiovascular_emergencies, respiratory_emergencies, neurological_emergencies, trauma_related_emergencies, toxicological_emergencies, metabolic_emergencies, obstetric_gynecological_emergencies
from disasters.disaster_descriptions.mental_health_crisis_descriptions import mood_disorders, anxiety_disorders, psychotic_disorders, personality_disorders, behavioral_and_developmental_disorders, substance_related_crises, suicidal_and_self_harm_crises, eating_disorders, other_mental_health_crises

import requests  # For making HTTP requests to external APIs

import os  # For accessing environment variables

# Fetch API Key and CSE ID from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

app = Flask(__name__)

DISASTER_DESCRIPTIONS = {
    "Natural Disasters": {
        "Geological Disasters": geological_disasters,
        "Hydrological Disasters": hydrological_disasters,
        "Meteorological Disasters": meteorological_disasters,
        "Climatological Disasters": climatological_disasters,
        "Biological Disasters": biological_disasters,
        "Space-Related Disasters": space_related_disasters,
        "Other Disasters": other_disasters,
    },
    "Man-Made Disasters": {
        "Industrial Disasters": industrial_disasters,
        "Transportation Disasters": transportation_disasters,
        "Structural Failures": structural_failures,
        "Environmental Disasters": environmental_disasters,
        "Fires and Explosions": fires_and_explosions,
        "War and Conflict": war_and_conflict,
        "Cyber and Technological Disasters": cyber_and_technological_disasters,
        "Health and Biological Disasters": health_and_biological_disasters,
    },
    "Medical Emergencies": {
        "Cardiovascular Emergencies": cardiovascular_emergencies,
        "Respiratory Emergencies": respiratory_emergencies,
        "Neurological Emergencies": neurological_emergencies,
        "Trauma-Related Emergencies": trauma_related_emergencies,
        "Toxicological Emergencies": toxicological_emergencies,
        "Metabolic Emergencies": metabolic_emergencies,
        "Obstetric/Gynecological Emergencies": obstetric_gynecological_emergencies,
    },
    "Mental Health Crises": {
        "Mood Disorders": mood_disorders,
        "Anxiety Disorders": anxiety_disorders,
        "Psychotic Disorders": psychotic_disorders,
        "Personality Disorders": personality_disorders,
        "Behavioral and Developmental Disorders": behavioral_and_developmental_disorders,
        "Substance-Related Crises": substance_related_crises,
        "Suicidal and Self-Harm Crises": suicidal_and_self_harm_crises,
        "Eating Disorders": eating_disorders,
        "Other Mental Health Crises": other_mental_health_crises,
    },
}

@app.route("/get_local_resources", methods=["POST"])
def get_local_resources():
    """
    Fetch local resources for a given disaster and location using Google Custom Search.
    """
    disaster = request.json.get("disaster")
    latitude = request.json.get("latitude")
    longitude = request.json.get("longitude")

    if not disaster or not latitude or not longitude:
        return jsonify({"error": "Missing required parameters"}), 400

    # Build the search query
    location = f"{latitude},{longitude}"
    query = f"local resources for {disaster} near {location}"
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": query,
        "num": 5
    }

    # Make the API request
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Google API Error:", response.text)  # Log the error
        return jsonify({"error": "Failed to fetch resources"}), 500

    search_results = response.json()
    print("Google API Response:", search_results)  # Log the full response

    resources = [{"name": item["title"], "link": item["link"]} for item in search_results.get("items", [])]
    return jsonify({"resources": resources})

@app.route("/")
def home():
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
    Endpoint to fetch the description for a specific subcategory.
    Looks up DISASTER_DESCRIPTIONS for matching entries.
    """
    subcategory = request.json.get("subcategory")
    if not subcategory:
        return jsonify({"error": "Subcategory not provided"}), 400

    # Search for description in DISASTER_DESCRIPTIONS
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

if __name__ == "__main__":
    app.run(debug=True)
