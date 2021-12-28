#include <iostream>
using namespace std;

int leapYear(int Year);

int main() {

    int startYear = 0;
    int startMonth = 0;
    int startDay = 0;

    int endYear = 0;
    int endMonth = 0;
    int endDay = 0;

    int yearSum = 0;

    int startDaySum = 0;
    int endDaySum = 0;

    int temp = 0;

    cin >> startYear >> startMonth >> startDay;
    cin >> endYear >> endMonth >> endDay;

    //예외처리
    if ((endYear - startYear) == 1000){
        if (endMonth >= startMonth && endDay >= startDay){
            cout << "gg";
            return 0;
        }
    } else if ((endYear - startYear) > 1000){
        cout << "gg";
        return 0;
    }

    //연도 합
    for (int i = startYear; i <= endYear; i++){
        temp = leapYear(i);
        if (temp == 1){
            yearSum += 366;
        }
        if (temp == 0){
            yearSum += 365;
        }
    }

    //시작연도 월/일까지 일의 합
    // 1월: 31일 2월: 28일 or 29일 3월: 31일 4월: 30일 5월: 31일 6월: 30일 7월: 31일 8월: 31일 9월: 30일 10월: 31일 11월: 30일 12월: 31일

    int month[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    temp = leapYear(startYear);

    if (temp == 1) {
        if (startMonth - 1 >= 2){
            for (int i = 0; i < startMonth - 1; i++){
                startDaySum += month[i];
            }
            startDaySum += 1;
        }
        else{
            for (int i = 0; i < startMonth - 1; i++){
                startDaySum += month[i];
            }
        }
    } else if (temp == 0) {
        for (int i = 0; i < startMonth - 1; i++){
            startDaySum += month[i];
        }
    }

    startDaySum += startDay;

    temp = leapYear(endYear);

    if (temp == 1) {
        if (endMonth - 1 >= 2){
            for (int i = 0; i < endMonth - 1; i++){
                endDaySum += month[i];
            }
            endDaySum += 1;
        }
        else{
            for (int i = 0; i < endMonth - 1; i++){
                endDaySum += month[i];
            }
        }
    } else if (temp == 0) {
        for (int i = 0; i < endMonth - 1; i++){
            endDaySum += month[i];
        }
    }

    endDaySum += endDay;

    if (temp == 1){
        endDaySum = 366 - endDaySum;
    } else if (temp == 0){
        endDaySum = 365 - endDaySum;
    }

    yearSum = yearSum - startDaySum - endDaySum;

    cout << "D-" << yearSum;

    return 0;
}

//윤년 판별 함수
int leapYear(int year) {
    if (year % 4 == 0){
        if (year % 100 != 0 || year % 400 == 0) {
            return 1;
        }
        else{
            return 0;
        }
    }
    else{
        return 0;
    }
}