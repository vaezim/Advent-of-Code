from copy import deepcopy

class Image:
    def __init__(self, img_line):
        self.img_ling = img_line
        self.width = 25
        self.height = 6

    def GetPart1(self):
        self.layers = []
        for i in range(0, len(self.img_ling), self.width*self.height):
            layer = self.img_ling[i:i+self.width*self.height]
            layer_list = []
            for j in range(0, len(layer), self.width):
                layer_list.append(layer[j:j+self.width])
            self.layers.append(deepcopy(layer_list))
        min_zero = float("inf")
        min_zero_index = 0
        for i, l in enumerate(self.layers):
            num_zero = 0
            for item in l:
                num_zero += item.count('0')
            if num_zero < min_zero:
                min_zero = num_zero
                min_zero_index = i
        num_one, num_two = 0, 0
        for item in self.layers[min_zero_index]:
            num_one += item.count('1')
            num_two += item.count('2')
        return num_one * num_two
    
    def GetPart2(self):
        message = deepcopy(self.layers[0])
        message = list(map(lambda x: list(x), message))
        for i in range(self.height):
            for j in range(self.width):
                for l in self.layers:
                    if l[i][j] != '2':
                        message[i][j] = l[i][j]
                        break
        msg = "\n"
        for item in message:
            msg += ''.join(item)
            msg += '\n'
        return msg