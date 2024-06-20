#include <stdio.h>

int main(){

    float a ;
    scanf("%f",&a);
    if(a>0){
        printf("positive");
    
    }
    else if (a<0) {
        printf("negative");
    }
    else {
        printf("number is zero");
    }
}