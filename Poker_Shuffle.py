# -*- coding: utf-8 -*-

"""
Poker_Shuffle.py
Author: Rorical
Notator: EL_File4138

A Solution for CCBC12 Timeline E 1830.
暴力破解Faro Shuffle问题。
"""

def outerShuffle(arr):
    assert len(arr) % 2 == 0, "fuck you"
    length_d2 = int(len(arr) / 2)
    final = ""
    for i in range(length_d2):
        final += (arr[i])
        final += (arr[i + length_d2])
    return final

def innerShuffle(arr):
    assert len(arr) % 2 == 0, "fuck you"
    length_d2 = int(len(arr) / 2)
    final = ""
    for i in range(length_d2):
        final += (arr[i + length_d2])
        final += (arr[i])
    return final

def solve(initial, target):
    sequence = "000000"
    for i in range(64):
        out = initial[:]
        sequence = format(i, "b").zfill(5)
        for i in sequence:
            if i == "0":
                out = outerShuffle(out)
            else:
                out = innerShuffle(out)
        flag = True
        for index in range(len(target)):
            if target[index] != "?":
                if target[index] != out[index]:
                    flag = False
                    break
        if flag:
            break
    return sequence, out

initial = "FUAFRFOLSEHS"
puzzles = ["?F?O?????L??", "???S??E??S??", "??UA????E???", "F?????H???O?", "?????O?S???L", "S???F????A??", "FUROFAESFLHS"]

last = initial
for p in puzzles:
    ans, last = solve(last, p)
    print(ans)

initial = "UFFAFRLOESSH"
puzzles = ["?U???O?R????", "E??F??????F?", "?R????U??S??", "????EH??O???", "??A?????L??F", "SFOAURLHEFSF"]

last = initial
for p in puzzles:
    ans, last = solve(last, p)
    print(ans)