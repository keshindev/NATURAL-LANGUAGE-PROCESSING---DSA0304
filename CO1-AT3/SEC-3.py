import re

text = input("Enter text:\n")

while True:
    print("\n1.Date  2.Phone  3.Hashtag  4.Mention  5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print(re.findall(r"\d{2}/\d{2}/\d{4}", text))

    elif choice == "2":
        print(re.findall(r"[6-9]\d{9}", text))

    elif choice == "3":
        print(re.findall(r"#\w+", text))

    elif choice == "4":
        print(re.findall(r"@\w+", text))

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
        
