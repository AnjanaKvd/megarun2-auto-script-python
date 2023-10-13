import subprocess

# Function to simulate a swipe
def swipe(left=True):
    # Starting coordinates for your character
    character_x = 360  # Rounded to the nearest integer
    character_y = 1200  # Rounded to the nearest integer
    
    # Calculate the ending coordinates based on your swipe direction
    if left:
        end_x = character_x - 200  # Adjust the value as needed
    else:
        end_x = character_x + 200  # Adjust the value as needed
    
    end_y = character_y  # Maintain the same Y coordinate
    
    # Duration for the swipe
    duration = 200  # Adjust the duration as needed
    
    # Use ADB to simulate the swipe
    swipe_command = f"adb shell input swipe {character_x} {character_y} {end_x} {end_y} {duration}"
    subprocess.run(swipe_command.split())

# To swipe left:
while True:
    swipe(left=True)

# To swipe right:
# swipe(left=False)
