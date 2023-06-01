import csv
from hashlib import sha256

with open("pas_with_sha256.csv") as sha:
    token = list(csv.reader(sha))

name_users = []
password_dict = {}

for password in range(0, 10000):
    hash = sha256(b"%i" %password).hexdigest()
    password_dict[hash] = password

for key in token:
    name = key[0]
    hashed_password = key[1]
    cracked_password = password_dict.get(hashed_password)
    if cracked_password is not None:
        name_users.append(name)
        print(name, ':', cracked_password)
