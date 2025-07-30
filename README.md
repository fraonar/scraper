# Maps and Yelp Scraper

This project is a web scraper that collects business information from Google Maps Places API and Yelp for a specified location. The scraper gathers details such as business name, phone number, address, and website, while filtering out businesses that already have a website. The results can be exported to an Excel file or a Google Sheet.

## Project Structure

```
maps-yelp-scraper
├── src
│   ├── main.py                # Entry point of the application
│   ├── google_maps_api.py     # Functions to interact with Google Places API
│   ├── yelp_scraper.py        # Web scraping logic for Yelp
│   ├── filters.py             # Functions to filter businesses without a website
│   ├── excel_writer.py        # Export filtered data to Excel
│   ├── google_sheets_writer.py # Push filtered data to Google Sheets
│   └── utils.py               # Utility functions
├── requirements.txt           # Required libraries
├── .gitignore                 # Files to ignore by Git
└── README.md                  # Project overview and setup instructions
```

## Setup Instructions

1. **Obtain API Key**:
   - For Google Maps Places API, you need to create a project in the Google Cloud Console and enable the Places API. Generate an API key and restrict it as necessary.

2. **Install Required Libraries**:
   - Navigate to the project directory and install the required libraries using pip:
     ```
     pip install -r requirements.txt
     ```

3. **Run the Scraper**:
   - Execute the main script to start the scraping process:
     ```
     python src/main.py
     ```

## Functionalities

- **Google Maps Integration**: Fetches business details based on location using the Google Places API.
- **Yelp Scraping**: Scrapes business information from Yelp using BeautifulSoup and Selenium.
- **Data Filtering**: Filters out businesses that already have a website.
- **Data Export**: Exports the filtered data to an Excel file or pushes it to Google Sheets.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or bug fixes.
