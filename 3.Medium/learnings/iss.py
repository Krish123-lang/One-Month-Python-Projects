import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

# Fetch current astronauts data from the API
astronauts_url = "http://api.open-notify.org/astros.json"
with urllib.request.urlopen(astronauts_url) as response:
    astronauts_data = json.loads(response.read())

# Write astronauts info to a text file
with open("iss.txt", "w") as file:
    file.write(f"There are currently {astronauts_data['number']} astronauts on the ISS:\n\n")
    for person in astronauts_data["people"]:
        file.write(f"{person['name']} - onboard\n")

    # Get user's current latitude and longitude
    user_location = geocoder.ip('me')
    file.write(f"\nYour current lat / long is: {user_location.latlng}")

# Open the text file in the default web browser
webbrowser.open("iss.txt")

# Setup the turtle screen for ISS tracking map
screen = turtle.Screen()
screen.setup(width=1280, height=720)
screen.setworldcoordinates(-180, -90, 180, 90)

# Load world map and ISS icon
screen.bgpic("images/map.gif")
screen.register_shape("images/iss.gif")

# Create the turtle representing the ISS
iss = turtle.Turtle()
iss.shape("images/iss.gif")
iss.setheading(45)
iss.penup()

# API endpoint to get ISS current position
iss_position_url = "http://api.open-notify.org/iss-now.json"

try:
    while True:
        with urllib.request.urlopen(iss_position_url) as response:
            data = json.loads(response.read())

        lat = float(data["iss_position"]["latitude"])
        lon = float(data["iss_position"]["longitude"])

        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")

        # Update ISS position on map
        iss.goto(lon, lat)

        # Pause for 5 seconds before updating again
        time.sleep(5)

except KeyboardInterrupt:
    print("\nISS tracking stopped by user.")
    turtle.bye()  # Close turtle window cleanly