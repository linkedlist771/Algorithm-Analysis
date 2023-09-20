#include <iostream>

template <class T>
void Mult(T** a, T** b, T** c, int m, int n, int p) {
    for (int i = 0; i < m; i++) 
        for (int j = 0; j < p; j++) {
            T sum = 0;
            for (int k = 0; k < n; k++)
                sum += a[i][k] * b[k][j];
            c[i][j] = sum;
        }
}

int counter = 0;

template <class T>
void CountedMult(T** a, T** b, T** c, int m, int n, int p) {
    for (int i = 0; i < m; i++) 
        for (int j = 0; j < p; j++) {
            T sum = 0;
            for (int k = 0; k < n; k++) {
                sum += a[i][k] * b[k][j];
                counter++;
            }
            c[i][j] = sum;
        }
}

int main() {
    int sizes[] = {2, 3, 4}; // 你可以根据需要增加更多的大小
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]);

    for (int m_idx = 0; m_idx < num_sizes; m_idx++)
        for (int n_idx = 0; n_idx < num_sizes; n_idx++)
            for (int p_idx = 0; p_idx < num_sizes; p_idx++) {
                int m = sizes[m_idx];
                int n = sizes[n_idx];
                int p = sizes[p_idx];

                // 初始化矩阵
                int** a = new int*[m];
                int** b = new int*[n];
                int** c = new int*[m];
                for (int i = 0; i < m; i++) {
                    a[i] = new int[n];
                    c[i] = new int[p];
                }
                for (int i = 0; i < n; i++) {
                    b[i] = new int[p];
                }

                // 填充矩阵
                for (int i = 0; i < m; i++)
                    for (int j = 0; j < n; j++)
                        a[i][j] = 1;
                for (int i = 0; i < n; i++)
                    for (int j = 0; j < p; j++)
                        b[i][j] = 1;

                counter = 0;
                CountedMult(a, b, c, m, n, p);
                std::cout << "For m=" << m << ", n=" << n << ", p=" << p << ":\n";
                std::cout << "Total multiplications: " << counter << std::endl;
                std::cout << "Expected multiplications: " << m * n * p << "\n\n";

                // 清理内存
                for (int i = 0; i < m; i++) {
                    delete[] a[i];
                    delete[] c[i];
                }
                for (int i = 0; i < n; i++) {
                    delete[] b[i];
                }
                delete[] a;
                delete[] b;
                delete[] c;
            }

    return 0;
}
