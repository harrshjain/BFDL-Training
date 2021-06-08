d = {'a' : 'apple', 'b' : 'banana', 'c' : {'d' : 'dog', 'e' : 'eggs', 'f' : {'g' : 'gun'}}}

def getValues(d, lst):
    for x, y in d.items():
        if type(d[x]) is dict:
            getValues(d[x], lst)
        else:
            lst.append(y)
    return lst

def getOutput(d, key):
    lst = []
    for a, b in d.items():
        if a == key:
            if type(d[a]) is dict:
                return getValues(d[a], lst)
            else:
                return b
        if type(d[a]) is dict:
            return getOutput(d[a], key)

def get(d, key):
    temp = getOutput(d, key)
    if type(temp) is list:
        print(*temp)
    else:
        print(temp)

        
get(d,'c')
print(getOutput(d,'f'))
print(getOutput(d,'b'))
print(getOutput(d,'e'))
