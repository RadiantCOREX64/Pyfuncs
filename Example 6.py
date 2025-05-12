x = 3

y = 4

def myfunction (x,y):

#Local variable



    x += 3

    y -= 2

    global p

    p = x * y

    print (p)
    
myfunction(x , y)

print(x)

print(y)

print(p)