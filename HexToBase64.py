import binascii
h = input("Enter hex string")
hex = h.decode("hex")
base64 = binascii.b2a_base64(hex)
print(base64)
