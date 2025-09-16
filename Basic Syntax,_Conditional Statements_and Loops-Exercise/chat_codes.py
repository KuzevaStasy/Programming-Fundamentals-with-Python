message_number = int(input())

for i in range(message_number):
    message_code = int(input())

    if message_code == 88:
        print("Hello")
    elif message_code == 86:
        print("How are you?")
    elif (message_code != 88 and message_code != 86) and message_code < 88:
        print("GREAT!")
    else:
        print("Bye.")
