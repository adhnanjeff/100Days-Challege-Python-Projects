import pandas as pd
import datetime as dt
import smtplib

# Read birthday data from CSV
data = {
    'Name': ['Shruthi', 'Daddy', 'Bahu ka', 'Amma', 'Adhnan'],
    'Email': ['shruthivijay03@gmail.com', 'siraj2669@yahoo.com', 'bzulaiha@gmail.com', 'thasleemasiraj96@gmail.com','adhnanjeffms@gmail.com'],
    'Year': [2003, 1972, 1999, 1983, 2004],
    'Month': [9, 11, 12, 4, 4],
    'Day': [3, 17, 25, 23, 22]
}

my_mail = "adhnanjeff26@gmail.com"
my_pass = "mltanulztjluvnjk"
df = pd.DataFrame(data)

# Define a function to check a condition
def find_matching_name(month, day):
    matching_row = df[(df['Month'] == month) & (df['Day'] == day)]
    if not matching_row.empty:
        return matching_row.iloc[0]  # Return the first matching row
    else:
        return None

# Get current date
now = dt.datetime.now() 
month = now.month
day = now.day

# Find matching birthday
matching_row = find_matching_name(month, day)

# Print the matching row
#print(matching_row)

name = matching_row['Name']
with open("Base/Projects/Day 32/letter.txt") as f:
    letter_content = f.read()
    new_letter = letter_content.replace("[person]", name)

with smtplib.SMTP("smtp.gmail.com") as conn:
    conn.starttls()
    conn.login(user=my_mail, password=my_pass)
    conn.sendmail(
        from_addr=my_mail,
        to_addrs=matching_row['Email'],
        msg=f"Subject: Happy Birthday {name}\n\n{new_letter}"
    )