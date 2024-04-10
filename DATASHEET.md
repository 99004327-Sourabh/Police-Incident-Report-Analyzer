# Datasheet for Incident Report Data

## Motivation

- **For what purpose was the dataset created?**  
  This dataset was created to analyze incidents reported in PDF formats, sourced from specific URLs. The primary goal is to augment the data with additional context such as weather conditions at the time of the incident and the geographical orientation relative to the town's center, aiming to provide richer insights for analytical purposes.

- **Who created the dataset and on behalf of which entity?**  
  The dataset creator and the entity behind it are not specified. This script is designed as a general tool for processing and augmenting incident report data.

- **Who funded the creation of the dataset?**  
  Funding information is not provided.

## Composition

- **What do the instances that comprise the dataset represent?**  
  Instances represent individual incidents, including details such as the date and time, location, nature of the incident, and additional augmented data like weather conditions and geographical direction from the town's center.

- **How many instances are there in total (and in each split, if applicable)?**  
  The total number of instances depends on the input URLs and the data they contain.

- **Does the dataset contain all possible instances or is it a sample?**  
  The dataset is a sample, dependent on the input URLs provided for incident reports in PDF format.

- **What data does each instance consist of?**  
  Each instance includes the incident date and time, incident number, location, nature, initial responding officer or entity (incident ORI), and augmented data such as weather code, side of town, etc.

- **Is there any missing information from individual instances?**  
  Information might be missing if the source PDFs do not contain it or if data augmentation processes (e.g., weather code retrieval, location geocoding) fail.

## Collection Process

- **How was the data associated with each instance acquired?**  
  Data is initially extracted from PDFs containing incident reports. It's then augmented with weather codes retrieved via the Open-Meteo API and geographical analysis using the `geopy` library.

- **Who was involved in the data collection process?**  
  The process is automated; involvement is limited to the individual or entity executing the script and providing URLs for the source PDFs.

## Preprocessing/cleaning/labeling

- **Was any preprocessing/cleaning/labeling of the data done?**  
  Yes, the script tokenizes the text extracted from PDFs, parses relevant incident data, and augments it with additional information like weather conditions and geographical direction.

- **Is the software used to preprocess/clean/label the instances available?**  
  The script itself serves as the preprocessing tool. It uses libraries such as `requests`, `urllib.request`, `pypdf`, `geopy`, and `datetime` for its operations.

## Uses

- **Has the dataset been used for any tasks already?**  
  The script is intended for general use in processing and augmenting incident report data. Specific use cases are not provided.

- **What tasks could the dataset be used for?**  
  The dataset could be used for analytical studies on incidents, such as understanding trends over time, the impact of weather conditions on incident rates, or geographical analysis of incidents within a town or city.

## Distribution

- **How will the dataset be distributed?**  
  The dataset's distribution is not applicable here as it's generated dynamically by the script. However, the script itself can be shared and used by others.

## Maintenance

- **Who is supporting/hosting/maintaining the dataset?**  
  Support and maintenance for the script and any generated dataset would be the responsibility of the individual or entity that uses it.

- **How can the owner/curator/manager of the dataset be contacted?**  
  Contact information is not provided, as the dataset creator and maintenance responsibilities are not specified.
