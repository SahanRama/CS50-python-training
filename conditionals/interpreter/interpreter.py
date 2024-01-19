def main():
    x,y,z = input("Expression: ").split(" ")
    answer = float(do_math(x,y,z))
    print(round(answer,1))

def do_math(num1,expression,num2):
    num1 = int(num1)
    num2 = int(num2)
    match expression:
        case "+":
            return num1+num2
        case "-":
            return num1-num2
        case "/":
            return num1/num2
        case "*":
            return num1*num2


main()
