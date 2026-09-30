#include <iostream>
#include <vector>

double trapezoidalQuad(double (*f)(double), double a, double b, double dx){
    int N = int((b-a)/dx) + 1;
    std::vector<double> w(N, 1.0);
    w[0] = w[N-1] = 0.5;
    double result = 0.0;
    dx = (b-a)/double(N);
    for (int i = 0; i < N; ++i) {
        double x = a + i*dx;
        result += w[i]*f(x);
        }
    return result*dx;
}

double f(double x) {
    return (x- 2.0)*(x- 2.0)*(x- 2.0)- 3.5*x + 8.0;
}

int main() {
    std::cout.precision(15);
    std::cout << trapezoidalQuad(f, 0.0, 4.0, 0.1) << std::endl;
    return 0;
}