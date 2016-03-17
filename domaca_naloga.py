

x=int(raw_input("Ugani stevilko "))
if x==10:
    print("bravo")

while True:
    if x > 10:
       print ("prevec")
       x=int(raw_input("Ugani stevilko "))

    elif x <10:
        print ("premalo")
        x=int(raw_input("Ugani stevilko "))
    else:
        print("bravo")
        break

print("konec programa")
