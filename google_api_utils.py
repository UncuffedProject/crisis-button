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
    # Step 1: Perform a Text Search to get the place_id
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
        place_id = place.get("place_id")
        address = place.get("formatted_address", "Address not available")

        # Step 2: If place_id is available, fetch additional details
        if place_id:
            details_url = "https://maps.googleapis.com/maps/api/place/details/json"
            details_params = {
                "place_id": place_id,
                "fields": "formatted_address,formatted_phone_number,website",
                "key": GOOGLE_API_KEY,
            }
            details_response = requests.get(details_url, params=details_params)
            details_data = details_response.json()

            if details_response.status_code == 200 and details_data.get("result"):
                details = details_data["result"]
                return {
                    "address": details.get("formatted_address", address),
                    "phone": details.get("formatted_phone_number", "Phone not available"),
                    "website": details.get("website", "Website not available"),
                }

        # Fallback if no details are found
        return {
            "address": address,
            "phone": "Phone not available",
            "website": "Website not available",
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

import requests
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def geocode_location(location):
    """
    Geocodes a user-provided location into latitude and longitude using the Google Geocoding API.
    """
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": location, "key": GOOGLE_API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            return data["results"][0]["geometry"]["location"]
    return None
