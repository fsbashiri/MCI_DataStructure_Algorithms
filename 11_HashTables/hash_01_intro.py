def hash_func():
    print("aaaaaah!")
    return

user = {
    "name": 'Kyle',
    "age": 54,
    "magic": True,
    "scream": hash_func
}

print(user["name"]) # Lookup O(1)
print(user["scream"])
user["spell"] = 'abra kadabra' # Insert O(1)
print(user)