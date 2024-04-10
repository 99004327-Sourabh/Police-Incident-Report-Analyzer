## Police Incident Report Analyzer

### Overview

- **Type of Data:** Structured data containing processed incident reports.
- **Purpose:** To analyze patterns in incidents (locations, frequencies, nature of incidents, time-based trends). Potentially used for resource allocation, risk assessment, or identifying areas needing additional support services.
- **Source:** Derived from incident reports in PDF format. The original issuer or creator of the PDF incident reports is Norman Police Department.

### Methods

- **Collection:**
  - Incident data is initially recorded in PDF reports.
  - Python code is used to:
    - Fetch incident reports from URLs (provided in a CSV file).
    - Extract relevant data from PDFs using regular expressions.
    - Augment data with:
      - Day of the week
      - Time of day
      - Geolocation coordinates (if possible)
      - WMO codes for weather conditions
      - Rankings of locations and incident types based on frequency
      - Side of town determination
      - EMSSTAT status inference (True if EMS-related)
- **Preprocessing:**
  - Regular expressions extract structured data elements from semi-structured PDF text.
  - Geocoding is used to translate addresses into latitude/longitude coordinates.
  - Data transformations are used to generate rankings and categorize incidents.

### Variables

- **Day of the Week:** Day of the incident occurrence (1-7, where 1=Sunday)
- **Time of Day:** Hour of the incident (0-23)
- **Weather:** WMO weather code (interpretation requires WMO Code manual)
- **Location Rank:** Rank of the incident location based on frequency of incidents.
- **Side of Town:** Side of the town relative to a given reference point (N, S, E, W, NW, NE, SW, SE).
- **Incident:** Incident type (e.g., Contact a Subject, Larceny)
- **Nature Rank:** Rank of the incident type based on frequency.
- **EMSSTAT:** Whether the incident is EMS-related (True or False)

### Data Format

- **File Format:** Exported as CSV (based on the implied output).
- **Structure:** Tabular data (rows and columns)

### Quality and Limitations

- **Quality Factors:**
  - **Dependency on PDF Structure:** Changes in the PDF report format might break the regular expressions for data extraction.
  - **Geocoding Accuracy:** The accuracy of address-to-coordinate conversion can vary. Default coordinates are used in case of errors.
  - **WMO Interpretation:** Requires external WMO documentation to understand the weather codes.
- **Limitations**
  - **Missing Context:** Understanding some fields (Incident, EMSSTAT) might require domain knowledge of police/EMS terminology.
  - **Representativeness:** The data may only represent a specific region or a filtered set of incident reports.

### Use Cases

- **Trend Analysis:** Examining temporal patterns of incidents (time of day, day of week, weather-related).
- **Spatial Visualization:** Mapping incident hotspots or variations by the side of town.
- **Resource Planning:** Potentially informing police or EMS staffing/placement decisions (requires broader context).

### Privacy and Ethical Considerations

- **Anonymization:** Ensure any personally identifiable information or addresses have been removed or anonymized.
- **Sensitive Incident Types:** Be aware that some incident types may be sensitive in nature. Use and analyze the data in a responsible manner.

### Additional Notes

- **WMO Documentation:** The specific WMO Code table used is essential for making sense of the Weather column.
- **EMSSTAT Inference:** Provide more details or insights on how the EMSSTAT status is determined.