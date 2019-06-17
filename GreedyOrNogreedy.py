#貪欲検索と，非貪欲検索
import re

#(HaHaHa)
greedy = re.compile(r'(Ha){3,5}')

#(HaHaHa|HaHaHaHa|HaHaHaHaHa)
nogreedy = re.compile(r'(Ha){3,5}?')

#貪欲
mo = greedy.search('HaHaHaHaHa')
if mo:
    print(mo.group())
else:
    print("matchしてない")

#非貪欲
mo = nogreedy.search('HaHaHaHaHa')
if mo:
    print(mo.group())
else:
    print("matchしてない")
