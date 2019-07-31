import sys


# Class definitions ####################################################

# Create a StackError class to deal with Stack-related problems
class StackError(Exception):
    pass

# Create a general Stack class for managing the Hanoi pegs (a, b, and c)
# which adheres to LIFO rules
class Stack:
 
    # Stack can be initialized with a list
    def __init__(self, contents):
        
        self.contents = contents

    
    # Convert the Stack contents into a pretty string
    def __str__(self):
        
        return " ".join([str(disk) for disk in self.contents])            


    # Provide the number of elements in the Stack
    def size(self):
        
        return len(self.contents)
    

    # Check if the Stack is empty
    def is_empty(self):
        
        return (len(self.contents) == 0)
    

    # Provide the top element in the Stack
    def top(self):
        
        if self.is_empty():
            return 0 
        else:
            return self.contents[-1]

    
    # Remove a disk from the Stack and returns the disk's value
    def pop(self):

        popped = self.top()
        
        # Check to make sure the Stack is not empty
        if self.is_empty():
            raise StackError("There are no disks in the Stack object.") 
        else:
            self.contents = self.contents[:-1]
            return popped

    
    # Add a disk to the Stack
    def push(self, disk):
        
        # Check to make sure the pushed disk is not greater than the top disk
        # This would not normally be in a generalized Stack class, but given I'm not actually
        # submitting this assignment, putting the exception here makes my life easier
        if (self.top() > disk) or (self.is_empty()):
            self.contents += [disk]
        elif self.top() < disk:
            raise StackError("Not a viable move.")



class Hanoi:
    
    def __init__(self, initial):
        
        self.a = Stack(initial)
        self.b = Stack([])
        self.c = Stack([])

        self.disk_num = len(initial)

        self.count = 0


    def __str__(self):
        
        a_str = str(self.a)
        b_str = str(self.b)
        c_str = str(self.c)

        return  "A: " + a_str + '\n' + "B: " + b_str + '\n' + "C: " + c_str + '\n'
    

    # Takes two two Stacks as input and pushes the top disk of the source Stack
    # to the destination Stack
    def move(self, source, destination):
        
        # If the move is invalid, an exception defined in the Stack class will
        # be thrown
        to_push = source.pop()
        destination.push(to_push)

        # Equivalent to self.display(), I just thought this looked cleaner
        print(self)
    

    def recursive_move(self, source, destination, auxiliary, N):
        # Move top N - 1 from source to auxiliary
        # Move last remaining from source to destination
        # Move N-1 from auxiliary to destination
        
        # Keeps count of how many moves were needed
        self.count += 1

        while True:
            # If you are addressing the top of the source Stack...
            if N == 1:
                self.move(source, destination)
                break
            # If you are not addressing the top of the souce Stack...
            elif N > 1:
                # The destination becomes the auxiliary Stack
                # The auxiliary Stack becomes the destination
                new_destination = auxiliary
                new_auxiliary = destination

                # We are now addressing one position closer to the top of the source Stack, 
                # so decrement N (but only in the scope of the recursive call)
                self.recursive_move(source, new_destination, new_auxiliary, N - 1)

                self.move(source, destination)

                self.recursive_move(auxiliary, destination, source, N - 1)

                break
    

    def solve(self):

        self.recursive_move(self.a, self.c, self.b, self.disk_num)

        print(f"This game took {self.count} moves.")
        
        





##############################################################################


# Short main function for implementing Hanoi towers algorithm 
def main():
    
    initial = [int(disk) for disk in sys.argv[1:]] 
    
    hanoi = Hanoi(initial)
    print(hanoi)

    hanoi.solve()

# Call the main function 
main()
