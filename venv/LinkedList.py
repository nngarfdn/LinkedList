# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:58:24 2020

@author: hp
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext

    def setData(self, newData):
        self.data = newData


class LinkedList:
    def __init__(self):
        self.head = None

    def countNode(self):
        jml = 0
        p = self.head
        while p is not None:
            jml = jml + 1
            p = p.getNext()
        return jml

    def cekData(self, namaData):
        p = self.head
        if self.isEmpty():
            return False
        else:
            while p is not None :
                if namaData == p.getData() :
                    return True
                    break
                elif p.getNext() == None:
                    return False
                p = p.getNext()


    def cariData(self, namaData):
        p = self.head
        dataKe = 0
        if self.isEmpty() :
            return -1
        else:
            while p is not None:
                dataKe = dataKe + 1
                if namaData == p.getData():
                    return dataKe
                    break
                elif p.getNext() == None:
                    return False
                p = p.getNext()


    def sisipData(self, dataApa, nilaiData):
        if self.isEmpty() :
            return None
        else:
            p = self.head

            while(p.data is not dataApa) :
                p = p.getNext()
                if(p is None) :
                    self.insertLast(dataApa)
                    return True

            newNode = Node(nilaiData)
            dataSetelah = p.getNext()
            p.setNext(newNode)
            (p.getNext()).setNext(dataSetelah)

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def insertFirst(self, data):
        nodeBaru = Node(data)
        nodeBaru.setNext(self.head)
        self.head = nodeBaru

    def deleteFirst(self):
        if self.isEmpty():
            return None
        else:
            yangKeluar = self.head
            self.head = yangKeluar.getNext()
            return yangKeluar

    def insertLast(self, data):
        if self.isEmpty():
            self.insertFirst(data)
        else:
            p = self.head
            while p.getNext() is not None:
                p = p.getNext()

            nodeBaru = Node(data)
            p.setNext(nodeBaru)

    def deleteLast(self):
        if self.isEmpty():
            return None
        elif self.head.getNext() == None:
            yangKeluar = self.head
            self.head = None
            return yangKeluar
        else:
            p = self.head
            while p.getNext().getNext() != None:
                p = p.getNext()

            yangKeluar = p.getNext()
            p.setNext(None)  # sama dengan p.next = None
            return yangKeluar

    def deleteNode(self, dataDihapus):
        if (self.isEmpty()):
            return None
        else:
            p = self.head
            # Berhenti loop sebelum menemukan dataDihapus
            # maka akan didapatkan |data sebelum dataDihapus|
            # |Data sebelum dataDihapus| dibutuhkan untuk
            # mengganti data setelah |data sebelum dataDihapus| (yaitu dataDihapus)
            # dengan data setelah dataDihapus
            while ((p.getNext()).data is not dataDihapus):
                p = p.getNext()
                if (p.getNext() is None):
                    return False

            dataSetelah = (p.getNext()).getNext()
            p.setNext(dataSetelah)

    def printAll(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.getNext()


LL = LinkedList()
LL.insertFirst("Nussa")
LL.insertFirst("Rara")
LL.insertLast("Anta")
LL.sisipData("Rara", "Ariq")
print(LL.deleteNode("Nussa"))
LL.printAll()
