def pattern():
    for i in range(len(name)):
        #Code for A:
        if name[i]=="A" or name[i]=="a":
            print_A = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0 or col==4) and (row!=0) or (row==0 or row==3) and (col<4 and col>0):
                        print_A[row][col]="*"
            list2.append(print_A)
        #Code for B:
        elif name[i]=="B" or name[i]=="b":
            print_B = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0) or (row==0 or row==3 or row==6) and(col!=4) or (col==4) and (row!=0 and row!=3 and row!=6):
                        print_B[row][col]="*"
            list2.append(print_B)
        #Code for C:
        elif name[i]=="C" or name[i]=="c":
            print_C = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0) and (row!=0 and row!=6) or (row==0 or row==6) and (col!=0):
                        print_C[row][col]="*"
            list2.append(print_C)
        #Code for D:
        elif name[i]=="D" or name[i]=="d":
            print_D = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0) or (col==4 and (row!=0 and row!=6)) or ((row==0 or row==6 ) and (col>0 and col<4)):
                        print_D[row][col]="*"
            list2.append(print_D)
        #Code for E:
        elif name[i]=="E" or name[i]=="e":
            print_E = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or row==0 or row==3 or row==6:
                        print_E[row][col]="*"
            list2.append(print_E)
        #Code for F:
        elif name[i]=="F" or name[i]=="f":
            print_F = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or row==0 or row==3:
                        print_F[row][col]="*"
            list2.append(print_F)
        #Code for G:
        elif name[i]=="G" or name[i]=="g":
            print_G = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0) and (row!=0 and row!=6) or (row==0 or row==6) and(col!=0) or col==4 and (row>2 and row<6) or row==3 and (col<4 and col>1):
                        print_G[row][col]="*"
            list2.append(print_G)
        #Code for H:
        elif name[i]=="H" or name[i]=="h":
            print_H = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or col==4 or row==3:
                        print_H[row][col]="*"
            list2.append(print_H)
        #Code for I:
        elif name[i]=="I" or name[i]=="i":
            print_I = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==0 or row==6 or col==2:
                        print_I[row][col]="*"
            list2.append(print_I)
        #Code for J:
        elif name[i]=="J" or name[i]=="j":
            print_J = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==0 or row==6 and col<3 or col==2 and (row>0 and row<6):
                        print_J[row][col]="*"
            list2.append(print_J)
        #Code for K:
        elif name[i]=="K" or name[i]=="k":
            print_K = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or (row<4 or col>0) and (row+col==4) or (row>3 or col>1) and (row-col==2):
                        print_K[row][col]="*"
            list2.append(print_K)
        #Code for L:
        elif name[i]=="L" or name[i]=="l":
            print_L = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or row==6 and col>0:
                        print_L[row][col]="*"
            list2.append(print_L)
        #Code for M:
        elif name[i]=="M" or name[i]=="m":
            print_M = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or col==4 or (col>0 and row>0 and row<3 and col<3) and (row-col==0) or row==1 and col==3:  
                        print_M[row][col]="*"
            list2.append(print_M)
        #Code for N:
        elif name[i]=="N" or name[i]=="n":
            print_N = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or col==4 or (col>0 and row>0 and col<4 and row<6) and (row-col==1):
                        print_N[row][col]="*"
            list2.append(print_N)
        #Code for O:
        elif name[i]=="O" or name[i]=="o":
            print_O = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (row==0 or row==6) and (col!=0 and col!=4) or (col==0 or col==4) and (row!=0 and row!=6):
                        print_O[row][col]="*"
            list2.append(print_O)
        #Code for P:
        elif name[i]=="P" or name[i]=="p":
            print_P = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 and row!=0 or row==0 and (col!=0 and col!=4) or col==4 and(row!=0 and  row<3) or row==3 and (col!=0 and col!=4):
                        print_P[row][col]="*"
            list2.append(print_P)
        #Code for Q:
        elif name[i]=="Q" or name[i]=="q":
            print_Q = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0 or col==4) and (row!=0 and row<5) or (row==0 or row==5) and (col!=0 and col!=4) or (row==4 and col==2) or (row==6 and col==4):
                        print_Q[row][col]="*"
            list2.append(print_Q)
        #Code for R:
        elif name[i]=="R" or name[i]=="r":
            print_R = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 and (row!=0) or row==0 and (col!=0 and col!=4) or col==4 and (row!=0 and row<3) or (row==3) and (col!=0 and col!=4) or (row>3 and col>0) and (row-col==2):
                        print_R[row][col]="*"
            list2.append(print_R)
        #Code for S:
        elif name[i]=="S" or name[i]=="s":
            print_S = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if ((row==0 or row==3 or row==6) and (col>0 and col<4)) or (col==0 and (row>0 and row<3) or (col==4 and (row>3 and row<6))):
                        print_S[row][col]="*"
            list2.append(print_S)
        #Code for T:
        elif name[i]=="T" or name[i]=="t":
            print_T = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==0 or col==2:
                        print_T[row][col]="*"
            list2.append(print_T)
        #Code for U:
        elif name[i]=="U" or name[i]=="u":
            print_U = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0 or col==4) and (row!=6) or row==6 and (col!=0 and col!=4):
                        print_U[row][col]="*"
            list2.append(print_U)
        #Code for V:
        elif name[i]=="V" or name[i]=="v":
            print_V = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0 or col==4) and (row<4) or row>3 and (row-col==4) or (row>4 or col>2) and (row+col==8):
                        print_V[row][col]="*"
            list2.append(print_V)
        #Code for W:
        elif name[i]=="W" or name[i]=="w":
            print_W = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or col==4 or (row>3 and row<6 and col>0 and col<3) and (row+col==6) or row==5 and col==3:
                        print_W[row][col]="*"
            list2.append(print_W)
        #Code for X:
        elif name[i]=="X" or name[i]=="x":
            print_X = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0 and row==0) or (col==0 and row==6) or (col==4 and row==0) or (col==4 and row==6) or (row>0 and row<6) and (row-col==1) or (row>0 and row<6) and (row+col==5):
                        print_X[row][col]="*"
            list2.append(print_X)
        #Code for Y:
        elif name[i]=="Y" or name[i]=="y":
            print_Y = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row<3 and (row-col==0) or (row<2 or col>2) and (row+col==4) or col==2 and row>2:
                        print_Y[row][col]="*"
            list2.append(print_Y)
        #Code for Z:
        elif name[i]=="Z" or name[i]=="z":
            print_Z = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==0 or row==6 or (row>0 and row<6) and (row+col==5) :
                        print_Z[row][col]="*"
            list2.append(print_Z)
        elif name[i]==" ":
            print_ = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==6:
                        print_[row][col]=" "
            list2.append(print_)
        else:
            print("INVALID")
    return list2

name = input("Enter the name: ")
list2=[]
list3= pattern()

for i in range(7):
    for j in range(len(list3)):
        for k in range(5):
            print(list3[j][i][k],end=" ")
        print(end="  ")
    print()