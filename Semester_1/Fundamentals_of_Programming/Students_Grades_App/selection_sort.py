'''
SELECTION SORT
while there still are items to be sorted, the minimum/maximum item from the list is appended to the sorted list
the algorithm returns the sorted list
'''

def selectionSort(list,key):
    sortedlist=[]

    while len(list)>0:
        m=min(list,key=key)
        mi=list.index(m)
        sortedlist.append(m)
        list.pop(mi)

    return sortedlist



def filter(l, fct):
    list = []
    for i in l:
        if fct(i):
            list.append(i)
    return list