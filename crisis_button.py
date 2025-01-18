from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Resource data for main buttons and sub-buttons
RESOURCES = {
    # FIRE
    "HOUSE FIRE": "Call 911 immediately and evacuate the building. Do not use elevators.",
    "FOREST FIRE": "Evacuate the area following local emergency services. Avoid inhaling smoke.",
    "ELECTRICAL FIRE": "Disconnect the power source if safe. Use a fire extinguisher rated for electrical fires.",
    "VEHICLE FIRE": "Exit the vehicle and move a safe distance away. Call 911.",
    "INDUSTRIAL FIRE": "Follow workplace evacuation procedures and call emergency services.",

    # MEDICAL EMERGENCY
    "HEART ATTACK": "Call 911 immediately. Chew and swallow aspirin unless allergic.",
    "STROKE": "Call 911 immediately. Note the time symptoms started.",
    "SEVERE INJURY": "Apply pressure to bleeding wounds and call 911.",
    "ALLERGIC REACTION": "Use an EpiPen if available and call emergency services.",
    "SEIZURE": "Ensure the person is safe. Do not restrain them. Call for help if it lasts over 5 minutes.",
    "BREATHING DIFFICULTY": "Call 911 and assist with prescribed medication if available.",
    "POISONING": "Call Poison Control at 1-800-222-1222 or 911.",

    # HUNGRY
    "FOOD INSECURITY": "Contact local food banks or community kitchens for assistance.",
    "LACK OF ACCESS TO MEALS": "Seek programs offering free or subsidized meals.",
    "MALNUTRITION": "Contact healthcare providers for nutrition programs.",
    "EMERGENCY FOOD SUPPLIES": "Locate emergency distribution centers for immediate aid.",

    # DOMESTIC VIOLENCE
    "PHYSICAL ABUSE": "Call 911 or the National Domestic Violence Hotline at 800-799-7233.",
    "EMOTIONAL ABUSE": "Seek support groups or counseling services.",
    "FINANCIAL ABUSE": "Contact local advocacy organizations for help.",
    "SEXUAL ABUSE": "Call 911 or a sexual assault hotline for confidential assistance.",
    "COERCIVE CONTROL": "Plan a safe exit strategy with local support groups.",

    # CRIME OR SAFETY ISSUE
    "ASSAULT": "Call 911 and seek medical attention if needed.",
    "BURGLARY": "Report the incident to law enforcement. Do not enter the property.",
    "THEFT": "Report stolen items to the police. Document losses for insurance claims.",
    "VANDALISM": "File a police report and document the damage.",
    "ACTIVE SHOOTER": "Run, hide, and fight as a last resort. Call 911 when safe.",
    "KIDNAPPING": "Contact law enforcement immediately. Provide as much detail as possible.",
    "STALKING": "Report the stalker to authorities. Keep records of incidents.",

    # MENTAL HEALTH CRISIS
    "SUICIDAL THOUGHTS": "Call 988 or a suicide hotline for immediate support.",
    "ANXIETY ATTACK": "Encourage breathing exercises and seek a calm environment.",
    "SEVERE DEPRESSION": "Connect with a mental health professional or hotline.",
    "PSYCHOTIC EPISODE": "Call 911 if safety is a concern. Avoid arguing with the individual.",
    "SUBSTANCE ABUSE CRISIS": "Seek immediate support from a substance abuse hotline or clinic.",
    "PTSD EPISODE": "Encourage grounding techniques and contact a counselor.",

    # I'M LOST
    "LOST IN A CITY": "Use GPS or ask for directions from authorities.",
    "LOST IN THE WILDERNESS": "Stay in one place and make yourself visible to rescuers.",
    "LOST ON PUBLIC TRANSIT": "Contact transit staff or use station maps.",
    "LOST WHILE TRAVELING ABROAD": "Reach out to local embassies or law enforcement for help."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/handle_crisis", methods=["POST"])
def handle_crisis():
    event_name = request.json.get("event_name", "").upper()
    response = RESOURCES.get(event_name, "No specific response available.")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
