'''
MS SE role in Bing Team
CTCT 1.8. Zero Matrix: 

Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.  

'''
'''
solution1 :
0 이 있는 열과 행을 찾아서 기록해놓는다
0을 표시한다

solution 2: 0이 있는 행,열을 기록할 배열을 행렬의 일부에서 재활용한다.
[확보 > 찾기 > 전체 적용]
1) 재활용하기 전에 첫 행, 첫 열에도 0 있엇는지 확인
2) 0이 실제로 있는 곳 확인, 첫 행 첫 열에 표기, 0  적용
3) 마지막 첫행 첫열에도 0 반영!
'''




import unittest
def zero_matrix(mat):
    firstRowHasZero = False
    firstColHasZero = False

    #check first row
    if 0 in mat[0]:
        firstRowHasZero = True

    #check first col
    for i in range(len(mat)):
        if mat[i][0] == 0:
            firstColHasZero = True
            break

    #check rest of mat, and check in the first row or col
    for row in range(1, len(mat)):
        for col in range(1, len(mat)):
            if mat[row][col] == 0:
                mat[0][col] = 0
                mat[row][0] = 0
    
    
    # nullify
    for col in range(len(mat)):
        if mat[0][col] == 0:
            nullify_col(mat, col)

    for row in range(len(mat)):
        if mat[row][0] == 0:
            nullify_row(mat, row)
    
    if firstRowHasZero:
        print('0 row')
        nullify_row(mat, 0)
    if firstColHasZero:
        print('0 col')
        nullify_col(mat, 0)
    print('3, {}'. format(mat))
    
    return mat

def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
