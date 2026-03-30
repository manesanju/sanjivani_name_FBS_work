##### Q.1 : Convert the time entered in hh,min and sec into seconds.

# Take input
hh = int(input("Enter hours: "))
mm = int(input("Enter minutes: "))
ss = int(input("Enter seconds: "))

# Convert into seconds
total_seconds = (hh * 3600) + (mm * 60) + ss     # 1 hour = 3600 seconds , 1 minute = 60 seconds

# Display result
print(f'The total seconds of {hh} hours & {mm} minutes & {ss} seconds is {total_seconds} seconds.')