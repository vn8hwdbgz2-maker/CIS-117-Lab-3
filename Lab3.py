
# CIS-117 Lab3
# This program reads a CSV file containing country information
# and separates the countries into different CSV files based on
# their region. Each file contains only the country name and region.
#Christian Strus
#Worked Independently

import csv

try:
    # Open the country CSV file
    with open("country_full.csv", "r", newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)

        regions = {}

        # Organize countries by region
        for row in reader:
            country = row["name"]
            region = row["region"]

            if region not in regions:
                regions[region] = []

            regions[region].append(country)

    # Create a separate file for each region
    for region, countries in regions.items():
        filename = region + ".CSV"

        with open(filename, "w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)

            writer.writerow(["name", "region"])

            for country in countries:
                writer.writerow([country, region])

    print("Country files were created successfully!")

except FileNotFoundError:
    print("Error: The CSV file could not be found.")

except PermissionError:
    print("Error: You do not have permission to access the file.")

except IOError as error:
    print("File error:", error)
