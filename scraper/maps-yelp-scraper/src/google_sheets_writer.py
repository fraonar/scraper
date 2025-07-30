def push_to_google_sheets(data, spreadsheet_id, range_name, credentials_file):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    # Set up the credentials and client
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(creds)

    # Open the Google Sheet
    sheet = client.open_by_key(spreadsheet_id).sheet1

    # Clear existing content
    sheet.clear()

    # Prepare data for insertion
    headers = ["Business Name", "Phone Number", "Address", "Website"]
    sheet.append_row(headers)

    for business in data:
        row = [
            business.get("name"),
            business.get("phone_number"),
            business.get("address"),
            business.get("website")
        ]
        sheet.append_row(row)