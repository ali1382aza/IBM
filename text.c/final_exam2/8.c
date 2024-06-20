#include <stdio.h>

int fac(int x){
    if(x>0){
        return x*fac(x-1); 
    }
    else{
        return 1;
    }
}
int main(){
    int a,b,r;
    scanf("%d",&a);
    scanf("%d",&b);
    r=fac(a)+fac(b);
    printf("%d",r);
}