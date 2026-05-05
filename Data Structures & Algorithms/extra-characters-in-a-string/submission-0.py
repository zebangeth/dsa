class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        node.word = word


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_dict = Trie()
        for word in dictionary:
            word_dict.add_word(word)

        self.root = word_dict.root
        self.ans = len(s)

        self.dfs(s, 0, 0, self.root)
        return self.ans

    def dfs(self, s, start, extra, node):
        if extra >= self.ans:
            return

        if start == len(s):
            # 只有当当前不在匹配某个 word 的中间时，才是一个有效分割
            if node == self.root or node.is_word:
                self.ans = min(self.ans, extra)
            return

        # 如果当前 node 已经是一个完整 word 的结尾：
        # 可以选择结束这个 word，从 root 开始处理同一个 start
        if node.is_word:
            self.dfs(s, start, extra, self.root)

        # 只有在 root 状态下，才允许把当前字符当作 extra 跳过
        # 因为 root 表示“现在没有正在匹配某个 word”
        if node == self.root:
            self.dfs(s, start + 1, extra + 1, self.root)

        # 如果当前字符可以继续匹配 Trie，就连续匹配下去
        # 注意：这里不允许中途 skip
        c = s[start]
        if c in node.children:
            self.dfs(s, start + 1, extra, node.children[c])