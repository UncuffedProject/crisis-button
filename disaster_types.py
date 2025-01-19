# Import disaster names and descriptions
from natural_disaster_names import (
    geological_disasters,
    hydrological_disasters,
    meteorological_disasters,
    climatological_disasters,
    biological_disasters,
    space_related_disasters,
    other_disasters
)
from natural_disaster_descriptions import (
    geological_disasters as geo_desc,
    hydrological_disasters as hydro_desc,
    meteorological_disasters as meteo_desc,
    climatological_disasters as climate_desc,
    biological_disasters as bio_desc,
    space_related_disasters as space_desc,
    other_disasters as other_desc
)

# Comprehensive list of all crisis events categorized
DISASTER_TYPES = {
    "Natural Disasters": {
        "Geological Disasters": {name: geo_desc.get(name, "Natural disasters caused by processes occurring within the Earth's crust, such as earthquakes, volcanic eruptions, and landslides.") for name in geological_disasters},
        "Hydrological Disasters": {name: hydro_desc.get(name, "Disasters associated with water movement, including floods, flash floods, and storm surges, often caused by excessive precipitation or rising water levels.") for name in hydrological_disasters},
        "Meteorological Disasters": {name: meteo_desc.get(name, "Weather-related disasters caused by atmospheric processes, including hurricanes, tornadoes, and severe thunderstorms.") for name in meteorological_disasters},
        "Climatological Disasters": {name: climate_desc.get(name, "Disasters linked to long-term climate patterns, such as droughts, wildfires, and heatwaves, often influenced by global warming or seasonal anomalies.") for name in climatological_disasters},
        "Biological Disasters": {name: bio_desc.get(name, "Disasters caused by biological factors, such as pandemics, locust swarms, or algal blooms, which threaten human health, agriculture, or ecosystems.") for name in biological_disasters},
        "Space-Related Disasters": {name: space_desc.get(name, "Disasters originating from outer space, including asteroid impacts, solar storms, or other celestial events impacting Earth.") for name in space_related_disasters},
        "Other Disasters": {name: other_desc.get(name, "Miscellaneous disasters that do not fit traditional categories, such as dust storms, sandstorms, or glacial outburst floods.") for name in other_disasters}
    },
    "Man-Made Disasters": [
        "Crime", "Arson", "Civil Disorder", "Terrorism", "War", "Chemical Spills", "Oil Spills",
        "Biological Threats", "Cyber Attacks", "Nuclear Incidents", "Structural Collapse"
    ],
    "Medical Emergencies": [
        "Heart Attack", "Stroke", "Severe Injury", "Allergic Reaction", "Seizure",
        "Breathing Difficulty", "Poisoning", "Overdose", "Heat Stroke", "Hypothermia"
    ],
    "Mental Health Crises": [
        "Suicidal Thoughts", "Severe Depression", "Anxiety Attack", "PTSD Episode",
        "Psychotic Episode", "Substance Abuse Crisis", "Eating Disorders"
    ],
    "Domestic and Interpersonal Violence": [
        "Physical Abuse", "Emotional Abuse", "Financial Abuse", "Sexual Abuse",
        "Coercive Control", "Elder Abuse", "Child Abuse", "Stalking", "Human Trafficking"
    ],
    "Homelessness and Housing Crises": [
        "Chronic Homelessness", "Transitional Homelessness", "Episodic Homelessness",
        "Hidden Homelessness", "Family Homelessness", "Youth Homelessness",
        "Veteran Homelessness", "Housing Displacement (e.g., Eviction)"
    ],
    "Food and Basic Needs": [
        "Food Insecurity", "Malnutrition", "Lack of Access to Meals",
        "Emergency Food Supplies", "Water Shortages"
    ],
    "Safety and Security Issues": [
        "Assault", "Burglary", "Theft", "Vandalism", "Active Shooter",
        "Kidnapping", "Hostage Situation"
    ],
    "Lost or Missing Persons": [
        "Lost in a City", "Lost in the Wilderness", "Lost While Traveling Abroad",
        "Lost on Public Transit"
    ],
    "Community and Social Crises": [
        "Riots", "Public Health Epidemics", "Pandemics", "Mass Casualty Incidents",
        "Refugee Crises", "Forced Evacuations"
    ],
    "Technological and Infrastructure Failures": [
        "Power Outage", "Communication Breakdown", "Internet Blackouts",
        "Transportation Accidents", "Dam Failures", "Data Breaches"
    ],
    "Workplace Crises": [
        "Workplace Violence", "Layoffs or Job Loss", "Sexual Harassment",
        "Discrimination", "Unsafe Working Conditions"
    ],
    "Educational Crises": [
        "School Shootings", "Bullying", "Teacher Strikes", "Student Mental Health Crises"
    ],
    "Environmental Crises": [
        "Pollution", "Deforestation", "Habitat Loss", "Animal Extinction",
        "Climate Change-Related Events"
    ],
    "Financial Crises": [
        "Bankruptcy", "Foreclosure", "Job Loss", "Debt Crisis", "Lack of Financial Support"
    ],
    "Personal Crises": [
        "Divorce", "Death of a Loved One", "Sudden Illness", "Family Conflict",
        "Legal Troubles"
    ]
}

if __name__ == "__main__":
    # Test print the natural disasters section
    print("Natural Disasters:")
    for category, disasters in DISASTER_TYPES["Natural Disasters"].items():
        print(f"\n{category}:")
        for name, description in disasters.items():
            print(f"  - {name}: {description}")
