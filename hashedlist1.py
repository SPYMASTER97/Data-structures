# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:08:36 2021

@author: saswa
"""

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
        return
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] =  None
    
    
if __name__ == '__main__':
    t = HashTable()
    t["march 3"] = 2536
    t["september 23"] = 6463
    t["January 23"] = 644
    t["May 12"] = 6464
    del t["January 23"]
    print(t.arr)