#include "stdio.h"
#include "math.h"
#include "stdlib.h"

// int k=10;
// int * l = &k ;
//  *l

//#define INCORRECT_PROGAM 1;

#define PART_SIZE 1024;

struct result_s {
  int len;
  double * x;
  double * y;
};

struct params_s {
  double k;
  double Te;
};

typedef struct result_s result_t;
typedef struct params_s params_t;

// result_t r1;  // r1.len
// result_t * rr = &r1; // (*rr).len; rr->len

typedef double (*f_t)(double x, double Y, void * data);

void realloc_arr(double ** arr, int number) {
  *arr = realloc(*arr, number * sizeof(double));
}

result_t * euler(f_t f, double x0, double F0,
                 double eps, double h,
                 int m,
                 void * data) {
  double x = x0;
  double F = F0;
  int c = 0;
  int num_cells = 0;
  double deltaF;
  result_t * r = malloc(sizeof(result_t));
  r->len=0;
  r->x = NULL;
  r->y = NULL;

  while (1) {
    if (c % m == 0) {

#ifndef INCORRECT_PROGAM
      //printf("Work!\n");
      if (r->len >= num_cells) {
        num_cells += PART_SIZE;
        realloc_arr(&(r->x), num_cells);
        realloc_arr(&(r->y), num_cells);
      }
#endif
      r->x[r->len]=x;
      r->y[r->len]=F;
      (r->len)++;
    }

    deltaF=f(x, F, data)*h;

    if (fabs(deltaF)<eps) {
      break;
    }

    x+=h;
    F+=deltaF;
    c++;
  }
  return r;
}

double kettle_diffur(double t, double T, void * data) {
  params_t * p = (params_t *) data;

  return -p->k * (T - p->Te);
}

void free_result(result_t * r){
  free(r->x);
  free(r->y);
  free(r);
};

void solve(double t0, double T0, double k, double Te,
           double eps, double h, int m) {

  result_t * r;
  params_t data;

  data.k=k;
  data.Te=Te;

  r = euler(kettle_diffur,
            0.0,
            100.0,
            0.01,
            0.1,
            m,
            &data
            );


  for (int i=0; i < r->len; i++) {
    printf("%f\t%f\n", r->x[i], r->y[i]);
  }

  free_result(r);
}


int main(int argc, char ** argv) {
  int m = 1000;
  printf("Hello, World!\n");
  printf("This is %s program (having %i arguments) "
         "for a Cauchy problem "
         "solving.\n", argv[0], argc);
  if (argc>=2) {
    m=atoi(argv[1]);
  }
  solve(0.0,
        100.0,
        0.01,
        24.0,
        0.01,
        0.1,
        m
        );
}
