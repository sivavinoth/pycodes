def find():
    flag = []
    smlist = ['a','b','c','a']
    for dup_count in smlist:  
        if smlist.count(dup_count)>1:
            if dup_count not in flag:
             flag.append(dup_count)
            
    print(flag)
find()

print("hi")


