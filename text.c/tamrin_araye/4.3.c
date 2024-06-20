#include <stdio.h>
#include <string.h>

int main() {
    char numbers1[10001];
    char numbers2[10001];
    int sum=0,kam,n=0;
    

    scanf("%s",numbers1);
    scanf("%s",numbers2);

    int k=strlen(numbers1);
    int h=strlen(numbers2);

    kam = (k<h) ? k : h ;
    
    int digit1=numbers1[0]-'0';
    printf("%d\n",digit1);
    int digit2=numbers2[0]-'0';
    printf("%d\n",digit2);
    sum=(digit1+digit2);
    printf("%d",sum);

    

}