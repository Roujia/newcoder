# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表

    def Find(self, target, array):
        # write code here
        # 因为有序，所以从右上角或者左下角开始比
        if len(array) == 0 or array[0] == 0:  # 数组为空，行，列
            return False
        i = 0  # 行
        j = len(array[0]) - 1  # 列
        while (i < len(array) and j >= 0):
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

if __name__=="__main__":
    s=Solution()
    a=[[1,2,3],
       [4,5,7],
       [9,12,13]]
    print(s.Find(9,a))