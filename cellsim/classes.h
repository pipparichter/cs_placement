#pragma once 

#include <string>

class CellSim
{
    public:
    
    // Class constructor
    CellSim(std::string initial, std::string rule);
    // Class destructor
    ~CellSim();
    void run();


    private:

    std::string next(std::string current);
    
    // The setup which initializes the simulation 
    std::string initial;
    // Each index of the rule string 
    std::string rule;
    // 'size' is the dimension of the simulation
    int size;
    
};
