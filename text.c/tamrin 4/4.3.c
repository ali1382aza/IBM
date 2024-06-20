#include <stdio.h>

int main(){
    int n,i=1,x=0,number=1;
    scanf("%d",&n);

    while(1){
        while(i<=number){
            if(number%i==0){
                x++;
            }
            i++;
        if(x==n){
            break;
        }    
        }
        number++;
    }
    printf("%d",number);
}