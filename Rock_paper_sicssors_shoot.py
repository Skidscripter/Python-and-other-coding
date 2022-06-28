from ast import Pass
from codecs import ignore_errors
import random
from turtle import end_fill

a = input("rock, paper, sis: ")
b = random.choice(['rock' ,'paper' ,'sis'])
print("they chose " + b)

if a == "rock" and b == "rock":
    print("tie and they chose " + b)
if a == "rock" and b == "rock":
    print("tie and they chose " + b)
if a == "rock" and b == "rock":
    print("tie and they chose " + b)
if a == "rock" and b == "sis":
    print("you win and they chose " + b)
if a == "paper" and b == "rock":
    print("you win and they chose " + b)
if a == "sis" and b == "paper":
    print("you win and they chose " + b)
if a == "sis" and b == "rock":
    print("you lose and they chose " + b)
if a == "paper" and b == "sis":
    print("you lose and they chose " + b)
if a == "rock" and b == "paper":
    print("you lose and they chose " + b)