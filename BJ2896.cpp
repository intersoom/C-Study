#include <iostream>
using namespace std;

int main() {
    double Min(double a, double b, double c);

    double orange = 0;
    double apple = 0;
    double pineapple = 0;

    int orangeP = 0;
    int appleP = 0;
    int pineappleP = 0;

    double orangeX = 0;
    double appleX = 0;
    double pineappleX = 0;

    double orangeR = 0;
    double appleR = 0;
    double pineappleR = 0;

    double x = 0;

    cin >> orange >> apple >> pineapple;
    cin >> orangeP >> appleP >> pineappleP;

    orangeX = orange / orangeP;
    appleX = apple / appleP;
    pineappleX = pineapple / pineappleP;

    x = Min(orangeX, appleX, pineappleX);

    orangeR = orange - orangeP * x;
    appleR = apple - appleP * x;
    pineappleR = pineapple - pineappleP * x;

    cout.precision(10);

    if (orangeR <= 0)
        cout << 0 << " ";
    else
        cout << orangeR << " ";

    if (appleR <= 0)
        cout << 0 << " ";
    else
        cout << appleR << " ";

    if (pineappleR <= 0)
        cout << 0 << " ";
    else
        cout << pineappleR;



    return 0;
}

double Min(double a, double b, double c){
    double min = 0.0;

    if (a <= b){
        min = a;
    } else if (b > a){
        min = b;
    }

    if (min <= c){
        min = min;
    } else if (min > c){
        min = c;
    }

    return min;

}