name = input("Your name: ")
age = int(input("Your age: "))

print(f"\n🎉 Hi {name}! Congratulations!")
print(f"🎂 You are now {age} years old.")

print("\nFun fact:")
print(f"- At {age}, your back hurts for no reason")
print("- You get excited about discounts")
print("- And naps are no longer optional 😄")

print("\nDo you want to stay young at heart?")
print("If yes, type: good luck")

selection = input("> ")

if selection.lower() == "good luck":
    print("\n✨ Good luck activated!")
    print("You may be older, but at least you’re still awesome 😎")
else:
    print("\n😂 Wise choice. Aging is mandatory, growing up is optional!")
