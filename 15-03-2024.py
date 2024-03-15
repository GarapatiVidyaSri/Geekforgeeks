class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def sort(self, h1):
        temp=h1
        l=[]
        while temp:
            l.append(temp.data)
            temp=temp.next
        l.sort()
        i=0
        temp2=h1
        while temp2:
            temp2.data=l[i]
            i+=1
            temp2=temp2.next
        return h1
            
            
        