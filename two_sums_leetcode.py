les = [1,3,11,2,7]
t= 9

dic = dict()
for i,v in enumerate(les):
    if v in dic:
        print([dic[v],i])
    else:
        dic[t-v]=i
print(dic)
## fucntion>>
def two_sum(les, target):
  aux_dic = {}
  for i,v in enumerate(les):
    if v in aux_dic:
      return [aux_dic[v],i]
    else:
      aux_dic[target-v] = i
  else:
    return []
