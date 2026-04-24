class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        id_to_word = collections.defaultdict(list)
        for word in strs:
            id_to_word[self.get_word_id(word)].append(word)
        return list(id_to_word.values())
    
    def get_word_id(self, word):
        id = [0] * 26
        for c in word:
            id[ord(c) - ord("a")] += 1
        return tuple(id)