#include <stdio.h>

main(){

  printf("%d\n", g(12));
  return 0;

}

int a(int x)
{

  if (x == 1){
    return 10;
  }
  return 10 + a(x - 1);

}

int b(int x)
{

  if (x == 1){
    return 2;
  }
  return -(b(x - 1));
}

int c(int x)
{  
  if (x == 1){
    return 1;
  }
  return c(x - 1) + (x * x);
}

int d(int x)
{
  if (x == 1){
    return 1;
  }
  return (x * x) * d(x - 1) + x -1;
}

int e(int x)
{
  if (x == 1){
    return 3;
  }
  if (x == 2){
    return 5;
  }
  return (x - 1) * e(x - 1) + (x - 2) * e(x - 2); 
}

int f(int x)
{
  if (x == 1){
    return 2;
  }
  if (x == 2){
    return 5;
  }
  return f(x - 1) * f(x - 2);
}

int g(int x)
{
  if (x == 1){
    return 1;
  }
  if (x == 2){
    return 2;
  }
  if (x == 3){
    return 3;
  }
  return g(x - 1) + 2 * g(x - 2) + 3 * g(x - 3);
}