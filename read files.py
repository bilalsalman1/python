contact_file = open ("text.txt" , "r")
for contact in contact_file.readlines():
    print(contact)

contact_file.close()