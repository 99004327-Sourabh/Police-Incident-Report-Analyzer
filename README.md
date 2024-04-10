# Police Incident Report Analyzer

## Introduction

The Police Incident Report Analyzer is a cutting-edge Python application developed as part of the CIS 6930 course assignment for Spring 2024. This tool is meticulously designed to automate the extraction and augmentation of data from police incident reports, which are publicly available but often disseminated in less accessible PDF formats. By leveraging advanced programming techniques and state-of-the-art libraries, this project aims to transform raw data into a structured, enriched format ideal for downstream data analysis tasks. The augmentation process incorporates additional data dimensions such as weather conditions, geographical insights, and temporal analysis, all while maintaining a keen awareness of fairness and bias mitigation in data processing.

## Project Scope

This tool is pivotal for researchers, data scientists, and public safety officials who seek to derive actionable insights from incident reports. It enriches the data with contextual information that can significantly impact the interpretation and analysis of incidents, thus facilitating a more nuanced understanding of public safety patterns.

## Features and Functionalities

- **PDF Data Extraction**: Utilizes `pypdf` for robust extraction of text from PDF files containing incident reports.
- **Data Augmentation**: Enriches incidents with weather conditions using the `requests` library to access weather data, and employs `geopy` for geographical calculations.
- **Command-line Interface**: Offers a simple yet powerful CLI for easy operation by end-users, making it highly accessible for diverse user demographics.

## Detailed Function Descriptions

- **`get_weather_code(date_time, latitude, longitude)`**: Connects to the Open-Meteo API to retrieve historical weather conditions based on the incident's date and location. This function is essential for understanding environmental factors that may influence incident rates.

- **`calculate_bearing(pointA, pointB)`**: Calculates the geographical bearing from one point to another, aiding in the determination of the incident's relative direction from the town center. This function utilizes mathematical formulas to ensure accuracy in directional analysis.

- **`calculate_side_of_town(location)`**: Determines the incident's cardinal direction (N, S, E, W, NE, NW, SE, SW) relative to the town's center. This categorization is crucial for spatial analysis and understanding regional incident distributions.

- **`get_location_coordinates(address)`**: Converts physical addresses into geographical coordinates (latitude and longitude) using `Nominatim` from the `geopy` library. This function is fundamental for all subsequent geographical computations.

- **`fetch_incidents(urls)`**: Downloads and reads PDF files from a list of URLs, acting as the initial data ingestion step in the pipeline.

- **`extract_text_from_pdf(rawPDF)`**: Parses text from PDF documents, transforming unstructured PDF data into a structured textual format suitable for further processing.

- **`parse_line_to_incident(line)`**: Interprets individual lines of text extracted from PDFs, organizing them into structured records of incidents.

- **`extractincidents(rawPDF)`**: A wrapper function that employs `extract_text_from_pdf` and `parse_line_to_incident` to streamline the extraction process.

- **`augment_data(incidents)`**: The core function where data augmentation occurs, enriching incident records with additional context such as weather, location ranking, and side of town. This function embodies the essence of the project, transforming raw data into a rich dataset ready for analysis.

- **`print_augmented_data(augmented_incidents)`**: Outputs the augmented incident data to the console in a tab-separated format, making the data easily redirectable to a file or other tools for further analysis.

## Installation and Setup

1. **Clone the Repository**: Start by cloning the project repository to your local machine.
2. **Install Python 3.x**: Ensure Python 3.x is installed. This project is developed and tested with Python 3.x, leveraging its advanced features and libraries.
3. **Install Dependencies**: Navigate to the project directory and install required dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```
    This command installs all the necessary libraries, including `pypdf`, `geopy`, `requests`, and `argparse`, ensuring the tool functions as intended.


4. **Prepare URLs File**: Create a CSV file containing URLs of incident reports, with each URL on a separate line. Ensure the CSV file has a header row specifying the column names.

5. **Run the Program**: Execute the following command in your terminal, replacing `<your_urls_file.csv>` with the path to your CSV file containing URLs of incident reports:
    ```bash
    python assignment2.py --urls your_urls_file.csv
    ```

    Upon execution, the program will fetch incident reports from the provided URLs, extract relevant data, augment it with additional information, and print the augmented data to the console.



## Assumptions

- The incident reports are assumed to be in PDF format.
- The URLs provided in the CSV file are assumed to lead to valid incident report documents.
- The Open-Meteo API is assumed to be accessible and provides accurate weather data.
- The geocoding service (Nominatim) is assumed to be accessible and provides accurate coordinates for addresses.

## Bugs

- A ReadTimeoutError may occur during geocoding due to network issues or timeouts.
- ValueError may occur during date and time parsing if the format is not as expected in the incident reports.

Feel free to reach out for any further assistance or clarification.
# cis6930sp24-assignment2
