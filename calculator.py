
print("1.   addtion")
print("2.   subtraction")
print("3.   multply")
print("4.   devision")
print("select any one of the options")
Var = input("option")
Data = input("num")
Data2 = input("num")
if Var == 1:
    Ans = Data+Data2
    print(Ans)
elif Var == 2:
    Ans = Data-Data2
    print(Ans)
elif Var == 3:
    Ans = Data*Data2
    print(Ans)
else:
    Ans = Data/Data2
    print(Ans)