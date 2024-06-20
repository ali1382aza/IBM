#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(){
    int i=0,j=0,p=0;
    char input[100],ch,asli[100],tavan[100];
    while((ch=getchar()) != '\n'){
        input[i]=ch;
        i++;
    }
    input[i]='0';
    int k=strlen(input) ;
    for(int g=0;g<i;g++){
        if (input[g]=='e'){
            for(int h=0;h<g;h++){
                asli[h]=input[j];
                j++;
            }
            printf("%d\n",k);
            g++;
            for(int o=g ; o<k ;o++){
                tavan[p]=input[o];
                p++;
            }
        }
    }
    float asli1=atof(asli) , tavan1=atof(tavan);
    printf("%f\n",asli1);
    printf("%f",tavan1);
    int adad = (int)asli1*(pow(10,(int)tavan1));
    printf("%d",adad);
}