#include <iostream>
#include <vector>
#include <string>
#include <random>
// 'classes.h' includes the class declarations
#include "classes.h"

// Class constructor
CellSim::CellSim(std::string initial, std::string rule)
{
    // Using the 'this' keyword is not required; this is what the compiler does
    // automatically (but I think it's easier to read this way, more Pythonic)
    this -> size = initial.size();
    this -> initial = initial;
    this -> rule = rule;
}


// Class destructor
CellSim::~CellSim()
{
}


std::string CellSim::next(std::string current)
{
    std::string extended = '0' + current + '0';
    std::string next_gen;

    for (int i = 0; i < (this -> size); i ++) 
    {
        int first;
        int second;

        if (extended[i] == '0') {first = 0;}
        else {first = 1;}

        if (extended[i + 1] == '0') {second = 0;}
        else {second = 1;}

        int sum = first + second;
        
        if (sum == 0) {next_gen += (this -> rule[0]);}
        else if (sum == 1) {next_gen += (this -> rule[1]);}
        else if (sum == 2) {next_gen += (this -> rule[2]);}
    }
    return next_gen;
}


void CellSim::run()
{   
    std::string current = this -> initial;

    for (int i = 0; i < (this -> size); i ++)
    {
        std::cout << current << '\n';
        current = this -> next(current);
    }
}

