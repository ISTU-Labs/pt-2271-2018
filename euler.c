#include "stdio.h"
#include <stdlib.h>


struct result_s {
  int    len;
  double * a;
};

typedef struct result_s result_t;

//struct result_s s1;
//result_t s2;

typedef double (* f_t)(double x, double F);

double cooling_f(double x, double F) {
  return 0.0;
}

result_t * euler(f_t f,
                 double x0,
                 double F0,
                 double eps,
                 double h,
                 int m) {
  result_t * r = malloc(sizeof(result_t));
  if (r==NULL) {
    printf("Cannot allocate mamory!\n");
    exit(1);
  }
  r->a = malloc(sizeof(double) * 10); // realloc()
  r->lrn = 10;
  return r;
}

// result_t s1;    // s1.len = 0;
// result_t * p1;  // *p1.len = 0; pi->len = 0;

void result_free(result_t * result) {
  free(result->a);
  free(result);
}

void show(result_t * result) {
  printf("Showing the result!\n");
  result[0];
}

int main(int argc, char ** argv) {
  result_t * result = NULL;
  printf("Progran %s solving Cauchy problem!\n", argv[0]);
  result=euler(cooling_f,
               0.0,  // x0
               100.0, // F0
               0.01,  // eps
               0.1,   // h
               10    // m
               );
  show(result);
  result_free(result);
}



/*

# C=Ctrl, M (Meta) = Alt
# C-x,C-c - Exit
# C-x,C-s - Save
# C-Space - Start selection
# C-w - Cut
# M-w - Copy
# C-k - Cut to endline jkfsd
# C-y - Yank, Paste
# M-Y - Yank buffer
# C-x, 3 - Vertical split
# ....., 2 - Horizontal
# C-x, 1 - One
# C-x, 0 - Close current
# C-x, o - Other windows
# M-x  - Execute command

# C-g - Escape, Cancel


*/
