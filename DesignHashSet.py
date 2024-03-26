# Design a HashSet without using any built-in hash table libraries.
"""
Implement `MyHashSet` class:
- void add(key) Inserts the value key into the HashSet.
- bool contains(key) Returns whether the value key exists in the HashSet or not.
- void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
 

Constraints:

- 0 <= key <= 106
- At most 104 calls will be made to add, remove, and contains.
"""
# Solution

class MyHashSet:
    def __init__(self):                       # Intitalizes a HashSet which creates a list of 'None' values to act as buckets for storing keys
        self.size = 1000                      # Size of the hash table
        self.buckets = [None] * self.size     # Initialize the hash table

    def hash_func(self, key: int) -> int:     # Hashing function that takes a key and return its hashed value
        return key % self.size                # here, the key modulo the size of the hash table
    
    def add(self, key: int) -> None:          # Adds a key to the HashSet. 
        index = self.hash_func(key)           # It calculates the hash value of the key,
        if not self.buckets[index]:           # find its corresponding bucket,
            self.buclets[index] = []          # and, appends the key to that bucket if it's not already present
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:       # Removes a key from the HashSet.
        index = self.hash_func(key)           # It calculates the hash value of the key, finds the corresponding bucket,
        if self.buckets[index] and key in self.buckets[index]:
            self.buckets[index].remove(key)   # and removes the key if it's present in that bucket.

    def contains(self, key: int) -> bool:     # Checks if a key exists in the HashSet. It calculates the hash value
        index = self.hash_func(key)           # of the key, find the corresposnding bucket, and checks if the key exists
        return self.bucket[index] and key in self.buckets[index]
    

# Your MyHashSet pbject will be instatntiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
