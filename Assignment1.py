def convert_temperature(temp, unit):
    """
    Converts temperature between Fahrenheit and Celsius.
    
    Parameters:
        temp (float): The temperature value to convert.
        unit (str): The unit of the input temperature ('F' or 'C').
    
    Returns:
        float: The converted temperature rounded to 2 decimal places.
    """
    if unit.upper() == 'F':
        # Convert Fahrenheit to Celsius
        converted = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {round(converted, 2)}°C")
    elif unit.upper() == 'C':
        # Convert Celsius to Fahrenheit
        converted = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {round(converted, 2)}°F")
    else:
        print("Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        return None

    return round(converted, 2)


# ----- Main Program -----
print("Temperature Converter")
try:
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of the given temperature (C/F): ")
    convert_temperature(temp, unit)
except ValueError:
    print("Please enter a valid numeric temperature.")
