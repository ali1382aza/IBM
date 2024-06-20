#include <stdio.h>

int main(){
    int x,d=0;
    scanf("%d",&x);
    while(x>0){
        d*=10;
        d+=(x%10);
        x/=10;
    }
    printf("%d",d);
}