class Node:
    def __init__(self, num_children):
        self.metadata = []
        self.children = [] # Node()
        self.num_children = num_children

    def AddChild(self, child):
        self.children.append(child)

    def AddMetadata(self, data):
        self.metadata.append(data)

    def GetValue(self):
        if len(self.children) == 0:
            return sum(self.metadata)
        val = 0
        for idx in self.metadata:
            if idx > len(self.children):
                continue
            val += self.children[idx-1].GetValue()
        return val
    
    def __str__(self):
        s = f"Num children = {len(self.children)}\n"
        s += "Metadata: "
        for i in self.metadata:
            s += f"{i}, "
        return s

class Tree:
    def __init__(self, text):
        self.nodes = [] # Node()
        self.sum_metadata = 0
        self.nums = list(map(int, text.strip().split()))

    def GetRootNodeValue(self):
        root = self.nodes[0]
        return root.GetValue()

    def GetSumMetadata(self):
        self._ParseNode(0)
        return self.sum_metadata

    def _ParseNode(self, ptr):
        num_children = self.nums[ptr]
        num_metadata = self.nums[ptr+1]
        node = Node(num_children)
        self.nodes.append(node)
        ptr += 2
        for _ in range(num_children):
            ptr, child = self._ParseNode(ptr)
            node.AddChild(child)
        for _ in range(num_metadata):
            node.AddMetadata(self.nums[ptr])
            self.sum_metadata += self.nums[ptr]
            ptr += 1
        return ptr, node