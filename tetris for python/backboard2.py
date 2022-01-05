

MAXWIDTH = 12
MAXHEIGHT = 21
BackGround = []

def backBoard():
    for row in range(21):
        for col in range(12):
            if row == 20:
                BackGround[row][col] = 1
            elif col == 0:
                BackGround[row][col] = 1
            elif cow == 11:
                BackGround[row][col] = 1
            else:
                BackGround[row][col] = 0






 
