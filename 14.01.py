with open("input.txt","r") as f:
    a=f.readline()
x=0
y=0
z=0
w=0
for i in a:
    if ord(i) in range(65,91):
        x+=1
with open("litereA.txt","w") as f:
    f.write(str(x))
for i in a:
    if ord(i) in range(97,123):
        y+=1
with open("litereB.txt","w") as f:
    f.write(str(y))
for i in a:
    if ord(i) in range(49,58):
        z+=1
with open("cifre.txt","w") as f:
    f.write(str(z))
for i in a:
    if ord(i)==42 or ord(i)==43 or ord(i)==45 or ord(i)==47:
        w+=1
with open("operatori.txt","w") as f:
    f.write(str(w))