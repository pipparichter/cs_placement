#include <iostream>
#include <vector>
#include <random>
// The 'classes' header file contains the relevant class declarations
#include "classes.h"

int main() 
{
    // Get the initial generation and rule from standard input
    std::string initial;
    std::cout << "Initial generation: ";
    std::cin >> initial;

    std::string rule;
    std::cout << "Rule: ";
    std::cin >> rule;
    
    std::cout << '\n';

    CellSim cellsim(initial, rule);
    cellsim.run();    
}
