import json, sys

class JsonParser:
    def __init__(self, json):
        self.json = json
        self.queue = [json]

    def GetNonRedNumSum(self):
        result = 0
        while len(self.queue):
            element = self.queue.pop()

            # element is a list
            if type(element) == list:
                for item in element:
                    if type(item) == int:
                        result += item
                    elif type(item) == list or type(item) == dict:
                        self.queue.append(item)

            # element is a dict
            elif type(element) == dict:
                if self._IsNonRedDict(element):
                    for key in element:
                        item = element[key]
                        if type(item) == int:
                            result += item
                        elif type(item) == list or type(item) == dict:
                            self.queue.append(item)

        return result

    def _IsNonRedDict(self, d):
        for val in d.values():
            if val == "red":
                return False
        return True
    