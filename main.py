def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

func = multi_add(1,2,3,4,5,6,7,87,9)
print(func)

# conditional logic 
def main():
    x,y = 10, 500
    # conditional flow 
    if x < y :
        result = "x is less than y "
    else:
        result = "nothing works no more"

    print(result)

main()

# match case statement 
def master():
    x = 0
    while(x < 5):
        print(x)
        x = x + 1
    days = ["monday","tuesday","wednesday","thursday","friday"]
    # bullt in range function 
    for x in range(5,10):
        print(x)

    for d in days:
        print(d)
# no index counter for the forloop 
# break statement breaks execution of the loop when condition is met
# continue statement 
# enumerate function no index counter // enumerate 
    cities = ["london","paris","los angeles","paris","chicago","maimi"]
    for i,c in enumerate(cities):
        print(i,c)
        #
master()