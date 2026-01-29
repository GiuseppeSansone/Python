# Capture pattern matching for assigning values within the match

name = input("What is your name? ")

match name:
    case "":
        print("Tach Post")
    case "Josi" | "Giuseppe" as s:
        print(f"Oh hi there, {s}!")
    case name:
        print(f"Hello, {name}!")

