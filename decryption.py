choice = input("Do you have a file to decrypt or do you want to create a file:\nPress 1 to decrypt a text file\nPress 2"
               " to enter text\n")

if choice == "1":
    fhand_name = input("Enter the name of the file: ")
    fhand = open(fhand_name)
    enc = fhand.read()
if choice == "2":
    enc = input("enter the text to be decrypted: ")

password = input("enter the decryption key: ")
deenc = ""

k = 0
for i in range(len(enc)):
    if i <= (len(password)-1):
        k = int(password[i])
        deenc = deenc + chr(ord(enc[i])-k)
    if i > (len(password)-1):
        k = int(password[((i+1) % len(password))-1])
        deenc = deenc + chr(ord(enc[i])-k)
print("this is your decrypted text:\n{}".format(deenc))