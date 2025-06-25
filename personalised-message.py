# displaying personalised message which can handle leading and trailing spaces.
firstname = input("what is your name?")
lastname = input("what is your last name?")
clean_firstname = firstname.strip()
clean_lastname = lastname.strip()
name = clean_firstname+" "+clean_lastname
if name== " ":
    print("Hello, Stranger.")
else:
    print(f"Hello {name}, Welcome.")
 