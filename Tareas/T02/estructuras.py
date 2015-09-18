import sistema
import dis
import sys

class listObject():
    def __init__(self,value,dad=None,son=None):
        self.value = value
        self.dad = dad
        self.son = son
    def __repr__(self):
        return str(self.value)


class myList():
    def __init__(self,mainElement=None,string=None):
        self.mainElement = mainElement
        self.lastElement = mainElement
        self.length = 0

    def __repr__(self):
        ret = ''
        for i in range(self.length):
            if i == self.length - 1:
                ret += '{}'.format(self[i].value)
            else:
                ret += '{}, '.format(self[i].value)
        return '[' + ret + ']'

    def append(self,value):
        if self.lastElement == None:
            self.mainElement = listObject(value)
            self.lastElement = listObject(value)
            self.length += 1
            return
        elif self.length == 1:
            a = listObject(value)
            self.mainElement.son = a
            self.lastElement.son = a
            self.lastElement.son.dad = self.lastElement
            self.lastElement = self.lastElement.son
            self.length += 1
        else:
            self.lastElement.son = listObject(value)
            self.lastElement.son.dad = self.lastElement
            self.lastElement = self.lastElement.son
            self.length += 1

    def pop(self,position=None):
        if not position:
            position = self.length
        def _pop(node,position = self.length):
            ret = None
            if position > self.length:
                return ret
            if node != None:
                ret = node
                if _pop(node.son,position) != None:
                    ret = _pop(node.son,position)
                    node.son = None
                    self.length -= 1
            return ret
        return _pop(self.mainElement,position)

    def __setitem__(self,key,value):
        self[key].value = value

    def __getitem__(self,n):
        if n >= self.length:
            raise IndexError('Index out of range, stupid')
            return
        node = self.mainElement
        for i in range(n):
            node = node.son
        return node
    
    def __len__(self):
        return self.length

    def __contains__(self,n):
        node = self.mainElement
        while node != None:
            if node.value == n:
                return True
            else:
                node = node.son
        return False

    def __iter__(self):
        for i in range(self.length):
            yield self[i]

    def __str__(self):
        return self.__repr__()

    def __add__(self,other):
    	for element in other:
    		self.append(other.value)


lista = myList()#.append(1)
lista.append(1)
lista.append(2)
lista.append(3)
lista[0] = 2
print(lista)

#help(list)   

