import requests
import os

# Fetch API Key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

def get_location_name(latitude, longitude):
    """
    Converts GPS coordinates to a human-readable location using Google Geocoding API.
    """
    geocoding_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "latlng": f"{latitude},{longitude}",
        "key": GOOGLE_API_KEY,
    }
    response = requests.get(geocoding_url, params=params)
    data = response.json()

    if response.status_code == 200 and data.get("results"):
        address_components = data["results"][0]["address_components"]
        locality = next(
            (comp["long_name"] for comp in address_components if "locality" in comp["types"]), None
        )
        state = next(
            (comp["long_name"] for comp in address_components if "administrative_area_level_1" in comp["types"]), None
        )
        return f"{locality}, {state}" if locality and state else data["results"][0]["formatted_address"]
    return None

def get_place_details(place_name, location):
    """
    Fetch place details such as address, phone, and website using Google Places API.
    """
    places_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": place_name,
        "location": location,
        "key": GOOGLE_API_KEY,
    }
    response = requests.get(places_url, params=params)
    data = response.json()

    if response.status_code == 200 and data.get("results"):
        place = data["results"][0]
        return {
            "address": place.get("formatted_address", "Address not available"),
            "phone": place.get("formatted_phone_number", "Phone not available"),
            "website": place.get("website", "Website not available"),
        }
    return {
        "address": "Address not available",
        "phone": "Phone not available",
        "website": "Website not available",
    }

def search_resources(query, location_name):
    """
    Use Google Custom Search API to find resources.
    """
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": f"{query} resources near {location_name}",
        "num": 5,
    }
    response = requests.get(search_url, params=params)
    return response.json().get("items", [])
