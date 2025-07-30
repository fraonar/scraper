# main.py

import pandas as pd
from google_maps_api import fetch_businesses_from_google_maps
from yelp_scraper import scrape_yelp_businesses
from filters import filter_businesses_without_website
from excel_writer import export_to_excel
from google_sheets_writer import export_to_google_sheets

def main():
    location = input("Enter the location to search for businesses: ")
    
    # Fetch businesses from Google Maps
    google_businesses = fetch_businesses_from_google_maps(location)
    
    # Scrape businesses from Yelp
    yelp_businesses = scrape_yelp_businesses(location)
    
    # Combine results
    all_businesses = google_businesses + yelp_businesses
    
    # Filter out businesses with websites
    filtered_businesses = filter_businesses_without_website(all_businesses)
    
    # Export results to Excel
    export_to_excel(filtered_businesses, 'filtered_businesses.xlsx')
    
    # Optionally, export results to Google Sheets
    export_to_google_sheets(filtered_businesses)

if __name__ == "__main__":
    main()