import re

with open("contact_list.txt", "r") as file:
    lines = file.readlines()
emails = []
names = []
for line in lines:
    email = re.findall(r"[A-Za-z0-9._%+-`!@#$%^&*()]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", line) 
    if email == []:
        continue
    else:
        emails.append(email)
        
i=0
print("Emails found:")
for email in emails:
    i+=1
    print(f"{i}. {email[0]}")