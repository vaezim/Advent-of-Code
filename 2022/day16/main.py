from Valve import Valve
from time import perf_counter


with open('input.txt', 'r') as file:
    lines = file.readlines()

valve_map = []
valveName2idx_dict = {}
valveIdx2name_dict = {}
valve_flow = []
for i, line in enumerate(lines):
    words = line.strip().split()

    assert words[1] not in valveName2idx_dict
    valveName2idx_dict[words[1]] = i # name to index
    valveIdx2name_dict[i] = words[1]

    valve_flow.append(int(words[4][5:-1]))

    if 'valves' in line:
        valve_map.append(line[line.index('valves')+6:].strip().split(', '))
    else:
        valve_map.append(line[line.index('valve')+5:].strip().split(', '))

##### Part 1 #####

valver = Valve(valve_map, valveName2idx_dict, 
                          valveIdx2name_dict, valve_flow)
valver.time = 30

part1_start = perf_counter()
lf = valver.findLargestFlow(start='AA', time_left=valver.time, # takes around 3 seconds
                            players_left=0, opened_valves=set())
part1_end = perf_counter()

print(f"Answer of Part 1: {lf} | time elapsed = " + "{0:.2f}".format(part1_end-part1_start) + " seconds")

##### Part 2 #####

valver.reset()
valver.time = 26

part2_start = perf_counter()
lf = valver.findLargestFlow(start='AA', time_left=valver.time, # takes around 2 minutes
                            players_left=1, opened_valves=set())
part2_end = perf_counter()

print(f"Answer of Part 2: {lf} | time elapsed = " + "{0:.2f}".format(part2_end-part2_start) + " seconds")
