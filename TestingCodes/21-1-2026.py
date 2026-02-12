import time

def main():
    age = int(input("Tell your age: "))
    role = "student"

    if age >= 18 and role == "student":
        print("Adult student")

if __name__ == "__main__":
    main()
