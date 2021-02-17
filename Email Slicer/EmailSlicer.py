Email = str(input("Enter your Email :"))

def EmailSlicer(email):
    email.strip()
    username = email[:email.index("@")]
    domain_name = email[email.index('@')+1:]
    return 'Your username is %s and your domain is %s'%(username, domain_name)



print EmailSlicer(Email)