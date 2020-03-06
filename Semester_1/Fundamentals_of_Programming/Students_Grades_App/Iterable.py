


class Iterable():

    def __init__(self):
        self.elems=[]
        self.idx=-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx== len(self.elems):
            raise StopIteration
        self.idx+=1
        return self.elems[self.idx]


    def __setitem__(self, idx, value):
        self.elems[idx]=value

    def __delitem__(self, idx):
        self.elems.pop(idx)

    def append(self,value):
        self.elems.append(value)

    def __len__(self):
        return len(self.elems)

    def insert(self,idx,obj):
        self.elems.insert(idx,obj)

    def __getitem__(self, item):
        return self.elems[item]

    def pop(self,idx):
        self.__delitem__(idx)

    def clear(self):
        self.elems.clear()
