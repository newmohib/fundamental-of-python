# Functions

def greet_user(first_name, last_name):
    print(f"Hi {first_name } {last_name}")


print("Start")
greet_user("Jhon", "Smith")
print("Finish")


# keyword Arguments greet_user(last_name = "jhone", first_name= "Smith")
# positional Arguments greet_user("jhone", "Smith")

greet_user(last_name="Mohib", first_name= "Rahman")
greet_user("Rahman", "Mohib")

# if we use both arguments in same functions then we use first positional Arguments then keyword Arguments, like example
greet_user("Rony", last_name= "MD")

# Return Statement
# by default all functions are return None


def square(number):
    return number * number


print(square(3))


# Creating a Reusable Function

def emoji_converter(message):
    words = message.split(' ')

    emojis = {
        ":)": "😊",
        ":(": "😔",
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return  output


# input from a user
message = input("> ")
result = emoji_converter(message)
print(result)


# Exceptions

try:
    age = int(input("Age: "))
    print(age)
    income = 20000
    risk = income / age
    print(risk)
except ZeroDivisionError:
    print("Age Cannot be 0")
except ValueError:
    print("Invalid value")
