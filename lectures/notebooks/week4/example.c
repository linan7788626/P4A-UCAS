#include <stdio.h>
#include <omp.h>

double simpson_c(double * y, double * x, long N)
{
    double dx = x[1] - x[0];
    double S = 0.0;
    long i;
    for (i=0;i<N;i+=2)
    {
        S += dx/3. * (y[i] + 4.0*y[i+1] + y[i+2]);
    }
    return S;
}

double simpson_c_omp(double * y, double * x, long N, int nThreads)
{
    double dx = x[1] - x[0];
    double S;
    S = 0.0;
    long i;
    #pragma omp parallel \
    num_threads(nThreads) \
	shared(y, x, dx, N, S) \
	private(i)
	{
        double partial_S = 0.0;
		#pragma omp for
        for (i=0;i<(N-1)/2;i++)
        {
            partial_S += dx/3. * (y[2*i] + 4.0*y[2*i+1] + y[2*i+2]);
        }
        #pragma omp critical
        S += partial_S;
    }
    return S;
}
