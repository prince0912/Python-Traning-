print("enetr 'x' for exit. ");
num = input("enter any number:");
if num == 'x':
    exit();
try:
    number = int(num);
except valueError:
    print("Enetr a Number:");
else:
    for i in range(2, number):
        if number%i==0:
              print(number," is not a prime number.");
        break;
    else:
              print(number,"is a prime number.");
