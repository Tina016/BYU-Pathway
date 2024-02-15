# Declaring the variable for the file
life_expectancy = "life-expectancy.csv"

# Open csv file
with open(life_expectancy, 'r') as le_file:
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

    # Initialize variables to calculate average, min, and max life expectancy for a specific country
    country_of_interest = input("Enter the country of interest: ")
    country_life_expectancies = []

    # Iterate over each row in the CSV file
    for line in le_file:
        # Split rows by comma
        row = line.strip().split(',')

        # Extracting values for each element
        country = row[0]
        country_code = row[1]
        year = row[2]
        life_expectancy = row[3]

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

            # Collect life expectancies for the country of interest
            if country.lower() == country_of_interest.lower():
                country_life_expectancies.append(life_expectancy)

    # Calculate average life expectancy by year of interest
    if num_year_entries > 0:
        avg_year_life_expectancy = total_year_life_expectancy / num_year_entries
    else:
        avg_year_life_expectancy = 0

    # Calculate average, min, and max life expectancy for the country of interest
    if country_life_expectancies:
        country_avg_life_expectancy = sum(country_life_expectancies) / len(country_life_expectancies)
        country_max_life_expectancy = max(country_life_expectancies)
        country_min_life_expectancy = min(country_life_expectancies)
    else:
        country_avg_life_expectancy = country_max_life_expectancy = country_min_life_expectancy = "No data available"

    # Print results
    print(f"The overall max life expectancy is: {overall_highest_life_expectancy} from {overall_highest_country} in {overall_highest_year}")
    print(f"The overall min life expectancy is: {overall_lowest_life_expectancy} from {overall_lowest_country} in {overall_lowest_year}")
    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {avg_year_life_expectancy:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max_life_expectancy}")
    print(f"The min life expectancy was in {year_min_country} with {year_min_life_expectancy}")
    print(f"\nFor {country_of_interest}:")
    print(f"The average life expectancy is {country_avg_life_expectancy:.2f}")
    print(f"The max life expectancy is {country_max_life_expectancy}")
    print(f"The min life expectancy is {country_min_life_expectancy}")

    # End