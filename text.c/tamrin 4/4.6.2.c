#include <stdio.h>
#include <math.h>


int be10(int adad,int mabna){
    int sum=0,x=0;
    while(adad!=0){
        int r=adad%10;
        sum+=r*(pow(mabna,x));
        adad/=10;
        x++;
    }
    return sum;
}
int az10(int adad,int mabna){
    int x=0,sum=0;
    while(adad!=0){
        sum+=((adad%mabna)*pow(10,x));
        x++;
        adad/=mabna;
    }
    return sum;
}

int main(){
    int adad,mabna;
    scanf("%d %d",&adad,&mabna);
    int result=az10(adad,mabna);
    printf("%d",result);

}