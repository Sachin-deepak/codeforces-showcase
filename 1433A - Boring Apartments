#include<stdio.h>
long long count_digits(long long num)
{
    long long count=0;
    while(num>0)
    {
        num/=10;
        count++;
    }
    return count;
}
long long count_pattern(long long num)
{
    long long x=num%10;
    long long count=(x-1)*10;
    long long y=count_digits(num);
    if(y==1) count+=1;
    else if(y==2) count+=3;
    else if(y==3) count+=6;
    else if(y==4) count+=10;
    return count;
}
int main()
{
    long long n,num,count;
    scanf("%lld\n",&n);
    for(int i=1; i<=n; i++)
    {
        scanf("%lld",&num);
        count=count_pattern(num);
        printf("%lld\n",count);
    }
}
