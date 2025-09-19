# Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9).

# Input temp in celsius.
celsius = float(input("Enter the temperature in celsius:"))
# Convert Celsiua to fahreheit using formula.
fahrenheit = (9 * celsius) / 5 + 32
# Display output
print(f"temperature in fahrenheit: {fahrenheit}")
