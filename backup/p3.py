n= int(input())
T= {}
root= list(range(1, n+1))    #所有可能的根節點答案

for i in range(1,n+1):
    line= input().split()
    n_line= list(map(int, line))[1:]
    T[i]= n_line

    for k in n_line:
        root.remove(k)

def h(v):
    c_nodes=T[v] #子節點
    if c_nodes==[]:
        return 0
    else:
        return max(map(h,c_nodes))+1
    
print(root[0])
print(sum(map(h, range(1, n+1))))
