#include <stdio.h>

int jam(int x){
    int sum;
    sum=x+10;
    return sum;
}
int jam2(int x){
    int sum=0;
    while(x!=0){
        sum+=(x%10);
        x=x/10;
    }
    return sum;
}
int main(){
    printf("%d",jam2(123));
}