# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:33:59 2021

@author: saswa
"""

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print("Linked List in Empty")
            return
        
        itr = self.head
        liststr = ''
        
        while itr:
            liststr += str(itr.data) + "-->"
            itr = itr.next
        print(liststr)
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
            
    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid input")
        
        if index == 0:
            self.head = self.head.next
            return
            
        count = 0
        itr = self.head
        while count < index - 1:
            itr = itr.next
            count+=1
        
        itr.next = itr.next.next
        
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid input")
        
        elif index == 0:
            self.head = data
            self.next = None
            return
        
        count = 0
        itr = self.head
        while count < index - 1:
            itr = itr.next
            count+=1
        
        node = Node(data, itr.next)
        itr.next = node
        
        
        
        
        
        
        
            
            
if __name__ == '__main__':
    l1 =  LinkedList()
    l1.insert_values(['abc','cdf','ada','addad'])
    l1.get_length()
    l1.insert_at(2, "tytu")
    l1.print()