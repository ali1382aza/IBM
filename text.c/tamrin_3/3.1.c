#include <stdio.h>

int main(){
    float weight,height,bmi;
    scanf("%f",&weight);
    scanf("%f",&height);
    bmi=weight/(height*height);
    printf("%.2f \n",bmi);
    if(bmi<18.5){
        printf("Underweight");
    }
    else if(bmi>=18.5 && bmi<25){
        
            printf("Normal");
        }
    
    else if(bmi>=25 && bmi<30){
        
            printf("Overweight");
        }
    else {
        printf("Obese");
    }
    
}