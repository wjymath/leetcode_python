class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A_dict = {}
        B_dict = {}
        same_cnt = 0
        diff_cnt = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                same_cnt += 1
            else:
                A_dict[secret[i]] = A_dict.get(secret[i], 0) + 1
                B_dict[guess[i]] = B_dict.get(guess[i], 0) + 1

        for i in A_dict:
            if i in B_dict:
                diff_cnt += min(A_dict[i], B_dict[i])
        return str(same_cnt) + "A" + str(diff_cnt) + "B"

