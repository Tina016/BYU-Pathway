#Week 7 | Project - Windchill Calculator

"""
Author: Martina Toebe

Purpose: write a program that asks the user for a t and then shows the wind chill values for various wind speeds at that t.

Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)

Where,T= Air t (ºF) V= Wind Speed (mph)

Convert from Celsius to Fahrenheit and return the converted temperature. 
The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.

Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and calculate and display the wind chill (using the windchill function created above) for each of these wind speeds.

Display the wind chill value to 2 decimals of precision.

"""
print("\nWelcome to the windchill calculator, making you life better!\n")# Not so creative, but adding something to look more like a program

# Function for windchill calculus

def windchill_calculator(t, v):
    return 35.74 + (0.6215 * t) - (35.75 * v ** 0.16) + (0.4275 * t * v ** 0.16) # Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * (9/5) + 32 # Convertion formula  multiply the Celsius temperature by (9/5) and then add 32

# User input option
t = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ").upper()# Validade the input tu upper case

if unit == 'C':
    t = celsius_to_fahrenheit(t)

# Display results
print(f"At t {t}F:")

# Validate the range for wind speed
wind_speed = 5
while wind_speed <= 60:
    wind_chill = windchill_calculator(t, wind_speed)
    print(f"At wind speed {wind_speed} mph, the wind chill is: {wind_chill:.2f}F")# Display validation with 2 decimal
    wind_speed += 5

# End
