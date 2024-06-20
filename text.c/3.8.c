#include <stdio.h>

int main(){
    int x ,ayas ,jaber ,izad ,bezi;
    scanf("%d",&x);
    ayas=x/100000;
    jaber=(x%100000)/50000;
    izad=(x-(100000*ayas+50000*jaber))/10000;
    bezi=(x-(100000*ayas+50000*jaber+10000*izad))/5000;
    if(ayas>=1){
        printf("%d Ayaz Coin",ayas);
        if(jaber>0 || izad>0 || bezi>0){
            printf(" & ");
        }
    }
    if(jaber>=1){
        printf("%d Jaber Coin",jaber);
        if(izad>0 || bezi>0){
            printf(" & ");
        }
    }
    if(izad>=1){
        printf("%d Izad Coin",izad);
        if(bezi>0){
            printf(" & ");
        }
    }
    if(bezi>=1){
        printf("%d Bezi Coin",bezi);
    }

}