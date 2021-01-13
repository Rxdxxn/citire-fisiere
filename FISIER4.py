#Ion şi Vasile joacă următorul joc: Ion spune un număr iar Vasile trebuie să găsească cinci numere consecutive, crescătoare,
# numărul din mijloc fiind cel ales de Ion.  
# Exemplu : Ion spune 10, Vasile spune 8 9 10 11 12. 
# Ajutaţi-l pe Vasile să găsească răspunsul mai repede. 
# Din fişierul « input.txt » se citeşte un număr, în fişierul « output.txt » - se înscrie consecutivitatea numerelor. 
with open("input.txt","r") as f:
    c=f.readline()    
    a=int(c)-2
    b=int(c)-1
    d=int(c)+1
    e=int(c)+2
with open("output.txt","w") as f:
    f.write(str(a))
    f.write(" ")
    f.write(str(b))
    f.write(" ")
    f.write(str(c))
    f.write(" ")
    f.write(str(d))
    f.write(" ")
    f.write(str(e))