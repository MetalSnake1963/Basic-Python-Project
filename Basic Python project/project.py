#Library
import csv
from hashlib import sha256

#here I oppend required Files
with open("pas_with_sha256.csv") as sha:
    token = list(csv.reader(sha))

# I made one empty dictionary and list
name_users = []
password_dict = {}

# I made hash codes from 0 To 10,000 Down there
for password in range(0, 10000):
    hash = sha256(b"%i" %password).hexdigest()
    password_dict[hash] = password

# I compared file hash codes and hash code dict I created.
for key in token:
    name = key[0]
    hashed_password = key[1]
    cracked_password = password_dict.get(hashed_password)
    if cracked_password is not None:
        name_users.append(name)
        print(name, ':', cracked_password) #finaly I cracked your passwords

print("|Developed by Metal Snake|")