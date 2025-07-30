def fetch_businesses(api_key, location, radius=5000):
    import requests

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": radius,
        "key": api_key,
        "type": "establishment"
    }

    businesses = []
    while True:
        response = requests.get(url, params=params)
        results = response.json().get('results', [])
        businesses.extend(results)

        # Check for next page token
        next_page_token = response.json().get('next_page_token')
        if not next_page_token:
            break

        params['pagetoken'] = next_page_token

    return businesses

def extract_business_details(business):
    details = {
        "name": business.get("name"),
        "phone_number": business.get("formatted_phone_number"),
        "address": business.get("vicinity"),
        "website": business.get("website")
    }
    return details

def get_businesses(api_key, location):
    businesses = fetch_businesses(api_key, location)
    business_details = [extract_business_details(biz) for biz in businesses]
    return business_details