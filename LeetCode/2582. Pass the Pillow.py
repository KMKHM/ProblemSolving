"""
Pass the Pillow
"""


class Solution:
    def passThePillow(self, n, time):

        init, flag = 1, True

        while time != 0:
            time -= 1
            if flag:
                init += 1
            else:
                init -= 1
            if init == n:
                flag = False
            if init == 1:
                flag = True
        return init

    def passThePillow2(self, n, time):
        chunks = time // (n - 1)
        return (time % (n - 1) + 1) if chunks % 2 == 0 else (n - time % (n - 1))

