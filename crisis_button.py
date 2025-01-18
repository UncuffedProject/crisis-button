from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Resource data for various crisis events
RESOURCES = {
    "FIRE": "Emergency dispatched to your location!",
    "MEDICAL EMERGENCY": "Call 911 immediately or proceed to the nearest hospital.",
    "HUNGRY": "Local Food Bank: 123 Community Lane, Phone: 555-FOOD",
    "HOMELESSNESS": "Select the type of homelessness for tailored resources.",
    "DOMESTIC VIOLENCE": "National Domestic Violence Hotline: 800-799-7233",
    "CRIME OR SAFETY ISSUE": "Call local law enforcement or 911.",
    "MENTAL HEALTH CRISIS": "National Suicide Prevention Hotline: 988",
    "I'M LOST": "Contact local authorities or use navigation tools. For assistance, call 555-HELP."
}

# Simulate location retrieval (replace this with actual GPS for production)
def get_location():
    geolocator = Nominatim(user_agent="crisis_button_app")
    location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")  # Simulated location
    return f"{location.latitude}, {location.longitude}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/handle_crisis", methods=["POST"])
def handle_crisis():
    event_name = request.json.get("event_name", "").upper()
    response = RESOURCES.get(event_name, "No specific response available.")
    
    if event_name == "FIRE":
        coordinates = get_location()
        response += f"\nCoordinates: {coordinates}"
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
