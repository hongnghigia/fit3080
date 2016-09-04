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

    def writeNode(self,node,openset,closedset,string):
        self.fout = open(self.fname + ".txt","a")
        self.fout.write("----------------------------------\n")
        self.fout.write("EXPANDED\n")
        self.fout.write(str(node.identifier) + "\n")
        self.fout.write(str(node.g) + "\n")
        self.fout.write(str(openset[0:5]))
        self.fout.write("\n")
        self.fout.write(str(closedset[0:5]))

        self.fout.close()

    def writeNewNode(self,node):
        op = self.convert(node.op)
        self.fout = open(self.fname + ".txt","a")
        self.fout.write("------------------------------------\n")
        self.fout.write("NEWLY GENERATED \n")
        self.fout.write("Op" + "\t" + str(op) + "\n")
        self.fout.write("ID" + "\t" + str(node.identifier) + "\n")
        self.fout.write("Parent" + "\t" + node.parent.string + "\n")
        self.fout.write("G" + "\t" + str(node.g) + "\n")
        self.fout.write("H" + "\t" + str(node.h) + "\n")
        self.fout.write("F" + "\t" + str(node.f) + "\n")
        self.fout.write("\n")
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
