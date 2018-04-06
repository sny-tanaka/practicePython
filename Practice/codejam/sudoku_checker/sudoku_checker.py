# coding: utf-8
import os

def main():
    fp = os.path.dirname(os.path.abspath(__file__))+'\\'
    # f = open(fp+'A-small-practice.in', 'r')
    f = open(fp+'A-large-practice.in', 'r')
    T = int(f.readline()[:-1])
    for i in range(T):
        N = int(f.readline()[:-1])
        num_list = []
        for j in range(N**2):
            num_list.append(map(int, f.readline()[:-1].split()))
        # 重複フラグの設定
        duplication_flag = True
        # 横の調査
        if duplication_flag:
            for j in range(N**2):
                one_line = []
                one_line = num_list[j]
                one_line_uniq = list(set(one_line))
                if len(one_line_uniq) != N**2 or max(one_line_uniq) != N**2 or min(one_line_uniq) != 1:
                    duplication_flag = False
                    break
        # 縦の調査
        if duplication_flag:
            for j in range(N**2):
                one_line = []
                for k in range(N**2):
                    one_line.append(num_list[k][j])
                one_line_uniq = list(set(one_line))
                if len(one_line_uniq) != N**2 or max(one_line_uniq) != N**2 or min(one_line_uniq) != 1:
                    duplication_flag = False
                    break
        # ボックスの調査
        if duplication_flag:
            for m in range(0, N*(N-1), N):
                one_box = []
                for j in range(m, N+m):
                    for k in range(m, N+m):
                        one_box.append(num_list[j][k])
                one_box_uniq = list(set(one_box))
                if len(one_box_uniq) != N**2 or max(one_box_uniq) != N**2 or min(one_box_uniq) != 1:
                    duplication_flag = False
                    break
        if duplication_flag:
            print("Case #" + str(i + 1) + ": Yes")
        else:
            print("Case #" + str(i + 1) + ": No")


if __name__ == '__main__':
    main()
