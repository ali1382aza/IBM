#include <stdio.h>

int main(){
    int sum1=1,x,sum2=0;
    scanf("%d",&x);
    for(int i=1;i<=x;i++){
        for(int d=i;d>0;d--){
            sum1*=d;
        }
        sum2+=sum1;
        sum1=1;
    }
    printf("%d",sum2);
}