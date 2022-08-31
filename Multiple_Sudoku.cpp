// Coding: UTF-8

/*
Multiple_Sudoku.cpp
Author: EL_File4138
Notator: EL_File4138

! Graveyard, please do not use.
*/


#include <iostream>
#include <set>
#include <algorithm>

const int standard_list[9] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };

using namespace std;

int sudoku_org[9][9];

int sudokuR[9][9];
int sudokuG[9][9];
int sudokuB[9][9];

int Color_Seperation() {

}

bool Eligiblity_Check(int draft_sudoku[9][9]) {
    int H, W, Block;
    for (H = 0; H <= 9; H++) {
        int checklist[9] = {};
        for (W = 0; W <= 9; W++) {
            checklist[W] = draft_sudoku[H][W];
        }
        sort(checklist, checklist + 9);
        if (equal(checklist, checklist + 8, standard_list, standard_list + 8)) {
            continue;
        }
        else {
            return false;
            break;
        }
    }
    for (W = 0; W <= 9; W++) {
        int checklist[9] = {};
        for (H = 0; H <= 9; H++) {
            checklist[H] = draft_sudoku[W][H];
        }
        sort(checklist, checklist + 9);
        if (equal(checklist, checklist + 8, standard_list, standard_list + 8)) {
            continue;
        }
        else {
            return false;
            break;
        }
    }
    return true;
}
