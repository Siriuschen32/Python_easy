#twosum threesum
def threesum(nums):
    X=sorted(nums)
    l=len(X)
    answer=[]
    k=0
    while k <=l-3:
        target=0-X[k]
        i=k+1
        j=l-1
        while i<j:
            if X[i]+X[j]==target:
                answer.append([X[k], X[i], X[j]])
                i=i+1
            elif X[i]+X[j]>target:
                j=j-1
            else:
                i=i+1
        k=k+1
    answer2=[]
    for s in answer:
        if s not in answer2:
            answer2.append(s)
    return answer2
a=[-1, 0, 1, 2, -1, -4, 3, -2, 3, 1, 0, 2, 0, -1]
b=[-4, -2, -1, -1, -1, 0, 0, 0, 1, 1, 2, 2, 3, 3]
print(threesum(a))

#坠好的方法
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)
