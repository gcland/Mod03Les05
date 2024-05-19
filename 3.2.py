import re
from statistics import mean

with open("weather_2020.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    a = re.findall("\d+°C", line)

c = []
for item in a:
    b = re.findall("\d+", item)
    c.append(b[0])

d = []
for number in c:
    d.append(int(number))

year2020_avg = mean(d)
print(f"The average temperature across the year 2020 is {round(year2020_avg,2)}°C.")

with open("weather_2021.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    a = re.findall("\d+°C", line)

c = []
for item in a:
    b = re.findall("\d+", item)
    c.append(b[0])

d = []
for number in c:
    d.append(int(number))

year2021_avg = mean(d)
print(f"The average temperature across the year 2021 is {round(year2021_avg,2)}°C.")

if year2020_avg > year2021_avg:
    print(f"2020 had a higher average temperature with {round(year2020_avg,2)}°C average compared to 2021's {round(year2021_avg,2)}°C average.")
if year2021_avg > year2020_avg:
    print(f"2021 had a higher average temperature with {round(year2021_avg,2)}°C average compared to 2021's {round(year2020_avg,2)}°C average.")