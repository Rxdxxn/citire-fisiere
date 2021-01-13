#Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre.
#Numărul globuleţelor albe se citeşte din fişierul « globulet.txt ». 
#Câte globuleţe are brăduţul, ştiind că numărul de globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe, 
#iar globuleţele albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii. 
#Numărul total de globuleţe este înscris în fişierul « bradut.txt » 

with open("globulet.txt","r") as f:
    a=f.readline()
    b=int(a)+3
    c=(int(a)+int(b))-2
    d=int(a)+int(b)+int(c)
with open("bradut.txt","w") as f:  
    f.write(str(d))

