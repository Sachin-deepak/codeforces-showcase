#include <stdio.h>
#include <math.h>
int main()
{
  long long int m,n,a;
  scanf("%lld %lld %lld",&m,&n,&a);
  long long int x;
  x=ceil((double)m/a)*ceil((double)n/a);
  printf("%lld",x);
}
