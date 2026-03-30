##### Q.3 : Convert distant given in feet and inches into meter and centimeter.

# Take input
feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

# Convert into meters and centimeters
total_inches = (feet * 12) + inches      # 1 feet = 12 inches
meters = total_inches * 0.0254           # 1 inch = 0.0254 meters
centimeters = total_inches * 2.54        # 1 inch = 2.54 cm

# Display result
print(f'The distance of {feet} feet & {inches} inches is {meters} meters and {centimeters} centimeters.')