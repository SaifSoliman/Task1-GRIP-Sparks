from py_expression_eval import Parser
import math
parser = Parser() #Parser is the main class of the library that contains the methods to parse, evaluate and simplify mathematical expressions

#pyexperssion eval is a Mathematical Expression Evaluator
#downloaded from github https://github.com/axiacore/py-expression-eval

flag =0
eqn = input("Please enter the equation: ")
valOfA = float(input("Please enter the value of A: "))
valOfB = float(input("Please enter the value of B: "))
tol = float(input("Please enter the value of tol: "))
fOfA = float(parser.parse(eqn).evaluate({'x' : valOfA}))
fOfB = float(parser.parse(eqn).evaluate({'x' : valOfB}))
numOfIterations = float(math.log((valOfB-valOfA)/tol))/float(math.log(2))
valOfC = (valOfA + valOfB) / 2
fOfC = float(parser.parse(eqn).evaluate({'x' : valOfC}))
Root = "."
if fOfC < 0:
    if fOfA > 0:
        Root = "C&A"
    else:
        Root = "C&B"
else:
    if fOfA > 0:
        Root = "C&B"
    else:
        Root = "C&A"

i = 2 #first iteration already made
#Saif Eldeen Soliman Abdeen 
#saifsoliman088@gmail.com
print("i=1, A=", valOfA, " B=", valOfB, " C=", valOfC, " f(A)=", fOfA, " F(B)=", fOfB, " F(C)=", fOfC, " Root=",Root, "\n" )

while i < numOfIterations:
    if Root == "C&A" :
        valOfB = valOfC
    else :
        valOfA = valOfC
        
    fOfA = float(parser.parse(eqn).evaluate({'x' : valOfA}))
    fOfB = float(parser.parse(eqn).evaluate({'x' : valOfB}))
    valOfC = (valOfA+valOfB) / 2
    fOfC = float(parser.parse(eqn).evaluate({'x' : valOfC}))
    print("i=", i , " A=", valOfA, " B=", valOfB, " C=", valOfC, " f(A)=", fOfA, " F(B)=", fOfB, " F(C)=", fOfC, " Root=",Root, "\n" )
    #check if f(c) < tol, if it is then the root is found andd set the flag to 1 and break don't continue
        
    if abs(fOfC) < tol:
        print("The Root is Found, C = ", valOfC)
        flag = 1
        break
    i = i+1
if flag == 0 :
    print("Root found, C = ", valOfC)
