'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
'''


class Solution(object):

    def comb_sum(self, input, target):
        if not input:
            return None
        ret = list()
        input.sort()
        self.helper(input, target, ret, [])
        return ret

    def helper(self, input, target, ret, tmp):

        s = sum(tmp) if tmp else 0

        if s > target:
            return
        elif s == target:
            ret.append(tmp)
            return
        else:
            for i, v in enumerate(input):
                self.helper(input[i:], target, ret, tmp + [v])


if __name__ == '__main__':
    print(Solution().comb_sum([2, 3, 6, 7], 7))
