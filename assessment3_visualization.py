# visualization.py
# 🌟 Carbon Footprint Visualization 🌟
# Author: Mahima Prajapati
# Group Members:
#   🔹 Maulik Miyani
#   🔹 Andre Lenon
#   🔹 Mahima Prajapati

import matplotlib.pyplot as plt


# ============================
# Function to create a chart
# ============================
def create_chart(emissions, filename="chart.png"):
    """
    Function: create_chart
    Purpose: Visualize carbon emissions in a bar chart
    Parameters:
        emissions (dict): Dictionary containing categories and values of CO2 emissions
        filename (str): Optional filename to save the chart
    Returns:
        str: The filename of the saved chart
    Authors:
        🔹 Maulik Miyani
        🔹 Andre Lenon
        🔹 Mahima Prajapati
    """
    # ----------------------------
    # Prepare data for plotting
    # ----------------------------
    labels = list(emissions.keys())  # Extract category names
    values = list(emissions.values())  # Extract emission values

    # ----------------------------
    # Create the bar chart
    # ----------------------------
    plt.figure(figsize=(5, 5))  # Set figure size
    plt.bar(labels, values, color=['#2ca02c', '#1f77b4', '#ff7f0e'])  # Add colors for better visual
    plt.title("Carbon Footprint Breakdown")  # Add chart title with emoji
    plt.ylabel("kg CO2")  # Label for y-axis

    # ----------------------------
    # Show the chart
    # ----------------------------
    # plt.savefig(filename)  # Optional: Save chart to file (currently commented)
    plt.show()  # Display the chart
    plt.close()  # Close the figure to free memory

    return filename  # Return the filename for reference
