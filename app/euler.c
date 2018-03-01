#include "stdio.h"
#include "math.h"
#include "stdlib.h"


#define RESULT_DELTA 1024

struct cooling_struct {
  double k;
  double Tenv;
};

struct rlen {
  int len;
};

typedef struct cooling_struct cooling_data;
typedef double (* f_t)(double x, double F, void * data);
typedef struct rlen rlen_t;


double cooling_f(double x,
                 double F,
                 void * data) {

  cooling_data * s = NULL;

  s = (cooling_data *) data;

  return -(s->k)*(F - s->Tenv );
}

void release(double * result) {
  free(result);
}

rlen_t * new_rlen() {
  rlen_t * s = malloc(sizeof(rlen_t));
  s->len = 0;
  return s;
}

int get_len(rlen_t * s) {
  return s->len;
}

void release_rlen(rlen_t * s) {
  free(s);
}

double * euler(f_t f,
               double x0,
               double F0,
               double h,
               double eps,
               int m,
               void * data,
               int * len
               ) {

  double * result = NULL;
  double x = x0;
  double F = F0;
  // F=F(x)=F(x0)
  double dF, deltaF;
  int c = 0;
  int bt = 0; // length of allocated array of results.
  int bc = 0;

  *len = 0;

  do {
    if (c++ % m == 0) {
      if (*len >= bt) {
        bc++;
        result = realloc(result, RESULT_DELTA * bc * sizeof(double));
        bt+=RESULT_DELTA;
      }
      result[(*len)++] = F;
    }

    dF=f(x, F, data);
    deltaF = dF * h;
    // printf("dF= %f \n", dF);

    x+=h;
    F+=deltaF;
    // F=F(x)

  } while (fabs(deltaF)>eps);


  return result;
}

double * calculate(double k,
                   double Tenv,
                   double t0,
                   double T0,
                   double h,
                   double eps,
                   int m,
                   rlen_t * lenp
                   ) {

  cooling_data d;

  d.k = k;
  d.Tenv = Tenv;

  return euler(cooling_f,
                 t0,
                 T0,
                 h,
                 eps,
                 m,
                 &d,
                 &(lenp->len)
               );

}

#ifdef TEST

int main(int argc, char ** argv) {
  rlen_t d_len;
  double * result;

  printf("The program for solving Cauchy problems.\n");

  result = calculate(0.01,
                     24,
                     0.0,
                     100.0,
                     0.1,
                     0.01,
                     10,
                     &d_len);

  for (int i=0; i<d_len.len; i++) {
    printf("%f\n", result[i]);
  }
  release(result);
}


#endif // TEST

/*
# C=Ctrl, M=Alt
# C-c, C-s
# C-x, C-c
# C-k "Kill"
# emacs
# C-w
# C-Space - start selection
# M-w - Copy block
# c-y "Yank"


*/
