#include <stdio.h>
/*int d=0,j=1;
int sum(int x){
    d++;
    if(x!=d){
        return j+
    }
}
*/
int main(){
    int x,sum=0,d=-1;
    scanf("%d",&x);
    for(int i=1;i<=x;i++){
        d+=2;
        printf("%d",d);
        sum+=d;
        if(i<x){
            printf("+");
        }
        else{
            printf("=");
        }
    }
    printf("%d",sum);
}