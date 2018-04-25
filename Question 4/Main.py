import json
from collections import Counter

#Use a dictionary to keep a number associated with each month
monthNameToNumber = {
	1: "January", 2: "February", 3: "March", 4: "April",
	5: "May", 6: "June", 7: "July", 8: "August",
	9: "September", 10: "October", 11: "November", 12: "December"
}

with open("birthdays.json", "r") as bdayJ:
	birthdaysInJSON = json.load(bdayJ)

#Initialize an array of the months we extract from the JSON
extractedMonths = []

for name, birthday_string in birthdaysInJSON.items():
    #Get the birthday month
    splitStr = birthday_string.split("/")
    month = int(splitStr[0])

    #Add found month to array
    extractedMonths.append(monthNameToNumber[month])

#Use collections built in Counter module to help count each month
counter = Counter(extractedMonths)

#Put the counter object into a dictionary and print it
print(dict(counter))