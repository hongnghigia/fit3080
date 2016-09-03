#!/usr/bin/python2.7
import os.path

class Writer:
    def __init__(self, fname):
        self.fname = fname
        if (os.path.exists(fname+".txt")):
            os.remove(fname+".txt")

    def write(self, op, state, cost):
        self.fout = open(self.fname + ".txt", "a")
        self.fout.write(str(op) + "\t" + str(state) + "\t" + str(cost) + "\n")
        self.fout.close()
