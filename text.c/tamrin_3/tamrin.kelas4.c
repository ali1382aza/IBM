void myfunction(char name[], int age){
    printf("hello %s. you are %d years old\n",name,age);
}

int myfunction2(int x){
    return x + 5;
}

int main(){
    int c,z;
    scanf("%d",&c);
    z=myfunction2(c);
    printf("your result is %d",z);
}