#include <stdio.h>

int sum=0;

int jam(int n){
    if(n!=0){
        return n%10+jam(n/10);
    }
    else{
        return 0;
    }
}
int main(){
    int n;
    scanf("%d",&n);
    int result=jam(n);
    printf("%d",result);
}