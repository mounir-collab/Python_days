import sys



def solve_n_queens(n):

    board = [-1] * n
    solutions = []

    def is_safe(col , row) -> bool :

        for r in range (row):
            c = board[r]

            #testing is are on the same col

            if ( c == col ) :
                return False
            
            #testing diagonal 

            if (abs(c - col) == abs(r - row)):
                return False
        
        return True
    
    def back_track(row):

        if ( row == n):
            solutions.append(board.copy())
            return
        
        for col in range(n):
            if is_safe(col , row) == True :
                board[row] = col
                back_track(row + 1)
                board[row] = -1


    def convert_solutions(solutions, n):
        result = []

        for sol in solutions:
            board = []
            for c in sol:
                row = "."*c + "Q" + "."*(n-c-1)
                board.append(row)
            result.append(board)

        return result

    back_track(0)

    return(convert_solutions(solutions , n))

    
       

    


def print_solutions(solutions, n):
    for sol in solutions:
        for r in range(n):
            row = ["." for _ in range(n)]
            row[sol[r]] = "Q"
            print(" ".join(row))
        print()

def main():
    if ( len(sys.argv) == 1):
        print("the next time enter an integer between 1 and 9 ...")
        exit(0)
    if ( len(sys.argv) == 2 ):
        n = sys.argv[1]
        try :
            n = int(n)
            solutions = (solve_n_queens(n))
            print(solutions)
            # print("Number of solutions:", len(solutions))
            # print_solutions(solutions , n)
        except ValueError as e :
            print("Error : " ,)
        exit(0)
    print("Just One Arg... ")
    exit(0)
    pass


if __name__ == "__main__":
    main()




# ████████████████████████████████████████████████████████████████
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ██                                                            ██ 
# ████████████████████████████████████████████████████████████████