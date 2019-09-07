#include <iostream>
#include <vector>
#include <string>
#include <random>
// 'classes.h' includes the class
// declarations
#include <classes.h>

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

void CellSim::display() 
{
    std::cout << cellsim::status << '\n';
}

void CellSim::run()
{   
    fot (int i = 0; i < (this -> size); i ++)
    {
        this -> display()
        this -> next()
    }
}

