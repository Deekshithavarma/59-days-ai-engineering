my_list= ["rag","embedding","vector","pca","database"]
print(my_list)
print("--------------------------------")
print(len(my_list))

my_list.append("mcp")
print(my_list)
print("--------------------------------")
my_list.remove("embedding")
print(my_list)
print("--------------------------------")
print(my_list[0],my_list[-1])
print("--------------------------------")
print([word.upper() for word in my_list])

temp=[]
for word in my_list:
  count=0
  for i in word:
   count+=1
  temp.append(count) 

tot=sum(temp)
print(tot)
print("--------------------------------")
print("avg:",tot/len(my_list)) 

