#!/usr/bin/python3
import os

def getProgress(year: int):
    if os.path.isdir(f"{year}"):
        return len(os.listdir(f"{year}"))
    return -1

file = open("README.md", 'w+')

# Header & description
file.write("# Advent of Code\n")
file.write("Python/C++ solutions for [Advent of Code](https://adventofcode.com/) challenges.\n\n")

# Progress bars
file.write("## Progress\n")

for year in range(2023,2014,-1):
    progress = getProgress(year)
    file.write(f"- **{year}** ![](https://progress-bar.dev/{progress}/?scale=25&width=300&suffix=/25)\n")

# Calendars
file.write("## Calendars")
file.write("### 🌟 2015 🌟")
file.write("https://github.com/vaezim/Advent-of-Code/assets/91099081/75a16dda-df61-48a0-8eae-c149bd9d589c")

file.close()
