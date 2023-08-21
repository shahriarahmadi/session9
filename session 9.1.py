def addition(a,b):
    result={}
    result['s']=(a['s']*b['m']+ b['s']*a['m'])
    result['m']=a['m']*b['m']
    return result
def multiply(a,b):
    result={}
    result['s']=a["s"]*b["s"]
    result['m']=a["m"]*b["m"]
    return result
def division(a,b):
    result={}
    result['s']=(a['s']* b['m'])
    result['m']=(a['m']* b['s'])
    return result
def subtraction(a,b):
    result={}
    result['s']=(((a['m']*b['m']/a['m'])*a['s'])- (a['m']*b['m']/ b['m'])*b['s'])
    result['m']=(a['m']*b['m'])
    return result
def show(r):
    print(f'{r["s"]} / {r["m"]}')

def options():
    while 1:
        num1=float(input("enter top number for the first fraction: "))
        num2=float(input("enter bottom number for the first fraction: "))
        if num2==0:
            print("Invalid!")
            while 1:
                num2=float(input("try again: "))
                if num2!=0:
                    break
        num3=float(input("enter top number for the second fraction: "))
        num4=float(input("enter bottom number for the second fraction: "))
        if num4==0:
            print("Invalid!")
            while 1:
                num4=float(input("try again: "))
                if num4!=0:
                    break
                
        print(f"first fraction :\n  {num1}/{num2} and the second fraction: {num3}/{num4} ")
        break
        
    a={"s":num1 ,  "m":num2}
    b={"s":num3 ,  "m":num4} 

    print("choose your intended operation: 1-addition 2-multiply 3-subtraction 4-division")
    option=int(input())
    if option==1:
        show(addition(a,b))
    elif option==2:
        show(multiply(a,b))
    elif option==3:
        show(subtraction(a,b))
    elif option==4:
        show(division(a,b))
    else:
        print("Invalid! Try again.")


options()       
        
