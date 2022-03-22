import random  as rnd
from random import choice

password=""
table_strong= "abcdefghigklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(?)_+-=*/\'\";:[{]}.<,>|`~"

for i in range(int(input("give me how many characters you want to have in your password: "))):
    password+=choice(table_strong)
print("password= ", password)