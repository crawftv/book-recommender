#!/usr/bin/env python3

import pickle

def pickle_thing(obj, filename):
    with open(filename, "wb") as outfile:
        pickle.dump(obj, outfile)
        outfile.close()

def unpickle_thing(filename):
    with open(filename,"rb") as infile:
        obj = pickle.load(infile)
        infile.close()
        return obj
