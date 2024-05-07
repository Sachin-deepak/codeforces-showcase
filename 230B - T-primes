#include <stdio.h>
#include <math.h>
int main ()
{
    long long int t;
    scanf("%lld",&t);
    for(long long int i=1;i<=t;i++)
    {
        long long int num,n;
        scanf("%lld",&num);
        n=sqrt(num);
        long long int x=0;
        if (n*n==num)
        {
            x=1;
        }
        if(x==1)
        {
            num = n;
            long long int flag=1;
            if (num<2)
                flag=0;
            else if (num>=4 && (num%2==0 || num%3==0))
                flag=0;
            long long int k=1;
            long long int a=6*k-1, b=6*k+1;
            long long int sqr = sqrt(num);
            while (a<=sqr && flag==1)
            {
                if (num%a==0 || num%b==0)
                {
                    flag=0;
                    break;
                }
              k++;
              a=6*k-1;
              b=6*k+1;
            }
            if (flag==1)
                printf("YES\n");
            else 
                printf("NO\n");
        }
        else
        {
            printf("NO\n");
        }
    }
}
