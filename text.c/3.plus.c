#include <stdio.h>

int main(){
    int x ,ayas ,jaber ,izad ,bezi ,cs ;
    scanf("%d",&x);
    ayas=x/100;
    jaber=(x%100)/50;
    izad=(x-(100*ayas+50*jaber))/10;
    bezi=(x-(100*ayas+50*jaber+10*izad))/5;
    cs=(x-(100*ayas+50*jaber+10*izad+5*bezi))/1;
    if(ayas>=1){
        printf("%d Ayaz Coin",ayas);
        if(ayas>=2){
            printf("s");
        }
        if(jaber>0 || izad>0 || bezi>0 || cs>0){
            printf(" & ");
        }
    }
    if(jaber>=1){
        printf("%d Jaber Coin",jaber);
        if(jaber>=2){
        printf("s");
        }
        if(izad>0 || bezi>0 || cs>0){
            printf(" & ");
        }
    }
    if(izad>=1){
        printf("%d Izad Coin",izad);
        if(izad>=2){
            printf("s");
        }
        if(bezi>0 || cs>0){
            printf(" & ");
        }
    }
    if(bezi>=1){
        printf("%d Bezi Coin",bezi);
        if(bezi>=2){
            printf("s");
        }
        if(cs>=1){
            printf(" & ");
        }
    }
    if(cs>0){
        printf("%d CS Coin",cs);
        if(cs>=2){
            printf("s");
        }
    }
}