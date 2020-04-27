name = input("Please enter your name: ")
password = input("Please enter a password: ")
if ((name == "bob") and (password == "password1234")) or ((name == "fred") and (password == "happyPass122")) or ((name == "lock") and (password == "passwithlock44")):
    print("Welcome: " + name + " " + "Access has been granted: ")
else:
    print("You are not welcome...Access denied! ")
    
    