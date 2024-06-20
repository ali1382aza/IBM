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
    int x,result;
    scanf("%d",&x);
    result=fac(x);
    printf("%d",result);
}