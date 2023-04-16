# import smtplib

# my_email = 'wendpanga2002@gmail.com'
# my_password = 'rdfbkrzcgwuypcbi'

# with smtplib.SMTP('smtp.gmail.com') as connection:
#   # tls = transport layer security
#   connection.starttls()
#   connection.login(user= my_email, password= my_password)
#   connection.sendmail(from_addr= my_email, to_addrs= 'marcusawen@yahoo.com', msg='Subject:Hello\n\n This is the body of my email.')

# import datetime as dt

# now= dt.datetime.now()
# year= now.year
# print(year)

import smtplib
import pandas
import datetime as dt
import random

my_email = 'wendpanga2002@gmail.com'
my_password = 'qdtuslimambqkvnx'

date_time= dt.datetime.now()
day= date_time.weekday

quotes = pandas.read_csv('quotes.txt')
quote_list = quotes.values.tolist()
my_quote= ' '.join(random.choice(quote_list))

if day == 6:
  with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user= my_email, password= my_password)
    connection.sendmail(from_addr= my_email, to_addrs= 'marcusawen@yahoo.com', msg=f'Subject:Motivational Quote\n\n {my_quote}')
