##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import random
import pandas

PLACEHOLDER = "[NAME]"

data= pandas.read_csv('birthdays.csv')
birth_year= data.year.values.tolist()
birth_month= data.month.values.tolist()
birth_day= data.day.values.tolist()
name= data.name.values.tolist()
email= data.email.values.tolist()

time= dt.datetime.now()
year= time.year
month= time.month
day= time.day

for months in birth_month:
  for days in birth_day:
    for emails in email:
      current_index = email.index(emails)
      current_name = name[current_index]
    
    if month == months:
      if day == days:
        letter_list= []
        with open('letter_templates\letter_1.txt') as first_letter:
          first_letter_content = first_letter.read()
          new_letter = first_letter_content.replace(PLACEHOLDER, current_name)
            
        letter_list.append(new_letter)
        
        with open('letter_templates\letter_2.txt') as second_letter:
            second_letter_content = second_letter.read()
            new_letter1 = second_letter_content.replace(PLACEHOLDER, current_name)
            
        letter_list.append(new_letter1)
        
        with open('letter_templates\letter_3.txt') as third_letter:
            third_letter_content = third_letter.read()
            new_letter2 = third_letter_content.replace(PLACEHOLDER, current_name)
            
        letter_list.append(new_letter2)
        
        letters = random.choice(letter_list)

        my_email = 'wendpanga2002@gmail.com'
        my_password = 'lehxmorbeldeytjl'

        with smtplib.SMTP('smtp.gmail.com') as connection:
          connection.starttls()
          connection.login(user= my_email, password= my_password)
          connection.sendmail(from_addr= my_email, to_addrs= 'marcusawen@yahoo.com', msg=f'Subject:Birthday Wishes\n\n{letters}')
