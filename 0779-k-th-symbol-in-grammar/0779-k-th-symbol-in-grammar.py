class Solution:
    def kthGrammar(self, n, k):
        if n == 1:
            # Per the requirements of the question, the data starts from the first row with a 0.
            return 0
        # As you recurse up into a parent row, the kth digit is based on the parent value at index (k+1) // 2.
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        if parent == 0:
            if k % 2 == 0:
                return 1
            else:
                return 0
        else:
            if k % 2 == 0:
                return 0
            else:
                return 1
