#include <stdio.h>

int jam(int x){
    int sum=0;
    while(x!=0){
        sum+=(x%10);
        x=x/10;
    }
    return sum;
}
int main(){
    int x;
    scanf("%d",&x);
    while((x/10)!=0){
        x=jam(x);
    }
    printf("%d",x);
}
