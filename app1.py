while True:
    try:
        print("Calculator UI!")
        print("1 - Addition\n 2 - Subtraction \n 3 - Multiplication \n 4 - Division \n 5 - Quit")
        opt = input('Enter choice! : ')
        
        if opt == '1':
            num1 = int(input('Enter number 1: '))
            num2 = int(input('Enter number 2: '))
            print(num1 + num2)
            print("\n")
        elif opt == '2':
            num1 = int(input('Enter number 1: '))
            num2 = int(input('Enter number 2: '))
            print(num1 - num2)
            print("\n")
        elif opt == '3':
            num1 = int(input('Enter number 1: '))
            num2 = int(input('Enter number 2: '))
            print(num1 * num2)
            print("\n")
        elif opt == '4':
            num1 = int(input('Enter number 1: '))
            num2 = int(input('Enter number 2: '))
            print(num1 / num2)
            print("\n")
        else: 
            break
    except:
        print('big error')