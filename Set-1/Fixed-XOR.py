import binascii
#define starting string
h = "1c0111001f010100061a024b53535009181c"
hex = h.decode("hex")
p = "686974207468652062756c6c277320657965"
print(bin(h ^ p))
