from .natural_disaster_descriptions import geological_disasters, hydrological_disasters, meteorological_disasters, climatological_disasters, biological_disasters, space_related_disasters, other_disasters
from .man_made_disaster_descriptions import industrial_disasters, transportation_disasters, structural_failures, environmental_disasters, fires_and_explosions, war_and_conflict, cyber_and_technological_disasters, health_and_biological_disasters
from .medical_emergency_descriptions import cardiovascular_emergencies, respiratory_emergencies, neurological_emergencies, trauma_related_emergencies, toxicological_emergencies, metabolic_emergencies, obstetric_gynecological_emergencies
from .mental_health_crisis_descriptions import mood_disorders, anxiety_disorders, psychotic_disorders, personality_disorders, behavioral_and_developmental_disorders, substance_related_crises, suicidal_and_self_harm_crises, eating_disorders, other_mental_health_crises

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
