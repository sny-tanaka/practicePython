#include <stdio.h>

/*
出力例
prob1_str_length = 7
prob2_str_length = 5
prob3_str_length = 0
prob4_str_length = 0
*/

int string_length(const char *str)
{
  /* ここに処理を実装してください。 */
  int len = 0;
  if (str == NULL)
  {
      return len;
  }
  while (*str++ != '\0')
  {
      ++len;
  }
  return len;
}

int main()
{
  const char *prob1_str = "abcdefg";
  char prob2_str[] = "efghi";
  char *prob3_str = NULL;
  const char *prob4_str = "";
  printf("prob1_str_length = %d\n", string_length(prob1_str));
  printf("prob2_str_length = %d\n", string_length(prob2_str));
  printf("prob3_str_length = %d\n", string_length(prob3_str));
  printf("prob4_str_length = %d\n", string_length(prob4_str));

  return 0;
}