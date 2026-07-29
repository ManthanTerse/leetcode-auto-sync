class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total_fbottles = numBottles
        while numBottles >= numExchange:
            new_bottles = numBottles / numExchange
            numBottles = new_bottles + (numBottles % numExchange)
            total_fbottles += new_bottles 
        return total_fbottles
        