#!python

import random
import sys



def main():

    gen_size = int(sys.argv[1])
    gens = int(sys.argv[2])
    rule = sys.argv[3:]
    
    # Create a list of length gen_size of randomly-placed ones and zeros
    seed = [random.choice((0, 1)) for i in range(gen_size)]

    # Initialize the automaton using the random seed and the given rule
    atmn = Automaton(seed, rule, gen_size)
    
    for gen in range(gens):
        
        print(atmn)

        atmn.next_gen()



class Automaton:


    # Initialize the class
    def __init__(self, seed, rule, gen_size):
        
        self.gen_size = gen_size

        self.current_gen = seed

        self.sum_zero = [int(rule[0])]
        self.sum_one = [int(rule[1])]
        self.sum_two = [int(rule[2])]
        self.sum_three = [int(rule[3])]


    def next_gen(self):
        
        # Add zeros to either side of the list to handle with edge cells (not included when
        # current_gen is reassigned)
        current = [0] + self.current_gen + [0]
        new = []

        i = 0
        # Find the sum of each set of three cells for the length of the current_gen
        # Set upper bound to one out-of-range on the last iteration, as slicing is non-inclusive 
        while (i < self.gen_size):
            
            summed = sum(current[i:i + 3])

            if summed == 0:
                new += self.sum_zero
            elif summed == 1:
                new += self.sum_one
            elif summed == 2:
                new += self.sum_two
            else: # if summed == 3: 
                new += self.sum_three

            i += 1
        
        # Reassign current_gen
        self.current_gen = new


    def __str__(self):
        
        gen = [str(cell) for cell in self.current_gen]
        
        return "".join(gen)


####################################################################

# A single-line function call to main to begin automaton
main()
