import csv
import json

# json_string = '{"name": "Pranav", "age": 18, "city": "Jaipur"}'
# data = json.loads(json_string)  # Parse JSON string to a Python dictionary
# print(data["city"])

# with open("data.json", "r") as file:
#     data = json.load(file)  # Load JSON data from file into a Python dictionary
#     print(data)


# data = {"name": "Bob", "age": 30, "city": "London"}
# # json_string = json.dumps(data, indent=4)  # Convert dictionary to JSON string
# # print(json_string)
#
# with open("output.json", "w") as file:
#     json.dump(data, file, indent=4)  # Write dictionary to JSON file


# Advanced JSON Operations

# nested_json = ('{"person": {"name": "Alice", "age": 25, "address": '
#                '{"city": "New York", "zip": "10001","state" : "Delhi"}}}')
# data = json.loads(nested_json)
# print(data["person"]["name"])  # Output: New York

# json_array = ('[{"name": "Alice"}, {"name": "Bob"},'
#               '{"name": "Sreekanth"},{"name": "Pranav"},{"name": "Dhamjit"}]')
# data = json.loads(json_array)
# for item in data:
#     print(f"Team of Netsetos  {item["name"]}")  # Output: Alice, Bob

# SELECT
#   fullVisitorId,
#   hits
# FROM
#   `bigquery-public-data.google_analytics_sample.ga_sessions_20170801`
# WHERE
#   ARRAY_LENGTH(hits) > 5
# LIMIT 10;

# with open("data.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)  # Each row is a list


# with open("data.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["provider_id"], row["agency_name"],row["state"])


# Write to a csv file

# data = [["Name", "Age", "City"], ["Alice", 25, "New York"],
#         ["Bob", 30, "London"],["Dhamjit",18,"Tamil Nadu"]]
#
# with open("demo_name_age.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)  # Write multiple rows


# data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
# # From Rest API . File , Database
#
# with open("output.csv", "w", newline="") as file:
#     fieldnames = ["name", "age"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#
#     writer.writeheader()  # Write the header row
#     writer.writerows(data)  # Write the data rows

# File Conversion
import json
import csv

# JSON data
# json_data = [
#     {"name": "Alice", "age": 25, "city": "New York"},
#     {"name": "Bob", "age": 30, "city": "London"}
# ]
# #
# # Convert JSON to CSV
# with open("output_json_csv.csv", "w", newline="") as file:
#     fieldnames = ["name", "age", "city"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerows(json_data)

# import csv
# import json
#
# # Read CSV and convert to JSON
# with open("data.csv", "r") as file:
#     reader = csv.DictReader(file)
#     data = [row for row in reader]
#
# # Write JSON to a file
# with open("output_from_csv.json", "w") as file:
#     json.dump(data, file, indent=4)


#Read data from a JSON file, modify it, and save it as a CSV file.
#ETL Extract Transform Load
import json
import csv

# Step 1: Read JSON data  Extract
with open("data.json", "r") as json_file:
    json_data = json.load(json_file)
    print(json_data)

# Step 2: Modify the data Transform
for record in json_data:
    # print(record)
    record["age"] = int(record["age"]) +  1  # Increment age by 1
#
# Step 3: Save data to CSV Load
with open("output_ex4.csv", "w", newline="") as csv_file:
    fieldnames = json_data[0].keys()  # Use keys from JSON as column headers
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(json_data)





















