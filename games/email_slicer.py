#email
email = input("What is your email ID?: ").strip()
#slice username
user = email[:email.index("@")]
#slice domain name
domain = email[email.index("@") + 1:]
#output_format
output = "Your username is {} and your domain name is {}.".format(user, domain)
#output_display
print(output)
print()
print("No personal info was stolen. We are good people!")
