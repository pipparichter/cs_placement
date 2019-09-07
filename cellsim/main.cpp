#include <iostream>
#include <vector>
#include <random>
// The 'classes' header file contains the relevant class declarations
#include <classes>

int main() 
{
    // Get the initial generation and rule from standard input
    const char[] initial;
    std::cout << "Initial generation: ";
    std::cin >> initial;
    std::cout >> '\n';
    const char[] rule;
    std::cout << "Rule ";
    std::cin >> rule;
    std::cout << '\n';


    CellSim cellsim(initial, rule);
    cellsim.run()    
}
