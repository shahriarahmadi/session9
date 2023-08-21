def addition(a,b):
    result={}
    result["hr"]=a["hr"]+b["hr"]
    result["min"]=a["min"]+b["min"]
    result["sec"]=a["sec"]+b["sec"]
    if  result["sec"]>=60:
        result["sec"]-=60
        result["min"]+=1
        
    if  result["min"]>=60:
        result["hr"]+=1
        result["min"]-=60
        
    if  result["hr"]>=24:
        print("Invalid!")
        result={"hr":0 , "min":0 , "sec":0}
    return result    


def subtraction(a,b):
    result={}
    result['hr']=b['hr']-a['hr']
    result['min']=b['min']-a['min']
    result['sec']=b['sec']-a['sec']
    if result["sec"]<0:
       result["min"]-=1
       result["sec"]+=60
        
    if result["min"]<0:
       result["hr"]-=1
       result["sec"]+=60
        
    if result["hr"]<0:
        print("Invalid!")
        
        
    return result


def show(result):
    print(f'{result["hr"]}: {result["min"]} : {result["sec"]}')


a={"hr":int(input("first hour: ")) , "min":int(input("first minute: ")) , "sec":int(input("first second: "))}
b={"hr":int(input("second hour: ")) , "min":int(input("second minute: ")) , "sec":int(input("second second: "))}

result_ad= addition(a, b)
show(result_ad)

result_sub= subtraction(a, b)
show(result_sub)