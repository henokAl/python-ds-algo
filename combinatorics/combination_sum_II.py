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
            i=0
            while i < len(input):
                self.helper(input[i+1:], target, ret, tmp+[input[i]])
                while i+1< len(input) and input[i]==input[i+1]:
                    i+=1
                i+=1


if __name__ == '__main__':
    print(Solution().comb_sum([10,1,2,7,6,1,5], 8))
