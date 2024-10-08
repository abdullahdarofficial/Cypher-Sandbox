class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        # if len(word1) != len(word2):
        #     return False
        # map1 = {}
        # for char in word1:
        #     if char in map1:
        #         map1[char] += 1
        #     else:
        #         map1[char] = 1
        # map2 = {}
        # for char in word2:
        #     if char in map2:
        #         map2[char] += 1
        #     else:
        #         map2[char] = 1
            
        # if len(map1) != len(map2):
        #     return False

        # set1 = set()
        # set2 = set()     
        # for char, count in map1.items():
        #     set1.add(count)    
        # for char, count in map2.items():
        #     set2.add(count)     

        # return set1 == set2  


        # If lengths differ, they cannot be "close"
        if len(word1) != len(word2):
            return False
        
        # Count frequencies of characters in both words
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        # The two words must contain the same unique characters
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        # The frequency of each character, when sorted, must be the same
        return sorted(freq1.values()) == sorted(freq2.values())

