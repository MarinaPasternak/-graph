import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def  type_of_num(input_value):
    while(input_value.isdigit()==0):
        print('wrong value')
        input_value=input()
    return int(input_value)

def  type_of_list(input_value,num):
    mynewlist = [int(s) for s in input_value if s.isdigit() and (s =="1" or s=="0")]
    if(len(mynewlist)==num):
        return  mynewlist
    else:
        print('wrong value')
        return type_of_list(input().split(),num)

def matrix_simetric(matrix, new_num_rows_colum ):
    answer = True
    for k in range(0,new_num_rows_column-1):
        for l in range(k+1,new_num_rows_column):
            if matrix[k][l]!=matrix[l][k]:
                answer=False
                break
        if answer==True:
            print('Matrix  simetric')
            return answer
        else:
            print('Matrix  nonsimetric')
            return answer


print('print num of collums and rows')
num_rows_column=input()
new_num_rows_column = type_of_num(num_rows_column);
print('matrix')
A = [[int(j) for j in  type_of_list(input().split(),new_num_rows_column)] for i in range(new_num_rows_column)]
if matrix_simetric(A, new_num_rows_column):
    G = nx.from_numpy_matrix(np.matrix(A), create_using=nx.DiGraph)
    layout = nx.spring_layout(G)
    nx.draw(G, layout)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos=layout)
    plt.show()
else:
    print('wrong')