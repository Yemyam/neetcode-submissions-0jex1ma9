class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # create a tree based on word routes that we can take, and then do bfs on that tree
        # and then we return the first route that we encounter
        # for each word, we can replace on letter with a wildcard *, this will be the key in a dicionary, and the value will be the list of words that follow the rule
        words = {}
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                wild_word = word[:i] + "*" + word[i + 1:]
                if wild_word in words:
                    words[wild_word].append(word)
                else:
                    words[wild_word] = [word]
        print(words.items())
        
        # now we do bfs starting from beginWord
        q = collections.deque()
        q.append(beginWord)
        out = 1
        visited = set()
        visited.add(beginWord)
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return out
                for i in range(len(curr)):
                    wild_word = curr[:i] + "*" + curr[i + 1:]
                    for adj_word in words[wild_word]:
                        if adj_word != curr and adj_word not in visited:
                            q.append(adj_word)
                            visited.add(adj_word)
            out += 1
        return 0
        
                
