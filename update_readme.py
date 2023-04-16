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

for year in range(2015,2023):
    progress = getProgress(year)
    file.write(f"- **{year}** ![](https://progress-bar.dev/{progress}/?scale=25&width=300&suffix=/25)\n")

file.close()
