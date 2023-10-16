class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prv_row=[1]
        
        for i in range (rowIndex):
            next_row=[0] * (len(prv_row)+1)
            
            for j in range (len(prv_row)):
                
                next_row[j] += prv_row[j]
                next_row[j+1] += prv_row[j]
            prv_row = next_row                           
                                       
        return prv_row