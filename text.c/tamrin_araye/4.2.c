#include <stdio.h>
#include <string.h>

int main() {
    char numbers1[10001];
    char numbers2[10001];
    int jam[10001];
    int sum=0,kam,n=0,g=0,ziad,r;
    int digit1,digit2;

    scanf("%s",numbers1);
    scanf("%s",numbers2);

    int k=strlen(numbers1);
    int h=strlen(numbers2);

    if(k>h){
        kam=h;
        ziad=k;
    }
    else{
        kam=k;
        ziad=h;
    }

    r=(kam-1);

    for(int i=(ziad-1);i>=(ziad-kam);i--){
        sum=0;
        sum+=n;
        n=0;
        if(ziad==k){
           digit1=numbers1[i]-'0';
           digit2=numbers2[r]-'0';
           r--; 
        }
        else{
            digit1=numbers2[i]-'0';
            digit2=numbers1[r]-'0';
            r--;
        }
        sum+=digit1+digit2;
        if (sum>9){
            n=(sum/10);
            sum=sum%10;
        }
        jam[g]=sum;
        g++;

    }