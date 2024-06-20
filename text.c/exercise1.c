#include <stdio.h>

int main(){
    int a;
    scanf("%d",&a);
    if (a==1) {
        printf("one");
    }
    else{
        if(a==2){
            printf("two");
        }
        else{
            if(a==3){
                printf("three");
            }
            else{
                if(a==4){
                    printf("four");
                }
                else{
                    printf("this number is wrong");
                }
            }
        }
    }


}