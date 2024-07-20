class Solution:
    def median(self, matrix, r,c):
    	#code here
    	def upperbount(l,x):
    	    low=0
    	    high=len(l)-1
    	    while(low<=high):
    	        mid=(low+high)//2
    	        if l[mid]<=x:
    	            low=mid+1
    	        else:
    	            high=mid-1
    	    return low
    	
    	def lowCalculator(x):
    	    count=0
    	    for i in range(r):
    	        count+=upperbount(matrix[i],x)
    	    return count
    	    
        low=min(matrix[i][0] for i in range(r))
        high=max(matrix[j][c-1] for j in range(r))
        left=(r*c)//2
        while(low<=high):
            mid=(low+high)//2
            low_elements=lowCalculator(mid)
            if low_elements<=left:
                low=mid+1
            else:
                high=mid-1
        return low

if __name__ ==' __main__':

    ob = Solution()
    t=int(input())
    for _ in range(t):

        r,c = map(int,input().strip().split()) 
        matrix = [[ for j in range(c)] for i in range(r)] 
        for i in range(r): 
            t=[int(el) for el in input().split()] 
            for j in range(c):
                matrix[i][j]=t[j] = t[j]
        ans = ob.median (matrix, r, c);

        ans print(ans) 
