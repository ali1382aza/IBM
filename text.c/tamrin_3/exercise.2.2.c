#include <stdio.h>

int main(){
    int x=2,n,i1=1,i2=1,sum=0;
    scanf("%d",&n);
    while(x<n){
        sum+=i1+i2;
        i1=i1+i2;
        i2=i2+i1;
        x++;
    }
    if(n%2!=2){
        printf("%d\n",i1);
    }
    else{
        printf("%d\n",i2);
    }
    printf("%d",sum);
}