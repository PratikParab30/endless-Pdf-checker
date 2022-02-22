import os
import re

fcrg=r".*.pdf"
ar1=[]
dr=input("Provide path:")
print("****************************")
for fo1,fo2,fo3 in os.walk(dr,topdown=True):
    ar2=[]
    ar2.append(fo1)
    for i in fo3:
        mh=re.match(fcrg,i)
        if "None" != str(mh):
            print(mh.group(),end="\n")
            ar2.append(mh.group())
    ar1.append(ar2)

while True:
    condc=False
    print("\n1.Search a file:")
    print("2.Exit")
    chs=input("\nEnter Your choice:")
    try:
        chs=int(chs)
        if(chs==1):
    
            nmof=input("Enter any keyword from file name for searching purpous: ")         
            for i in ar1:
                for j in range(0,len(i)):
                    if(j!=0):
                       nmof1=re.search(nmof,i[j])
                       if nmof1:
                           path1=f"{i[j]} present in {i[0]} location and full path is {os.path.join(i[0],i[j])}" 
                           print(path1)
                           print("")
                           condc=True
            if condc:
                break
            else:
                print("\n::File not found , Try again::\n")  
        elif(chs==2):
            break
        else:
            print("\nWrong Choice Entred::\n")
                
    except:
        print("\n::Please enter Integer choice::\n")
    