from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Resource data for all main buttons and sub-buttons
RESOURCES = {
    # FIRE
    "HOUSE FIRE": "Call 911 immediately and evacuate. Stay outside until cleared by authorities.",
    "FOREST FIRE": "Evacuate following emergency instructions. Avoid inhaling smoke.",
    "ELECTRICAL FIRE": "Turn off the power source if safe. Use a fire extinguisher designed for electrical fires.",
    "VEHICLE FIRE": "Exit the vehicle immediately and move to safety. Call 911.",
    "INDUSTRIAL FIRE": "Follow workplace safety protocols and evacuate to designated areas.",

    # MEDICAL EMERGENCY
    "HEART ATTACK": "Symptoms include chest pain and shortness of breath. Call 911 immediately.",
    "STROKE": "Remember FAST: Face drooping, Arm weakness, Speech difficulty, Time to call 911.",
    "SEVERE INJURY": "Apply pressure to bleeding wounds and keep the injured person still. Call 911.",
    "ALLERGIC REACTION": "Symptoms include swelling and difficulty breathing. Use an EpiPen if available and call 911.",
    "SEIZURE": "Clear the area of hazards. Do not restrain the person. Call for help if it lasts more than 5 minutes.",
    "BREATHING DIFFICULTY": "Administer prescribed medications if available. Call 911.",
    "POISONING": "Call Poison Control at 1-800-222-1222 or seek emergency help immediately.",

    # HUNGRY
    "FOOD INSECURITY": "Contact local food banks for assistance.",
    "LACK OF ACCESS TO MEALS": "Seek programs offering free meals or community support.",
    "MALNUTRITION": "Consult healthcare providers for nutrition-related programs.",
    "EMERGENCY FOOD SUPPLIES": "Locate emergency distribution centers for immediate aid.",

    # DOMESTIC VIOLENCE
    "PHYSICAL ABUSE": "Physical abuse involves bodily harm. Call 911 or a support hotline for immediate help.",
    "EMOTIONAL ABUSE": "Emotional abuse may involve manipulation or control. Counseling services are available.",
    "FINANCIAL ABUSE": "Financial abuse involves controlling someone's access to financial resources. Seek advocacy support.",
    "SEXUAL ABUSE": "Sexual abuse requires immediate attention. Contact a sexual assault hotline for confidential assistance.",
    "COERCIVE CONTROL": "Coercive control includes patterns of behavior that dominate or exploit. Plan a safe exit strategy.",

    # CRIME OR SAFETY ISSUE
    "ASSAULT": "Assault includes physical attacks. Seek medical help and contact authorities.",
    "BURGLARY": "Burglary involves unauthorized entry. File a police report and avoid disturbing the scene.",
    "THEFT": "Theft involves stolen property. Report incidents to law enforcement.",
    "VANDALISM": "Vandalism includes property damage. Document the damage and report it to authorities.",
    "ACTIVE SHOOTER": "In an active shooter situation, run, hide, and fight as a last resort. Call 911.",
    "KIDNAPPING": "Report missing persons or suspected abductions to law enforcement immediately.",
    "STALKING": "Stalking involves repeated harassment. Document incidents and contact authorities.",

    # MENTAL HEALTH CRISIS
    "SUICIDAL THOUGHTS": "If someone is suicidal, call 988 or a suicide prevention hotline immediately.",
    "ANXIETY ATTACK": "Encourage slow, deep breaths and provide a calm environment.",
    "SEVERE DEPRESSION": "Severe depression can require immediate intervention. Contact a counselor or hotline.",
    "PSYCHOTIC EPISODE": "Psychotic episodes may involve hallucinations or delusions. Call 911 if safety is a concern.",
    "SUBSTANCE ABUSE CRISIS": "Substance abuse crises require urgent care. Contact a substance abuse hotline.",
    "PTSD EPISODE": "Post-traumatic stress episodes can be alleviated with grounding techniques and professional help.",

    # I'M LOST
    "LOST IN A CITY": "Use GPS or public transportation apps to find your way.",
    "LOST IN THE WILDERNESS": "Stay in one place and make yourself visible to rescuers.",
    "LOST ON PUBLIC TRANSIT": "Contact transit staff or use station maps for guidance.",
    "LOST WHILE TRAVELING ABROAD": "Reach out to local embassies or law enforcement for assistance."
}

# Helper function to simulate GPS location retrieval
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
    
    # Example: Append GPS location for specific events
    if event_name in ["HOUSE FIRE", "FOREST FIRE", "VEHICLE FIRE"]:
        coordinates = get_location()
        response += f" Coordinates: {coordinates}"
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
