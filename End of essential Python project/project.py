#import
import csv
import hashlib
from hashlib import sha256

#Open required Files
with open("pas_with_sha256.csv") as sha:
    token = list(csv.reader(sha))

#Empty Dictonary
password_dict = {}
#For Loop
for password in range(0,10000):
    Hash = sha256(b"%i" %password).hexdigest()
    password_dict[password] = Hash

for name in token:
    name_users = name[0]
