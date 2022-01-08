try:
    my_list = [1, 2, 3]
    i = int(input("Enter index: "))
    print(my_list[i])

    numerator= int(input("Enter numerator:"))
    denominator = int(input("Enter denominator:"))

    result= numerator / denominator
    print(result)

# handling specific exception

except ZeroDivisionError:
    print("Denominator cannot be Zero. Please try again")

except IndexError:
    print("Index cannot be greater than size of the list")
    print("Program ends")
