import re
import argparse
import math
import requests
import urllib.request
from pypdf import PdfReader
from io import BytesIO
from datetime import datetime
from geopy.distance import distance
from geopy.geocoders import Nominatim
from collections import Counter
from geopy.distance import great_circle


#gievn ones :  
CENTER_OF_TOWN = (35.220833, -97.443611)

def get_weather_code(date_time, latitude, longitude):
    # """
    # Retrieves weather code for a specific date and location from the Open-Meteo API.

    # Parameters:
    # - date_time: The datetime object for which weather data is sought.
    # - latitude: The latitude of the location.
    # - longitude: The longitude of the location.

    # Returns:
    # - The weather code as an integer if available; otherwise, None.
    # """

    # Format the date as required by the Open-Meteo API.
    date_str = date_time.strftime('%Y-%m-%d')
    # Construct the API request URL.
    url = f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={date_str}&end_date={date_str}&daily=weather_code"
    # Make the request to the Open-Meteo API.
    response = requests.get(url)
    # Check if the request was successful.
    if response.status_code == 200:
        # Extract the JSON data from the response.
        data = response.json()
        # Extract the weather codes list from the data.
        weather_codes = data.get('daily', {}).get('weather_code', [])
        # Return the first weather code if the list is not empty.
        if weather_codes:
            return weather_codes[0]

    # Return None if no weather code could be retrieved.
    return None




def calculate_bearing(pointA, pointB):
    # """
    # Calculates the bearing from point A to point B.

    # Parameters:
    # - pointA: A tuple containing the latitude and longitude of the first point (lat, lon).
    # - pointB: A tuple containing the latitude and longitude of the second point (lat, lon).

    # Returns:
    # - The bearing in degrees from point A to point B, a float value between 0 and 360.

    # The formula used for calculation is based on spherical trigonometry to find the bearing between two points on the surface of a sphere.
    # """
    
    # Convert latitude and longitude from degrees to radians for both points.
    lat1, lon1 = math.radians(pointA[0]), math.radians(pointA[1])
    lat2, lon2 = math.radians(pointB[0]), math.radians(pointB[1])
    
    # Compute the change in coordinates.
    delta_lon = lon2 - lon1
    
    # Calculate the bearing using the formula.
    x = math.cos(lat2) * math.sin(delta_lon)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)
    
    # Calculate the initial bearing from point A to point B, convert from radians to degrees.
    bearing = math.atan2(x, y)
    bearing_degrees = math.degrees(bearing)
    
    # Normalize the bearing to ensure it falls within 0-360 degrees.
    normalized_bearing = (bearing_degrees + 360) % 360
    
    return normalized_bearing


def calculate_side_of_town(location):
    # """
    # Determines the cardinal or intercardinal direction of a given location relative to the center of town.

    # Parameters:
    # - location: A tuple containing the latitude and longitude of the location (lat, lon).

    # Returns:
    # - A string representing the cardinal or intercardinal direction (N, NE, E, SE, S, SW, W, NW) of the location relative to the town's center. If the location is None, returns "Unknown".

    # This function first calculates the bearing from the center of town to the given location using the calculate_bearing function. It then categorizes the bearing into one of the eight cardinal or intercardinal directions based on its value.
    # """
    
    # Return "Unknown" if the location is not provided.
    if location is None:
        return "Unknown"

    # Calculate the bearing from the center of town to the given location.
    bearing = calculate_bearing(CENTER_OF_TOWN, location)

    # Determine the direction based on the bearing's value.
    if 0 <= bearing < 22.5 or 337.5 <= bearing <= 360:
        return "N"  # North
    elif 22.5 <= bearing < 67.5:
        return "NE"  # Northeast
    elif 67.5 <= bearing < 112.5:
        return "E"  # East
    elif 112.5 <= bearing < 157.5:
        return "SE"  # Southeast
    elif 157.5 <= bearing < 202.5:
        return "S"  # South
    elif 202.5 <= bearing < 247.5:
        return "SW"  # Southwest
    elif 247.5 <= bearing < 292.5:
        return "W"  # West
    else:  # 292.5 <= bearing < 337.5
        return "NW"  # Northwest

    # This categorization helps in understanding the geographical orientation of the location relative to the center of the town, which can be useful for navigational purposes or spatial analysis.

def get_location_coordinates(address):
    # print(address)
    geolocator = Nominatim(user_agent="my_specific_geocoding_app")
    try:
        # Increase the timeout value to avoid ReadTimeoutError
        location = geolocator.geocode(address, timeout=10)  # Timeout increased to 10 seconds
        if location:
            # print(location.latitude, location.longitude)
            return (location.latitude, location.longitude)
        else:
            return None
    except Exception as e:
        # print(f"Error geocoding '{address}': {e}")
        return None

def fetch_incidents(urls):
    incidents_data = []
    for url in urls:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          

            data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()    
            incidents_data.append(data)
    return incidents_data

def extract_text_from_pdf(rawPDF):
    pdf_data = PdfReader(BytesIO(rawPDF))
    all_lines = []
    for page in pdf_data.pages:
        text = page.extract_text(extraction_mode="layout")
        lines = text.split("\n")
        all_lines.extend(lines)
    return all_lines

def parse_line_to_incident(line):
    # Splitting line into components and stripping whitespace
    components = re.split(r'\s{2,}', line.strip())
    # Handling different lengths of components
    if len(components) == 5:
        return tuple(components)
    elif len(components) == 3:
        return components[0], components[1], "", "", components[2]
    else:
        return None

def parse_incident_lines(lines):
    extracted_data = []
    for line in lines:
        # Skipping header or footer lines
        if line.startswith("    "):
            continue
        incident = parse_line_to_incident(line)
        if incident:
            extracted_data.append(incident)
            print("incident",incident)
    return extracted_data

def extractincidents(rawPDF):
    lines = extract_text_from_pdf(rawPDF)
    return parse_incident_lines(lines)

def augment_data(incidents):
    augmented_incidents = []
    location_counts = Counter(incident[2] for incident in incidents)
    nature_counts = Counter(incident[3] for incident in incidents)

    # Pre-calculate rankings
    location_rank = {loc: rank+1 for rank, (loc, _) in enumerate(location_counts.most_common())}
    nature_rank = {nature: rank+1 for rank, (nature, _) in enumerate(nature_counts.most_common())}

    for incident in incidents:
        date_time_str, incident_number, location, nature, incident_ori = incident
        try:
                # Adjust the format to include time parsing
            date_time = datetime.strptime(date_time_str, "%m/%d/%Y %H:%M")
        except ValueError as e:
            print(f"Error parsing date and time: {e}")
            continue  # Skip this incident or handle error appropriately
    
        coordinates = get_location_coordinates(location)
        weather_code = get_weather_code(date_time, *coordinates) if coordinates else None
        side_of_town = calculate_side_of_town(coordinates) if coordinates else "Unknown"

        # Check if the incident is EMS related based on Incident ORI
        ems_stat = (incident_ori == "EMSSTAT")

        # Calculating day of the week (1=Monday, 7=Sunday)
        day_of_week = date_time.isoweekday()
        # Extracting the hour for the time of day
        time_of_day = date_time.hour
        # print("time", time_of_day)
        
        augmented_incidents.append(
            (day_of_week, time_of_day, weather_code, location_rank.get(location, 0), side_of_town, nature, nature_rank.get(nature, 0), ems_stat)
        )

    return augmented_incidents


def print_augmented_data(augmented_incidents):
    #Print the augmented data to stdout in the specified format.
    for incident in augmented_incidents:
        print("\t".join(map(str, incident)))

def main(urls_file):
    #Main function to orchestrate the fetching, extraction, and augmentation process.
    # Read URLs from the provided file
    with open(urls_file, 'r') as f:
        urls = [line.strip() for line in f.readlines()]
    
    # Fetch and extract data from each PDF
    raw_incidents_data = fetch_incidents(urls)
    incidents = []  # This should be populated with the extracted incident data
    
    # For each raw PDF data, extract incidents and perform augmentation
    for raw_data in raw_incidents_data:
        pdf_incidents = extractincidents(raw_data)
        incidents.extend(pdf_incidents)
    
    augmented_incidents = augment_data(incidents)
    
    # Print the augmented data
    print_augmented_data(augmented_incidents)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Data augmentation for incident reports.")
    parser.add_argument("--urls", type=str, required=True, help="File containing URLs of incident reports.")
    
    args = parser.parse_args()
    main(args.urls)


