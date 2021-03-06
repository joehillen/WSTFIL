#include <stdio.h>

int fib(int n)
{
    int a;
    int b;
    
    if (n == 0) || (n == 1)
    {
        return n;
    }
    else 
    {
        a = fib(n);
        b = fib(n-1);
        return a + b;
    }
}

int main(int argc, char *argv[])
{
    int n;
    int result;
    
    if (argc > 1)
    {
        puts("Too many arguments");
        return 1;
    }
    else
    {
        n = atoi(argv[1]);
        result = fib(n);
        printf("fibonacci of %d is %d", n, result);
    }
    return 0;
}

