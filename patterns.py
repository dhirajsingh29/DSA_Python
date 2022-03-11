# Steps to solve pattern questions
#   number of lines = number of rows = number of times outer loop will run
#   identify for every row number:
#       * how many columns are there
#       * type of elements in the column
#   what is needed to print
#   Note: try to find formula relating rows and columns

class Pattern:

    # ****
    # ****
    # ****
    # ****
    def pattern_1(self, n: int) -> None:
        for row in range(1, n + 1):
            for col in range(1, n + 1):
                print("*", end=" ")
            print("\n")


    # *
    # * *
    # * * *
    # * * * *
    def pattern_2(self, n: int) -> None:
        for row in range(1, n + 1):
            for col in range(1, row + 1):
                print("*", end=" ")
            print("\n")


    # * * * * *
    # * * * *
    # * * *
    # * *
    # *
    def pattern_3(self, n: int) -> None:
        for row in range(1, n + 1):
            for col in range(n - row + 1, 0, -1):
                print("*", end=" ")
            print("\n")


    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 4
    # 1 2 3 4 5
    def pattern_4(self, n: int) -> None:
        for row in range(1, n + 1):
            for col in range(1, row + 1):
                print(col, end=" ")
            print("\n")


    # *
    # * *
    # * * *
    # * * * *
    # * * * * *
    # * * * *
    # * * *
    # * *
    # *
    def pattern_5(self, n: int) -> None:
        # 1 to 9, if n = 5
        for row in range(1, 2 * n):

            totalColumnsInRow = row if row <= n else (2 * n) - row

            for col in range(1, totalColumnsInRow + 1):
                print("*", end=" ")
            print("\n")


    #         *
    #       * *
    #     * * *
    #   * * * *
    # * * * * *
    def pattern_6(self, n: int) -> None:
        for row in range(1, n + 1):

            spacePrefix = n - row
            for space in range(1, spacePrefix + 1):
                print(" ", end=" ")

            for col in range(1, row + 1):
                print("*", end=" ")
            print("\n")


    # * * * * *
    #   * * * *
    #     * * *
    #       * *
    #         *
    def pattern_7(self, n: int) -> None:
        for row in range(1, n + 1):

            totalColumnsInRow = n - row + 1
            spacePrefix = n - totalColumnsInRow

            for space in range(1, spacePrefix + 1):
                print(" ", end=" ")

            for col in range(1, totalColumnsInRow + 1):
                print("*", end=" ")

            print("\n")

    
    #         *
    #       * * *
    #     * * * * *
    #   * * * * * * *
    # * * * * * * * * *
    def pattern_8(self, n: int) -> None:
        for row in range(1, n + 1):

            totalColumnsInRow = (2 * row) - 1
            spacePrefix = n - row

            for space in range(1, spacePrefix + 1):
                print(" ", end=" ")

            for col in range(1, totalColumnsInRow + 1):
                print("*", end=" ")
            
            print("\n")


    # * * * * * * * * *
    #   * * * * * * *
    #     * * * * *
    #       * * *
    #         *    
    def pattern_9(self, n: int) -> None:
        for row in range(n, 0, -1):

            totalColumnsInRow = (2 * row) - 1
            spacePrefix = n - row

            for space in range(1, spacePrefix + 1):
                print(" ", end=" ")

            for col in range(1, totalColumnsInRow + 1):
                print("*", end=" ")

            print("\n")


    #     *
    #    * *
    #   * * *
    #  * * * *
    # * * * * *
    def pattern_10(self, n: int) -> None:
        for row in range(1, n + 1):

            spacePrefix = n - row
            for space in range(1, spacePrefix + 1):
                print(" ", end="")
            
            for col in range(1, row + 1):
                print("*", end=" ")

            print("\n")


    # * * * * *
    #  * * * *
    #   * * *
    #    * *
    #     *
    def pattern_11(self, n: int) -> None:
        for row in range(1, n + 1):

            totalColumnsInRow = n - row + 1
            spacePrefix = n - totalColumnsInRow

            for space in range(1, spacePrefix + 1):
                print(" ", end="")

            for col in range(1, totalColumnsInRow + 1):
                print("*", end=" ")

            print("\n")
    

    # * * * * *
    #  * * * *
    #   * * *
    #    * *
    #     *
    #     *
    #    * *
    #   * * *
    #  * * * *
    # * * * * *
    def pattern_12(self, n: int) -> None:
        for row in range(1, (2 * n) + 1):

            totalColumnsInRow = n - row + 1 if row <= n else row - n
            spacePrefix = n - totalColumnsInRow

            for space in range(1, spacePrefix + 1):
                print(" ", end="")

            for col in range(1, totalColumnsInRow + 1):
                print("*", end=" ")

            print("\n")


    #         *
    #       *   *
    #     *       *
    #   *           *
    # * * * * * * * * *
    def pattern_13(self, n: int) -> None:
        for row in range(1, n + 1):

            spacePrefix = n - row
            for space in range(1, spacePrefix + 1):
                print(" ", end=" ")

            totalColumnsInRow = 1 if row == 1 else 2 if row > 1 and row < n else (2 * row) - 1
            spaceInMiddle = ((2 * row) - 1) - totalColumnsInRow

            for col in range(1, totalColumnsInRow + 1):
                print("*", end=" ")
                for middleSpace in range(1, spaceInMiddle + 1):
                    print(" ", end=" ")
                spaceInMiddle = 0

            print("\n")


    # * * * * * * * * *
    #   *           *
    #     *       *
    #       *   *
    #         *
    def pattern_14(self, n: int) -> None:
        for row in range(n, 0, -1):

            spacePrefix = n - row
            for space in range(1, spacePrefix + 1):
                print(" ", end=" ")

            totalColumnsInRow = (2 * row) - 1 if row == 1 or row == n else 2
            spaceInMiddle = ((2 * row) - 1) - totalColumnsInRow

            for col in range(1, totalColumnsInRow + 1):
                print("*", end=" ")
                for middleSpace in range(1, spaceInMiddle + 1):
                    print(" ", end=" ")
                spaceInMiddle = 0

            print("\n")


    #     *
    #    * *
    #   *   *
    #  *     *
    # *       *
    #  *     *
    #   *   *
    #    * *
    #     *
    def pattern_15(self, n: int) -> None:
        for row in range(1, 2 * n):
            
            spacePrefix = n - row if row <= n else row - n
            for space in range(1, spacePrefix + 1):
                print(" ", end="")

            totalColumnsInRow = (2 * row) - 1 if row <= n else ((2 * n) - 1) - (2 * spacePrefix)
            for col in range(1, totalColumnsInRow + 1):
                if col == 1 or col == totalColumnsInRow:
                    print("*", end="")
                else:
                    print(" ", end="")

            print()


    #     1
    #    1 1
    #   1 2 1
    #  1 3 3 1
    # 1 4 6 4 1
    # this pattern is called Pascal's triangle
    def pattern_16(self, n: int) -> None:
        for row in range(1, n + 1):

            spacePrefix = n - row
            for space in range(1, spacePrefix + 1):
                print(" ", end="")

            pass


    #    1
    #   212
    #  32123
    # 4321234
    #  32123
    #   212
    #    1
    def pattern_17(self, n: int) -> None:
        for row in range(1, 2 * n):

            totalColumnsInRow = row if row <= n else (2 * n) - row
            spacePrefix = n - totalColumnsInRow

            for space in range(1, spacePrefix + 1):
                print(" ", end="")

            for col in range(totalColumnsInRow, 0, -1):
                print(col, end="")

            for col in range(2, totalColumnsInRow + 1):
                print(col, end="")

            print("\n")


    #     *
    #    * *
    #   * * *
    #  * * * *
    # * * * * *
    #  * * * *
    #   * * *
    #    * *
    #     *
    def pattern_28(self, n: int) -> None:
        for row in range(1, 2 * n):

            totalColumnsInRow = row if row <= n else (2 * n) - row
            spacePrefix = n - totalColumnsInRow

            for space in range(1, spacePrefix + 1):
                print(" ", end="")
            
            for col in range(1, totalColumnsInRow + 1):
                print("*", end=" ")

            print("\n")


    #         1
    #       2 1 2
    #     3 2 1 2 3
    #   4 3 2 1 2 3 4
    # 5 4 3 2 1 2 3 4 5
    def pattern_30(self, n: int) -> None:
        for row in range(1, n + 1):

            spacePrefix = n - row
            for space in range(1, spacePrefix + 1):
                print(" ", end=" ")

            # row to 1
            for col in range(row, 0, -1):
                print(col, end=" ")

            # 2 to row
            for col in range(2, row + 1):
                print(col, end=" ")

            print("\n")


if __name__ == "__main__":
    pattern = Pattern()
    pattern.pattern_15(5)
