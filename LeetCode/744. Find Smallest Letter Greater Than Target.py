from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = ""
        diff = 27
        t = ord(target)

        for letter in letters:
            if letter > target:
                if ord(letter) - t < diff:
                    diff = ord(letter) - t
                    res = letter

        return letters[0] if not res else res