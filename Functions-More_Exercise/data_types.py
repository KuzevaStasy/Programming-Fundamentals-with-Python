def process_input(data_type):

    if data_type == "int":
        number = int(input())
        print(number * 2)

    elif data_type == "real":
        number = float(input())
        print(f"{number * 1.5:.2f}")

    elif data_type == "string":
        text = input()
        print(f"${text}$")

    else:
        print("Invalid type")

data = input().strip()
process_input(data)