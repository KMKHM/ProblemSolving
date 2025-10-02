class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0

        for string in text.split():
            flag = True
            for c in string:
                if c in brokenLetters:
                    flag = False
                    break
            if flag:
                res += 1
        return res