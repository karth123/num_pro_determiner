def harshad_num(harsh_num):
    Y = sum(map(int, str(harsh_num)))
    if harsh_num % Y == 0:
        print("(H)is a harshad number ""(",harsh_num,")")
    else:
        print("(H)It is not a harshad number ""(", harsh_num, ")")


def div_check(div_num):
    divisors = [1,2,3,4,5,6,7,8]
    for i in divisors:
        i = i+1
        if div_num % i == 0:
            print(" (D)It is divisible by", i)
        else:
            print(" (D)It is not divisible by", i)


def pr_test(pr_num):
    for x in range(2, pr_num):
        if pr_num % x == 0:
            print("   (C)Is a composite number ""(", pr_num, ")")
            break
        else:
            print("   (P)Is a prime number""(", pr_num, ")")


print(" Python program which verifies a given number as one of many special numbers")
rand_num = int(input("Enter a positive natural number :- "))

print(" Harshad number:- It is a number which is divisible by the sum of its digits")
print(" Divisibility:- Checks if a number is divisible by the numbers 10>n>1")
print("Prime test:- Checks if a number is prime or composite")
print("The codes for determining the properties of a number are given below:- ")
print("H- Harshad number")
print("D:- Divisibility")
print("P:- Prime test")
print("A:- All")
A = str(input("Enter a letter associated with the given property:- "))
if A == "h":
     harshad_num(rand_num)
elif A == "d":
    div_check(rand_num)
elif A == "p":
    pr_test(rand_num)
elif A == "a":
    harshad_num(rand_num)
    div_check(rand_num)
    pr_test(rand_num)
    print("Thanks for making my work more difficult")