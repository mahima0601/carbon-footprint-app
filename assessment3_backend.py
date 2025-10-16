# assessment3_backend.py
# 🌟 Carbon Footprint Backend 🌟
# Author: Andre Lenon
# Group Members:
#   🔹 Maulik Miyani
#   🔹 Andre Lenon
#   🔹 Mahima Prajapati

import pandas as pd

# ============================
# Carbon emission factors
# ============================
FACTORS = {
    "transport": 0.21,   # kg CO2 per km travelled
    "electricity": 0.85,  # kg CO2 per kWh consumed
    "flights": 90        # kg CO2 per flight hour
}


# ============================
# Function to calculate carbon footprint
# ============================
def calculate_footprint(transport_km, electricity_kwh, flight_hours):
    """
    Function: calculate_footprint
    Purpose: Calculate emissions for transport, electricity, and flights
    Parameters:
        transport_km (float): Distance travelled in km
        electricity_kwh (float): Electricity usage in kWh
        flight_hours (float): Number of flight hours
    Returns:
        emissions (dict): Emissions per category
        total (float): Total carbon footprint
    Authors:
        🔹 Maulik Miyani
        🔹 Andre Lenon
        🔹 Mahima Prajapati
    """
    # Calculate emissions per category
    emissions = {
        "transport": transport_km * FACTORS["transport"],
        "electricity": electricity_kwh * FACTORS["electricity"],
        "flights": flight_hours * FACTORS["flights"]
    }

    # Calculate total emissions
    total = sum(emissions.values())

    return emissions, total


# ============================
# Function to save progress to CSV
# ============================
def save_progress(emissions, total, filename="footprint.csv"):
    """
    Function: save_progress
    Purpose: Save current emissions and total to a CSV file
    Parameters:
        emissions (dict): Emissions per category
        total (float): Total emissions
        filename (str): CSV filename to save data
    Authors:
        🔹 Maulik Miyani
        🔹 Andre Lenon
        🔹 Mahima Prajapati
    """
    # Create DataFrame for current entry
    df = pd.DataFrame([{
        "transport": emissions["transport"],
        "electricity": emissions["electricity"],
        "flights": emissions["flights"],
        "total": total
    }])

    # Try to read existing CSV and append new entry
    try:
        old = pd.read_csv(filename)
        df = pd.concat([old, df], ignore_index=True)
    except FileNotFoundError:
        # If file does not exist, create a new one
        pass

    # Save updated DataFrame to CSV
    df.to_csv(filename, index=False)


# ============================
# Function to get last saved results
# ============================
def get_last_results(filename="footprint.csv"):
    """
    Function: get_last_results
    Purpose: Retrieve the last 5 saved records from CSV
    Parameters:
        filename (str): CSV filename to read data
    Returns:
        pandas.DataFrame: Last 5 records, or empty DataFrame if file not found
    Authors:
        🔹 Maulik Miyani
        🔹 Andre Lenon
        🔹 Mahima Prajapati
    """
    try:
        df = pd.read_csv(filename)
        return df.tail(5)  # Return last 5 entries
    except FileNotFoundError:
        return pd.DataFrame()  # Return empty DataFrame if file doesn't exist
