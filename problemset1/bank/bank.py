greeting = input("Greeting: ")
normalized = greeting.strip().lower()
if normalized.startswith("hello"):
    print("$0")
elif normalized.startswith("h"):
    print("$20")
else:
    print("$100")
