
# Dictionaries

customer = {
    "name": "John Smit",
    "age": 30,
    "is_varified": True
}
# customer["name"] =  "John"
print(customer["name"])
print(customer.get("age", 20)) # here 20 is default value

phone = input("Phone ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}

output = ""

for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)



# Emoji Converter

message = input("> ")
words = message.split(' ')

emojis = {
    ":)": "😊",
    ":(": "😔",
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

