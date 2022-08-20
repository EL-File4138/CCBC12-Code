// Coding: UTF-8

/*
Light_off.cpp
Author: EL_File4138
Notator: EL_File4138

A Solution for CCBC12 Timeline F 1876.
熄灯问题Reduction法求解。
*/

#include <bitset>
#include <memory>
#include <cstring>
#include <iostream>
#include <cmath>

const int W = 10; // 列
const int H = 12; // 行

const int possiblity = pow(2, W);

using namespace std;

bitset<10> source[H], result[H], lights[H];
bitset<10> line;

void input_source() // 原始数据输入函数；
{
    int x;
    for (int i = 0; i < H; i++)
        for (int j = 0; j < W; j++) {
            cin >> x;
            source[i][j] = x;
        }

}

void output_result() // 输出结果函数；
{
    cout << endl;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++){
            cout << result[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
        input_source();
        for (int n = 0; n < possiblity; n++) {
            memcpy(lights, source, sizeof(source)); // 把原始数据赋给新数组方便操作；
            line = n;
            for (int k = 0; k < H; k++) {
                result[k] = line; // 从上往下，保证下一行使上一行全部为0，即熄灯状态；
                for (int j = 0; j < W; j++) {
                    if (line.test(j)) // 判断是否为0；
                    {
                        lights[k][j].flip();
                        lights[k + 1][j].flip();
                        if (j > 0) {lights[k][j - 1].flip();}; // 不是最左边的话左边也要翻转；
                        if (j < H) {lights[k][j + 1].flip();}; // 不是最右边的话右边也要翻转；
                    }
                }
                line = lights[k]; // 把使上一行为0的下一行赋给line，重复上述操作；
            }
            if (lights[H-1].none()) {
                output_result(); // 输出最终结果；
                break;
            }
        }

    }
