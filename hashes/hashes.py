import hashlib

key = b"str2"
my_string = "this is a normal string. Nothing to see here".encode()

# for i in range(10):
#     hashed = hashlib.sha256(key).hexdigest()
#     print(hashed)

for i in range(10):
    hashed = hash(key)
    print(hashed % 8)
