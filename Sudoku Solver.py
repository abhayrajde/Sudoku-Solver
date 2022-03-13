#!/usr/bin/env python
# coding: utf-8

# # Sudoku Solver

# In[14]:


def solve(board):
    find = find_emp(board)
    
    if(not find):
        return (True)
    
    else:
        for i in range(1,10):
            if(validate(board,i,find)):
                board[find[0]][find[1]] = i
                
                if(solve(board)):
                    return(True)
                
                board[find[0]][find[1]] = 0
    return(False)
            
    


# In[15]:


def validate(board, num, pos):
    # WHILE VALIDATING WE NEED TO VALIDATE 3 PARAMETERS FOR SUDOKU
    # 1. CHECK ROW
    # 2. CHECK COLUMN
    # 3. CHECK THE 3X3 BOX 
    # IN ALL THE THREE PARAMETERS EVERY ELEMENT SHOULD BE UNIQUE
    
    
    # 1. CHECK ROW 
    for i in range(len(board[0])):
        if((board[pos[0]][i] == num) and (pos[1] != i)):
            return (False)
    
    # 2. CHECK COLUMN
    for i in range(len(board)):
        if((board[i][pos[1]] == num) and (pos[0] != i)):
            return (False)
    
    # 3. CHECK THE 3X3 BOX
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y*3, box_y * 3 +3):
        for j in range(box_x*3, box_x * 3 +3):
            if(board[i][j] == num and (i,j) != pos):
                return(False)
    
    
    return(True)
        
    


# In[16]:


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for i in range(len(board)):
        if((i%3 == 0) and (i != 0)):
            print("- - - - - - - - - - - - - ")
        
        for j in range(len(board[0])):
            if((j%3 == 0) and (j != 0)):
                print(" | ", end = "")
            
            if(j == 8):
                print(board[i][j])
                
            else:
                print(board[i][j], end = " ")
# print_board(board)
        


# In[17]:


def find_emp(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 0):
                return(i,j)     # Returns ROW=i & COLUMN = j
    
    return(None)
# print(find_emp(board))


# In[18]:


# DRIVERS CODE
print_board(board)
solve(board)
print("_________________________________________")
print_board(board)


# In[ ]:




