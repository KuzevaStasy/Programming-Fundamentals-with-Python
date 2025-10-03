def loading_bar(number):
    completed = number // 10
    remaining = 10 - completed

    if number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{number}% [{'%' * completed}{'.' * remaining}]")
        print("Still loading...")


num = int(input())
loading_bar(num)
