print("Hello Welcome to Smart Login System")
print("___________________________________")
print("")

correct_username = "admin"
correct_password = "admin123"

attempt = 0

while attempt < 3:
    username = input("Enter the Username : ")
    password = input("Enter the password : ")

    if username == correct_username and password == correct_password:
        print("Login Successfully")
        break
    else:
        print("try again you enter wrong password")
        attempt = attempt + 1

if attempt ==3:
    print("Account Blocked")

    


