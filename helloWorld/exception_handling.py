numerator=10
denominator=0

"""print(numerator/denominator)"""
try:
    numerator= int(input("Enter numerator:"))
    denominator = int(input("Enter denominator:"))

    result= numerator / denominator
    print(result)
except:
    print("Denominator cannot be Zero. Please try again")
    print("Program ends")