class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


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


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()

        for word in dictionary:
            trie.add_word(word)

        n = len(s)
        memo = {}

        def dfs(i):
            # dfs(i): s[i:] 最少有多少 extra characters
            if i == n:
                return 0

            if i in memo:
                return memo[i]

            # Option 1:
            # 把当前字符 s[i] 当成 extra character
            ans = 1 + dfs(i + 1)

            # Option 2:
            # 从 i 开始，尝试匹配一个连续的 dictionary word
            node = trie.root

            for j in range(i, n):
                c = s[j]

                # 一旦当前连续前缀不在 Trie 里，后面也不用继续了
                if c not in node.children:
                    break

                node = node.children[c]

                # 如果 s[i:j+1] 是一个完整 dictionary word
                # 那么这一段不算 extra，直接从 j + 1 继续
                if node.is_word:
                    ans = min(ans, dfs(j + 1))

            memo[i] = ans
            return ans

        return dfs(0)