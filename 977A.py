#include<stdio.h>
long long apply_logic(long long num,long long i)
{
    while(i>0)
    {
        if((num%10)!=0) num-=1;
        else if ((num%10)==0) num/=10;
        --i;
    }
    return num;
}
int main()
{
    long long num,i;
    scanf("%lld %lld",&num,&i);
    long long result=apply_logic(num,i);
    printf("%lld",result);
}
