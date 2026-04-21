class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_dict = {}
        out = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in words_dict:
                words_dict[sorted_word].append(word)
            else:
                words_dict[sorted_word] = [word]
        for key in words_dict.keys():
            out.append(words_dict[key])

        return out
