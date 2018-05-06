from collections import defaultdict
class Trie:
    def __init__(self):
        self.root = defaultdict()

    def insert(self,word):
        current = self.root
        for letter in word:
            current = current.setdefault(letter,{})
        current.setdefault("_end")

    def search(self,word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if "_end" in current:
            return True
        return False
test = Trie()
test.insert('helloworld')
test.insert('ilikeapple')
test.insert('helloz')

print test.search('helloworld')
print test.search('hello')
print test.search('ilikeapple')
        
