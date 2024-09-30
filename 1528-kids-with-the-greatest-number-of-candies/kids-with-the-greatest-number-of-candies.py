class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output=[]
        max_candies =max(candies)
        for candy in candies:
           output.append(candy + extraCandies >= max_candies) 
        return output
      
            

     
