class Ship:
    def __init__(self, lines):
        self.instructions = lines
        self.position = [0, 0]
        self.waypoint = [10, 1]
        # North [0, 1]  => 0
        # East  [1, 0]  => 1
        # South [0, -1] => 2
        # West  [-1, 0] => 3
        self.direction = 1
        self.direction_map = {
            0: [0, 1],
            1: [0, -1],
            2: [1, 0],
            3: [-1, 0],
        }

    def GetDestination(self):
        for instruction in self.instructions:
            self._RunInstruction(instruction)
        return abs(self.position[0]) + abs(self.position[1])
    
    def GetDestinationWithWaypoint(self):
        self.position = [0, 0]
        for instruction in self.instructions:
            self._RunInstructionWithWaypoiny(instruction)
        return abs(self.position[0]) + abs(self.position[1])

    def _RunInstruction(self, instruction):
        _type = instruction[0]
        _val = int(instruction[1:])
        _direction = self.direction_map[self.direction]
        if _type == 'F':
            self.position[0] += _direction[0] * _val
            self.position[1] += _direction[1] * _val
        elif _type == 'N':
            self.position[1] += _val
        elif _type == 'S':
            self.position[1] -= _val
        elif _type == 'E':
            self.position[0] += _val
        elif _type == 'W':
            self.position[0] -= _val
        elif _type == 'R':
            amount = _val // 90
            self.direction = (self.direction + amount) % 4
        elif _type == 'L':
            amount = _val // 90
            self.direction = (self.direction - amount) % 4

    def _RunInstructionWithWaypoiny(self, instruction):
        _type = instruction[0]
        _val = int(instruction[1:])
        if _type == 'F':
            self.position[0] += self.waypoint[0] * _val
            self.position[1] += self.waypoint[1] * _val
        elif _type == 'N':
            self.waypoint[1] += _val
        elif _type == 'S':
            self.waypoint[1] -= _val
        elif _type == 'E':
            self.waypoint[0] += _val
        elif _type == 'W':
            self.waypoint[0] -= _val
        elif _type in "LR":
            amount = _val // 90
            if _type == 'L':
                amount = 4 - amount
            w = self.waypoint.copy()
            if amount == 1:
                w[0] = self.waypoint[1]
                w[1] = -1 * self.waypoint[0]
            elif amount == 2:
                w[0] = -1 * self.waypoint[0]
                w[1] = -1 * self.waypoint[1]
            elif amount == 3:
                w[0] = -1 * self.waypoint[1]
                w[1] = self.waypoint[0]
            self.waypoint = w.copy()