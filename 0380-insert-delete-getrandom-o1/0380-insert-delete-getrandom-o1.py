class RandomizedSet:

    def __init__(self):
        self.data = []
        self.idx_map = {}   # hashmap for value : index mapping

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        self.data.append(val)   # add value to the list
        self.idx_map[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False
        last_element = self.data[-1]
        idx_to_remove = self.idx_map[val]
        self.data[idx_to_remove] = last_element
        self.idx_map[last_element] = idx_to_remove
        self.data.pop()
        del self.idx_map[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()