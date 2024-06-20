#include <stdio.h>

void F (int x);
void G (int x);
int X (int m);
int Y (int n);
int main (){
    int r, s;
    G (3);
    F (2);
    G(5);
    r = X (5);
    s = Y (10);
    printf("main: %d %d\n", r, s);
}
void F (int x){
    printf ("%d ", x);
}
void G (int x) {
    F (x + 1);
    printf("%d ", x);
}
int X (int m) {
    printf("X: %d\n", m);
    return (m + 2);
}
int Y (int n){
    printf("Y: %d %d\n", n, X (n));
    return (n * 3);
  }
