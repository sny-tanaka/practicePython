#include <stdio.h>

#define TRUE    (1)
#define FALSE   (0)
#define STRIKE  (1)
#define SPARE   (2)
#define COMMON  (0)

/**
 * @fn
 * @brief   入力された数値が正常値であるかどうかの判定
 * @param   tf  : 数値かどうかの判定
 *          inp : 入力された値
 *          rem : 残りピン数
 * @return  正常値=TRUE, 異常値=FALSE
 */
char input_check(char tf, int inp, int rem){
    if (tf == FALSE){
        printf("数値を入力してください！\n");
        return FALSE;
    }
    else if (inp > rem){
        printf("そんなにピンは残っていません！\n");
        return FALSE;
    }
    else if (inp < 0){
        printf("負の数は倒せません！\n");
        return FALSE;
    }
    else{
        return TRUE;
    }
}

/**
 * @fn
 * @brief   倒したピン数の入力を受け付ける
 * @param   flame : フレーム数
 *          throw : フレーム内投球数
 *          rem   : 残りピン数
 * @return  入力された数値
 */
int input(int flame, int throw, int rem){
    int inp = 0;
    char buf[4];
    while (TRUE){
        printf("%dフレーム%d投, 残りピン数%d本, 倒したピンの数 = ", flame, throw, rem);
        fgets(buf, 4, stdin);
        char tf = sscanf(buf, "%d", &inp);
        if (input_check(tf, inp, rem) == TRUE){
            break;
        }
    }
    return inp;
}

/**
 * @fn
 * @brief   その投球がSTRIKE/SPARE/その他のどれかを判定
 * @param   throw : フレーム内投球数
 *          pin1  : 1つ前の倒ピン数
 *          pin2  : 最新の倒ピン数
 * @return  STRIKE/SPARE/COMMONのいずれかを返す
 */
char throw_judge(int throw, int pin1, int pin2){
    char flag;
    if (throw == 1 && pin2 == 10){
        printf("Strike!\n");
        flag = STRIKE;
    }
    else if (throw == 2 && pin1 + pin2 == 10){
        printf("Spare!\n");
        flag = SPARE;
    }
    else{
        printf("%d\n", pin2);
        flag = COMMON;
    }
    return flag;
}

int main(void){
    int pin1 = 0;               /* 1つ前の倒ピン数 */
    int pin2 = 0;               /* 最新の倒ピン数 */
    int flame_score = 0;        /* フレーム単位のスコア */
    int rem = 10;               /* 残りピン数 */
    int strike = FALSE;         /* 連続ストライク数 */
    int flame;                  /* フレーム数 */
    int throw;                  /* 投球数 */
    char flag;                  /* 投球ごとのジャッジ */
    char third_flag = FALSE;    /* 3投目を投げる権利のフラグ */

    /* 1-10フレームの共通処理 */
    for (flame = 1; flame <= 10; flame++){
        rem = 10;
        for (throw = 1; throw <= 2; throw++){
            pin1 = pin2;
            pin2 = input(flame, throw, rem);
            if (flag == SPARE){
                flame_score = flame_score + 10 + pin2;
                printf("%dフレームまでの得点 = %d\n", flame-1, flame_score);
            }
            else if (strike >= 2){
                flame_score = flame_score + 20 + pin2;
                printf("%dフレームまでの得点 = %d\n", flame-2, flame_score);
            }
            flag = throw_judge(throw, pin1, pin2);
            if (flame == 10 && flag == STRIKE){
                third_flag = TRUE;
                strike = 1;
                continue;
            }
            else if (flame == 10 && flag == SPARE){
                third_flag = TRUE;
                rem = 10;
                continue;
            }
            else if (flag == STRIKE){
                strike++;
                break;
            }
            else if (strike == 1 && throw == 2){
                flame_score = flame_score + 10 + pin1 + pin2;
                printf("%dフレームまでの得点 = %d\n", flame-1, flame_score);
                rem = rem - pin2;
                strike = FALSE;
            }
            else{
                rem = rem - pin2;
            }
            if (third_flag == FALSE && flag == COMMON && throw == 2){
                flame_score = flame_score + pin1 + pin2;
                printf("%dフレームまでの得点 = %d\n", flame, flame_score);
            }
        }
    }

    /* 10フレーム3投目の処理 */
    if (third_flag == TRUE){
        flame = 10;
        throw = 3;
        pin1 = pin2;
        pin2 = input(flame, throw, rem);
        if (flag == COMMON){
            flame_score = flame_score + 10 + pin1 + pin2;
        }
        else{
            flame_score = flame_score + 10 + pin2;
        }
        printf("%dフレームまでの得点 = %d\n", flame, flame_score);
    }
    printf("あなたのスコアは%d点です！\n", flame_score);
}
