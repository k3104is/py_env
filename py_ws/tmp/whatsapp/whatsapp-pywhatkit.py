import pywhatkit

phone_number = input("Enter phone number: ")

pywhatkit.sendwhatmsg(phone_number, "Test", 2, 20, 15, True, 2)