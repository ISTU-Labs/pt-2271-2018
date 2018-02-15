%module euler
%{

  struct rlen {
    int len;
  };

 typedef struct rlen rlen_t;

 void release(double * result);

 double * calculate(double k,
                    double Tenv,
                    double t0,
                    double T0,
                    double h,
                    double eps,
                    int m,
                    rlen_t * lenp
                   );

 rlen_t * new_rlen();
 int get_len(rlen_t * s);
 void release_rlen(rlen_t * s);

 double get_i(double * arr, int i) {
   return arr[i];
 }

%}

void release(double * result);

rlen_t * new_rlen();
int get_len(rlen_t * s);
void release_rlen(rlen_t * s);

double * calculate(double k,
                   double Tenv,
                   double t0,
                   double T0,
                   double h,
                   double eps,
                   int m,
                   rlen_t * lenp
                   );

double get_i(double * arr, int i);
