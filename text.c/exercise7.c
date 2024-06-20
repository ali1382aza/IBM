int main(){
    float weight,height,bmi;
    scanf("%f",&weight);
    scanf("%f",&height);
    bmi=weight/pow(height,2);
    printf("%.2f \n",bmi);
    if(bmi<18.5){
        printf("Underweight");
    }
    else if(bmi>=18.5){
        if (bmi<25){
            printf("Normal");
        }
    }
    else if(bmi>=25){
        if (bmi<30){
            printf("Overweight");
        }
    }
    if (bmi>=30){
        printf("Obese");
    }
    
}