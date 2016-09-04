#!/usr/bin/python2.7
import os.path

class Writer:
    def __init__(self, fname):
        self.fname = fname
        if (os.path.exists(fname+".txt")):
            os.remove(fname+".txt")

    def write(self, op, state, cost):
        _op = self.convert(op)
        self.fout = open(self.fname + ".txt", "a")
        self.fout.write(str(_op) + "\t" + str(state) + "\t" + str(cost) + "\n")
        self.fout.close()


    def diagWrite(self,op ,state, cost,reason):
        
        _op = self.convert(op)
        self.fout = open(self.fname + ".txt", "a")
        self.fout.write(str(_op) + "\t" + str(state) + "\t" + str(cost) + "\t" + reason + "\n")
        self.fout.close()

    def convert(self, op):
        if op == 0:
            tmp = "START"
        elif op == 1:
            tmp = "1R"
        elif op == 2:
            tmp = "2R"
        elif op == 3:
            tmp = "3R"
        elif op == -1:
            tmp = "1L"
        elif op == -2:
            tmp = "2L"
        elif op == -3:
            tmp = "3L"

        return tmp