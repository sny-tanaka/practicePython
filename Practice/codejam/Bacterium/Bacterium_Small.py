# coding: utf-8

def Include(A, B, C):
    for i in range(B):
        A = A ** A
        print("A"+str(A))
    N = A % C
    return N

def main():
    N = Include(2, 3, 3)
    print(N)

if __name__ == '__main__':
    main()