#!/usr/bin/python3
import os

def getProgress(year: int):
    progress = ['🔲'] * 25
    for day in os.listdir(f"{year}"):
        n = int(day[3:])
        progress[n-1] = '✅'
    return progress

file = open("README.md", 'w+')

# Header & description
file.write("# Advent of Code\n")
file.write("Python/C++ solutions for [Advent of Code](https://adventofcode.com/) challenges.\n\n")

# Progress bars
file.write("## Progress\n")

for year in range(2024,2014,-1):
    progress = getProgress(year)
    progress = ''.join(progress)
    file.write(f"- **{year}** {progress}\n")

# Calendars
file.write("\n## Calendars\n")
file.write("### 🌟 2015 🌟\n")
file.write("https://github.com/vaezim/Advent-of-Code/assets/91099081/75a16dda-df61-48a0-8eae-c149bd9d589c\n")
file.write("### 🌟 2016 🌟\n")
file.write("https://github.com/vaezim/Advent-of-Code/assets/91099081/78d9c256-906c-4fa4-a54a-769feb5325bf\n")
file.write("### 🌟 2017 🌟\n")
file.write("https://github.com/vaezim/Advent-of-Code/assets/91099081/8532d2b3-af40-41e2-95a1-651e33a5a3c0\n")
file.close()