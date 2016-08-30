#!/usr/bin/python2.7

class Writer:
    def __init__(self, fname):
        self.fname = fname

    def write(self, op, state, cost):
        fout = open(self.fname + ".txt", "w")
        fout.write(op + "/t" + state + "/t" + cost)
        fout.close()
