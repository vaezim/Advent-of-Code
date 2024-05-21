class Plants:
    def __init__(self, text):
        self.padding = 100
        self.initial_state, self.maps = self._ParseText(text)

    def Pass20Generations(self):
        state = self.initial_state
        starting_index = 0
        for _ in range(20):
            state, offset = self._GenerateNextState(state)
            starting_index += offset
        return self._GetSumPlantedPotIndices(state, starting_index)

    def _GetSumPlantedPotIndices(self, state, starting_index):
        sum = 0
        for i in range(len(state)):
            if state[i] == '#':
                sum += (i + starting_index)
        return sum

    def Pass50BillionGenerations(self):
        N = 50_000_000_000
        visited_map = {self.initial_state : (0, 0)}
        state = self.initial_state
        sum_offsets = 0
        i = 0
        for _ in range(1000):
            i += 1
            state, offset = self._GenerateNextState(state)
            sum_offsets += offset
            visited_map[state] = (offset, i)
        return self._GetSumPlantedPotIndices(state, N-i+sum_offsets)

    def _GenerateNextState(self, state):
        state = "."*self.padding + state + "."*self.padding
        next_state = ".."
        for i in range(2, len(state)-2):
            next_state += self.maps[state[i-2:i+3]]
        offset = next_state.find('#')-self.padding
        next_state = next_state[next_state.find('#'):next_state.rfind('#')+1]
        return next_state, offset

    def _ParseText(self, text):
        initial_state = text[0]
        initial_state = initial_state[initial_state.find(':')+1:].strip()
        maps = {}
        for i in range(2, len(text)):
            left = text[i].strip()[:5]
            right = text[i].strip()[-1]
            maps[left] = right
        return initial_state, maps