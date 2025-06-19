my_list=[]
extracted_list=[]
rev_extracted_list=[]

for i in range(1,11):
    my_list.append(i)
print (my_list)

extracted_list=my_list[-5:]
print(extracted_list)
for x in range(len (extracted_list)-1,-1,-1):
    
    rev_extracted_list.append(extracted_list[x])
print(rev_extracted_list)