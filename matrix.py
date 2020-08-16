# 1.    You are given a 2D array of size mxn. Rotate the array by 90 degrees clockwise. Assume n >= 1, m>=1.

 

# Example 1:
# |  1  2  |
# |  3  4  |

 

# |  3  1  |
# |  4  2  | 

 

# Example: 
# |   1   2   3   4   5    |
# |   6   7   8   9   10  |     
# |   11 12 13 14 15 | 

 

# |   11   6    1   |
# |   12   7    2   |
# |   13   8    3   |
# |   14   9    4   |
# |   15   10  5   | 

def matrix(mat):
    rows = len(mat)
    cols  = len(mat[0])
    out_mat = mat
    for i in range(rows):
        for j in range(cols):
            print(i,j)
            out_mat[i][j] = mat[j][i]

    return out_mat

print(matrix([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))
    



        