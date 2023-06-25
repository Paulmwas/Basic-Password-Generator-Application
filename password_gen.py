import string
import random
#To read and write a csv file import the module from csv library
from csv import writer

def passgen():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    platform = input('Enter the name of the  platform: \n')
    pass_length = int(input('Enter the length of your password: \n'))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    password = ("".join(s[0:pass_length]))
    print(password)
    #create a column in form of a list
    passdata = [platform,password]
    #Appending your data in the csv file
    with open('pass.csv','a')as f:
        writedata = writer(f)
        writedata.writerow(passdata)
    

passgen()
    