import csv
from typing import Tuple, Optional

# ----------------- Question 1 -----------------
def analyze_climate_data(filename: str) -> Optional[Tuple[int, int, float, float, float, float]]:
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        if not data:
            print(f"The file at path {filename} is empty.")
            return None

        total_days = len(data)
        days_with_precipitation = sum(float(row['Precipitation']) > 0 for row in data)
        min_temperatures = [float(row['Minimum Temperature']) for row in data]
        max_temperatures = [float(row['Maximum Temperature']) for row in data]
        lowest_temperature = min(min_temperatures)
        highest_temperature = max(max_temperatures)
        mean_humidity = round(sum(float(row['Humidity']) for row in data) / total_days, 2)
        precipitations = [float(row['Precipitation']) for row in data]
        mean_precipitation = round(sum(precipitations) / total_days, 2)

        return total_days, days_with_precipitation, lowest_temperature, highest_temperature, mean_humidity, mean_precipitation

    except FileNotFoundError:
        print(f"The file at path {filename} does not exist.")
        return None


# invoke the function with relevant args of your choice
print(analyze_climate_data("data/weather_1.csv"))


# ----------------- Question 2 -----------------
def rainfall_prediction(filename: str) -> Optional[Tuple[int, int]]:
    try:
        correct_predictions=0
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        if not data:
            print(f"The file at path {filename} is empty.")
            return None
        
        for row in data:
            row['Temperature difference'] = (float(row['Maximum Temperature']) - float(row['Minimum Temperature']))
        

        predicted_rainy_days = sum(float(row['Temperature difference']) > 10 and float(row['Humidity']) > 50 for row in data)
        
        
        for row in data:
            
            if float(row['Precipitation']) > 0 and (float(row['Temperature difference']) > 10 and float(row['Humidity']) > 50):
                correct_predictions +=1
            
            if float(row['Precipitation']) == 0 and not ((float(row['Temperature difference']) > 10 and float(row['Humidity']) > 50)):
                correct_predictions +=1
            
        return predicted_rainy_days, correct_predictions

    except FileNotFoundError:
        print(f"The file at path {filename} does not exist.")
        return None


# invoke the function with relevant args of your choice
print(rainfall_prediction("data/weather_1.csv"))

def export_weather_predictions(source_file: str, destination_file: str) -> None:
    try:
        with open(source_file, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        if not data:
            print(f"The file at path {source_file} is empty.")
            return

        for row in data:
            row['Temperature difference'] = float(row['Maximum Temperature']) - float(row['Minimum Temperature'])
            row['forecast'] = 'sunny' if float(row['Temperature difference']) <= 10 or float(row['Humidity']) <= 50 else 'rainy'

        fieldnames = list(data[0].keys())
        fieldnames.remove('Temperature difference')
        
        for row in data:
            row.pop('Temperature difference', None)
        with open(destination_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    except FileNotFoundError:
        print(f"The file at path {source_file} does not exist.")

# invoke the function with relevant args of your choice
export_weather_predictions("data/weather_1.csv", "data/weather_1_pred.csv")
