#include <vector>
#include <algorithm>
#include <iostream>
#include <array>
using namespace std;

extern "C" __declspec(dllexport) short* solver(short* sud, short x, short y, short* res) {
    short* sudoku = new short[81];
    copy(sud, sud + 81, sudoku);
    

    if (sudoku[y * 9 + x] == 0) {
        vector<short> field3x3;
        for (short i = 0; i < 3; i++) {
            for (short j = 0; j < 3; j++) {
                short element = sudoku[(y - y % 3 + i) * 9 + x - x % 3 + j];
                if (element != 0) {
                    field3x3.push_back(element);
                }
            }
        }
        array<short, 9> column;
        for (short i = 0; i < 9; i++)
        {
            column[i] = sudoku[i * 9 + x];
        }
        array<short, 9> row;
        for (short i = 0; i < 9; i++)
        {
            row[i] = sudoku[y * 9 + i];
        }
        for (short digit = 1; digit < 10; digit++) {
            if (find(row.begin(), row.end(), digit) == row.end() &&
                find(column.begin(), column.end(), digit) == column.end() &&
                find(field3x3.begin(), field3x3.end(), digit) == field3x3.end())
            {
                sudoku[y * 9 + x] = digit;
                if (!(x == 8 && y == 8)) {
                    res = solver(sudoku, (x + 1) % 9, y + (x + 1) / 9, res);
                    if (res[0] != 0) {
                        return res;
                    }
                }
                else {
                    res[0] = 1;
                    return sudoku;
                }
            }
        }
    }
    else {
        if (!(x == 8 && y == 8)) {
            res = solver(sudoku, (x + 1) % 9, y + (x + 1) / 9, res);
        }
        else {
            return sudoku;
        }
    }
    delete[]sudoku;
    return res;
}


//int main() {
//    short res[81];
//    res[0] = 0;
//
//    short s[81] = { 7, 5, 2, 8, 0, 0, 0, 0, 9, 6, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 9, 0, 5, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 9, 0, 8, 0, 4, 0, 0, 2, 0, 7, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 6, 0, 0 };
//        
//
//    short* result = solver(s, 0, 0, res);
//    for (short i = 0; i < 9; i++)
//    {
//        for (short j = 0; j < 9; j++)
//        {
//            cout << result[i * 9 + j] << ' ';
//        }
//        cout << endl;
//    }
//    cout << res[0];
//    //delete[]res;
//    char a;
//    cin >> a;
//}