# Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

# Implement the AllOne class:

# AllOne() Initializes the object of the data structure.
# inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
# dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
# getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
# getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
# Note that each function must run in O(1) average time complexity.

 

# Example 1:

# Input
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# Output
# [null, null, null, "hello", "hello", null, "hello", "leet"]

# Explanation
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "leet"

class AllOne:

    def __init__(self):
        self.storage = []
        self.memo = {}
        

    def inc(self, key: str) -> None:
        if key in self.memo:
            self.memo[key] += 1
        else:
            self.memo[key] = 1
        idx = self.memo[key] - 1
        if idx > 0:
            self.storage[idx - 1].remove(key)
        if idx == len(self.storage):
            self.storage.append({key}) 
        else:
            self.storage[idx].add(key)
            

    def dec(self, key: str) -> None:
        self.memo[key] -= 1
        idx = self.memo[key]
        self.storage[idx].remove(key)
        if not self.storage[-1]:
            self.storage.pop()
        if idx > 0:
            self.storage[idx - 1].add(key)
        else:
            self.memo.pop(key)
        

    def getMaxKey(self) -> str:
        if not self.storage:
            return ""
        r = self.storage[-1].pop()
        self.storage[-1].add(r)
        return r
        

    def getMinKey(self) -> str:
        for i in range(len(self.storage)):
            if self.storage[i]:
                r = self.storage[i].pop()
                self.storage[i].add(r)
                return r
        return ""
                
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()