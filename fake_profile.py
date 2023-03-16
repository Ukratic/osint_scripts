import random
import requests

# Make a request to the randomuser API to get a random profile
response = requests.get("https://randomuser.me/api/").json()

# Extract the necessary information from the response data
gender = response["results"][0]["gender"]
age = response["results"][0]["dob"]["age"]
first_name = response["results"][0]["name"]["first"]
last_name = response["results"][0]["name"]["last"]
email = response["results"][0]["email"]
picture_url = response["results"][0]["picture"]["large"]
country = response["results"][0]["location"]["country"]
address = response["results"][0]["location"]["street"]["name"] + " " + str(response["results"][0]["location"]["street"]["number"])
postcode = response["results"][0]["location"]["postcode"]
city = response["results"][0]["location"]["city"]

# Generate a random email address
username = first_name.lower() + last_name.lower() + str(random.randint(100, 999))
domain = random.choice(["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"])
email_address = f"{username}@{domain}"

# Print the fake profile information
print("Name: " + first_name + " " + last_name)
print("Age: " + str(age))
print("Gender: " + gender)
print("Country: " + country)
print("Email: " + email_address)
print("Address: " + address + ", " + str(postcode) + " " + city)

# output fake profile information to a txt file
with open(f"{first_name}_{last_name}_profile.txt", "w") as f:
    f.write("Name: " + first_name + " " + last_name + "\n"
            " Age: " + str(age) + "\n"
            "Gender: " + gender + "\n"
            "Country: " + country + "\n"
            "Email: " + email_address + "\n"
            "Address: " + address + ", " + str(postcode) + " " + city)

# Download the profile picture and save it to a file
response = requests.get(picture_url)
with open(f"{first_name}_{last_name}_pic.jpg", "wb") as f:
    f.write(response.content)