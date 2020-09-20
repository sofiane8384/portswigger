import getpass
import json
import portswigger


email = input("Email address: ")
password = getpass.getpass("Password: ")

session = portswigger.login(email, password)
labs = portswigger.labs(session, verbose=False)
print(json.dumps(labs, indent=4))
