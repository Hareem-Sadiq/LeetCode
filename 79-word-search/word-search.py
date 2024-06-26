class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def backtrack(row, col, index):
            if index == len(word):
                return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
                return False

            # Mark the current cell as visited
            temp = board[row][col]
            board[row][col] = '#'

            # Explore adjacent cells
            if (backtrack(row + 1, col, index + 1) or
                backtrack(row - 1, col, index + 1) or
                backtrack(row, col + 1, index + 1) or
                backtrack(row, col - 1, index + 1)):
                return True

            # Restore the cell
            board[row][col] = temp
            return False

        # Iterate through each cell to start the search
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False