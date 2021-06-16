import numpy as np
import os
def main():
    arr2 = [ j*pow(10,i)  for j in range(1, 11) for i in range(2,6)]

    for canti_data in arr2:
        rng = np.random.default_rng()
        arr= rng.choice(canti_data+1 ,size=canti_data)
        str1=""
        cont=0
        for x in np.nditer(arr):
            cont+=1
            if cont!=arr.size: # es sin -1 porque el contador esta arriba :v
                str1+=str(x)+"\n"
            else:
                str1+=str(x)
        #print(str1)
        file = open("./data2/archivo"+str(canti_data)+".txt", "w")
        file. write(str1)    
        file. close()
    
    # print(array_from_file.size)

main()