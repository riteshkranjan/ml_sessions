
try:
    f = open("b.txt","r")  
    #filename, mode = r , w ,a, r+
except Exception as e:
    print(type(e))
    print(e) 
finally:
    print("in finally block")
    
print("reading a.txt now")

f = open("a.txt","r")
print(f.readlines())
f.close()


