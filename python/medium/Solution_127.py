# 127. Word Ladder


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        if beginWord == endWord:
            return 1
        bfs = []
        bfs.append((beginWord, 1))
        while bfs:
            world, length = bfs.pop(0)
            for i in range(len(world)):
                for character in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = world[:i] + character + world[i+1:]
                    if new_word in wordset and new_word != world:
                        wordset.remove(new_word)
                        bfs.append((new_word, length+1))
                        if new_word == endWord:
                            return length+1
        return 0


beginWord = 'hit'
endWord = 'cog'
wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

ans = Solution().ladderLength(beginWord, endWord, wordList)
print(ans)
