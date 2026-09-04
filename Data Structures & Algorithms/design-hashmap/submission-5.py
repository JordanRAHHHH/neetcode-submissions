class MyHashMap:

    def __init__(self):
        self.table = [[] for i in range (100)]

    def put(self, key: int, value: int) -> None:
        index = hash(key) % len(self.table)

        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                self.table[index][i][1] = value
                return
        self.table[index].append([key, value])

    def get(self, key: int) -> int:
        index = hash(key) % len(self.table)

        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                return self.table[index][i][1]
        return -1

    def remove(self, key: int) -> None:
        index = hash(key) % len(self.table)

        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                self.table[index].pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)