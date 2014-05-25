# -*- coding: utf-8 -*-
"""
Created on Sat May 24 12:46:14 2014

@author: sophie
"""
import markov

file_ = open("sherlock.txt")
markovgen = markov.Markov(file_)
print markovgen.generate_markov_text(50)
