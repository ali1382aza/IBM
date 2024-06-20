#include <stdio.h>

int sum(int x){
    int r;
    if(x>0){
        r=(x%10)+sum(x/10);
        return r;
    }
    else{
        return 0;
    }
}
int main(){
    int x;
    scanf("%d",&x);
    int result=sum(x);
    if(x%result==0){
        printf("true");
    }
    else{
        printf("false");
    }

    
}