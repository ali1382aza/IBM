#include <stdio.h>

int main(){
    int n,x=1,t=1;
    scanf("%d",&n);
    while(x<=n){
        t*=x;
        x++;
    }
    printf("%d",t);
}