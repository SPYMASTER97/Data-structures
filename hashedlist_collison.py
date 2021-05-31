# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:46:27 2021

@author: saswa
"""

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
                
        
        
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))
            
            
    def __delitem__(self,key):
        h = self.get_hash(key)
        
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
        
                
            

if __name__ == '__main__':
    t = HashTable()
    t["march 6"] = 252
    t["May 23"] = 536
    t["march 17"] = 36
    print(t.arr)
    print(t["march 17"])
    del t["May 23"]
    print(t.arr)