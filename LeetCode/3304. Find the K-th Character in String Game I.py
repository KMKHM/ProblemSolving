class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            tmp = ""
            for s in word:
                num = ord(s)
                num += 1
                num = 97 if num == 123 else num
                tmp += chr(num)
            word += tmp

        return word[k - 1]