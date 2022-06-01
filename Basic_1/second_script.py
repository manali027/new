#!/usr/bin/python3
import os, sys

def first():
    print("this is a the first function")

def second():
    print("this is a the SECOND function")
    third()

def third():
    print("this is a the THIRD function")

first()
second()


