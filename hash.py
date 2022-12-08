import hashlib
# Rtrams
#smart
# Splkiyoanr
# lion 
email = "selim17@gmail.com"
pwd= 'Selim Saba Ka vlobasa'
pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()


your_email = "selim17@gmail.com" 
your_password = "079e0bd14d8b631019dd7c03ff5939e1" 
hashed_your_password = hashlib.md5(your_password.encode()).hexdigest()
if email == your_email and pwd_hash == hashed_your_password:
    print("Right User")
else:
    print("Wrong Password")
hacker_email = "selim17@gmail.com" 
hacker_password = "079e0bd14d8b631019dd7c03ff5939e1" 
print(pwd)
print(pwd_hash)


