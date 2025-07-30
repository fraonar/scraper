def validate_location_input(location):
    if not location or not isinstance(location, str):
        raise ValueError("Location must be a non-empty string.")

def load_config(file_path):
    import json
    with open(file_path, 'r') as config_file:
        return json.load(config_file)

def save_config(config, file_path):
    import json
    with open(file_path, 'w') as config_file:
        json.dump(config, config_file, indent=4)