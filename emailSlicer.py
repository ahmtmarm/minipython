def main():
    print("Welcome to the email slicer")

    email_input = input("Input your email adress: ")
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    main()