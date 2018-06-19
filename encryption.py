# text = input("enter the text to be encrypted: ")
# enc = ""
# for i in text:
#     enc = enc + chr(ord(i)+2)
# print("this is the encrypted text:\n{}".format(enc))


choice = input("Do you have a file to encrypt or do you want to create a file:\nPress 1 to encrypt a text file\nPress 2"
    " to enter text\n")
if choice == "1":
    fhand_name = input("Enter the name of the file: ")
    fhand = open(fhand_name)
    text = fhand.read()
if choice == "2":
    text = input("enter the text to be encrypted: ")

# text = input("enter the t to be encrypted: ")
password = input("enter the encryption key: ")
enc = ""
# deenc = ""
k = 0
for i in range(len(text)):
    if i <= (len(password)-1):
        k = int(password[i])
        enc = enc + chr(ord(text[i])+k)
    if i > (len(password)-1):
        k = int(password[((i+1) % len(password))-1])
        enc = enc + chr(ord(text[i])+k)
name = input("What should the encrypted file be stored as?\n")
fout = open(name ,"w")
fout.write(enc)
# print("this is your text before encryption:\n{}\n\n".format(text))
# print("this is your encrypted text:\n{}".format(enc))
# print("")

# k = 0
# for i in range(len(enc)):
#     if i <= (len(password)-1):
#         k = int(password[i])
#         deenc = deenc + chr(ord(enc[i])-k)
#     if i > (len(password)-1):
#         k = int(password[((i+1) % len(password))-1])
#         deenc = deenc + chr(ord(enc[i])-k)
# print("this is your deencrypted text:\n{}".format(deenc))




























