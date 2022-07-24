def collatz(number):
    if number%2==0:
        result=number//2
        return result
    else:
        result=3 * number + 1
        return result
        
def main():
    counter=0
    num=int(input("Enter an integer: "))
    while num!=1:
        num=collatz(num)
        counter+=1
        print(num)
    print(f"Total of {counter} steps")
            

if "__main__"==__name__:
    main()
            