#include <stdio.h>
#include <string.h>

int main() {
    char numbers1[10001];
    char numbers2[10001];
    int jam[10001];
    int sum=0,kam,n=0,g=0,ziad,f;
    int digit1,digit2;

    scanf("%s",numbers1);
    scanf("%s",numbers2);

    int k=strlen(numbers1);
    int h=strlen(numbers2);

    kam = (k<=h) ? k : h ;
    ziad= (k<=h) ? h : k ;
    f=(kam-1);

    for(int i=(ziad-1);i>(ziad-kam-1);i--){
        sum=0;
        sum+=n;
        n=0;
        if(ziad==k){
            digit1=numbers1[i]-'0';
            digit2=numbers2[f]-'0';
            f--;
        }
        else{
            digit2=numbers2[i]-'0';
            digit1=numbers1[f]-'0';
            f--;
        }

        sum+=(digit1+digit2);
        if (sum>9){
            n=(sum/10);
            sum=sum%10;
        }
        jam[g]=sum;
        g++;
        if(i==(ziad-kam+1) && n!=0){
            jam[g]=n;
        }
    }

    if( n!=0){
            printf("%d",n);
    }
    
    for(int i=(kam-1);i>=0;i--){
        printf("%d\n",jam[i]);
    }

}