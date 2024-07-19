class Solution:
    def findPeakGrid(self, mat) :
        def findRow(mid,n,m):
            maxi=mat[0][mid]
            row=0
            for i in range(1,n):
                if mat[i][mid]>maxi:
                    maxi=mat[i][mid]
                    row=i
            return row
        low=0
        n=len(mat)
        m=len(mat[0])
        high=m-1
        while low<=high:
            mid=(low+high)//2
            row=findRow(mid,n,m)
            left= mat[row][mid-1] if mid-1>=0 else -1
            right=mat[row][mid+1] if mid+1<m else -1
            if mat[row][mid]>left and mat[row][mid]>right:
                return [row,mid]
            elif mat[row][mid]<left:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]
obj=Solution()
mat=[[10,20,15],[21,30,14],[7,16,32]]
print(obj.findPeakGrid(mat))
