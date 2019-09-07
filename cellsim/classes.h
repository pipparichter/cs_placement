#pragma once 

class CellSim
{
    public:
    
    // Class constructor
    CellSim(const char[] initial, const char[] rule);
    // Class destructor
    ~CellSim();

    private:

    void next();
    
    int size;
    
};
