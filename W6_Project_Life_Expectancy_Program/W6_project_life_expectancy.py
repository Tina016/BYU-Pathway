 #Week 6 | Project - Life Expectancy

"""
Author: Martina Toebe

Purpose: The dataset you will be using comes from OurWorldInData.org from an article on the Spanish Flu. The first graph on that page shows the life expectancies over the years for various countries.

You can download the dataset directly here: life-expectancy.csv. This is a .csv (Comma Separated Values) file that contains the data you'll need with each column separated by commas. There are roughly 19,000 rows in this dataset.

This dataset is licensed under the Creative Commons BY license, you may also read the Life Expectancy Data License.

Your task is to write a program to help analyze this large amount of data.

"""
# Import library to read CSV
import csv

# Declaring the variable for the file
life_expectancy = "life-expectancy.csv"

# Open csv file
with open(life_expectancy) as le_file:
    # Create a CSV reader object
    le_csv = csv.reader(le_file)
    
    # Initialize variables to store lowest and highest life expectancy
    overall_lowest_life_expectancy = None
    overall_lowest_country = ''
    overall_lowest_year = ''

    overall_highest_life_expectancy = None
    overall_highest_country = ''
    overall_highest_year = ''

    # Initialize variables to calculate average life expectancy by year of interest
    year_of_interest = int(input("Enter the year of interest: "))
    total_year_life_expectancy = 0
    num_year_entries = 0
    year_max_life_expectancy = None
    year_max_country = ''
    year_min_life_expectancy = None
    year_min_country = ''

    # Iterate over each row in the CSV file
    for row in le_csv:
        # Split rows by comma
        country_row = row[0].split(',')
        country_code_row = row[1].split(',')
        year_row = row[2].split(',')
        life_expectancy_row = row[3].split(',')

        # Loop through each element in the rows
        num_elements = len(country_row)
        i = 0
        while i < num_elements:
            # Extracting values for each element
            country = country_row[i]
            country_code = country_code_row[i]
            year = year_row[i]
            life_expectancy = life_expectancy_row[i]

            # Check if life expectancy is valid (numeric)
            if life_expectancy.replace('.', '').isdigit():  
                life_expectancy = float(life_expectancy)

                # Checking for overall lowest
                if overall_lowest_life_expectancy is None or life_expectancy < overall_lowest_life_expectancy:
                    overall_lowest_life_expectancy = life_expectancy
                    overall_lowest_country = country
                    overall_lowest_year = year

                # Checking for overall highest
                if overall_highest_life_expectancy is None or life_expectancy > overall_highest_life_expectancy:
                    overall_highest_life_expectancy = life_expectancy
                    overall_highest_country = country
                    overall_highest_year = year

                # Checking for average, max, and min by year of interest
                if int(year) == year_of_interest:
                    total_year_life_expectancy += life_expectancy
                    num_year_entries += 1

                    # Checking for max life expectancy by year of interest
                    if year_max_life_expectancy is None or life_expectancy > year_max_life_expectancy:
                        year_max_life_expectancy = life_expectancy
                        year_max_country = country

                    # Checking for min life expectancy by year of interest
                    if year_min_life_expectancy is None or life_expectancy < year_min_life_expectancy:
                        year_min_life_expectancy = life_expectancy
                        year_min_country = country

            i += 1

    # Calculate average life expectancy by year of interest
    if num_year_entries > 0:
        avg_year_life_expectancy = total_year_life_expectancy / num_year_entries
    else:
        avg_year_life_expectancy = 0

    # Print results
    print(f"The overall max life expectancy is: {overall_highest_life_expectancy} from {overall_highest_country} in {overall_highest_year}")
    print(f"The overall min life expectancy is: {overall_lowest_life_expectancy} from {overall_lowest_country} in {overall_lowest_year}")
    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {avg_year_life_expectancy:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max_life_expectancy}")
    print(f"The min life expectancy was in {year_min_country} with {year_min_life_expectancy}")

    # End

