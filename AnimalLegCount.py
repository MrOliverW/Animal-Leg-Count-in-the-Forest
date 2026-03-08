import unittest
#unittest is Python’s built-in framework for testing. 
#unittest allows you to write "test cases" that automatically verify if your code is behaving exactly as expected.

def count_four_legged_animals(animals):
    # This function counts the number of animals with four legs in the given list of animal arrays.
    four_legged_reference = {'lion', 'deer', 'elephant', 'horse', 'dog', 'cat'}
    # Reference list of four-legged animals for O(1) average time complexity lookups.

    count = 0

    #count = 0 initializes a counter to keep track of how many four-legged animals we find.
    for animal in animals:
        #for animal in animals: iterates through each animal in the input list to check if it is a four-legged animal.
        if animal.lower() in four_legged_reference:
            #normalizes the animal name to lowercase and checks if it exists in the four-legged reference set.
            count += 1
            #If the animal is found in the reference set, we increment our count by 1.

    return count
    # The function returns the total count of four-legged animals found in the input list.

# -- Unit Test Cases --

class TestAnimalCounter(unittest.TestCase):
    #creates a folder for test cases related to counting four-legged animals.
    def test_count_four_legged_animals(self):
        animals = ['lion', 'deer', 'elephant', 'horse', 'dog', 'cat', 'monkey', 'parrot', 'ostrich', 'snake', 'worm', 'spider', 'ant', 'centipede']
        self.assertEqual(count_four_legged_animals(animals), 6)
        #This test case checks a mixed list of animals, ensuring that the function correctly identifies and counts only the four-legged animals.

    def test_no_four_legged_animals(self):
        animals = ['monkey', 'parrot', 'ostrich', 'snake', 'worm', 'spider', 'ant', 'centipede']
        self.assertEqual(count_four_legged_animals(animals), 0)
        #This test case checks a list that contains no four-legged animals, ensuring the function returns 0.

    def test_all_four_legged_animals(self):
        animals = ['lion', 'deer', 'elephant', 'horse', 'dog', 'cat']
        self.assertEqual(count_four_legged_animals(animals), 6)
        #This test case checks a list that contains only four-legged animals, ensuring the function returns the correct count of 6.

    def test_empty_list(self):
        self.assertEqual(count_four_legged_animals([]), 0)
        #This test case checks the function's behavior when given an empty list, which should return a count of 0.

    def test_case_sensitivity(self):
        self.assertEqual(count_four_legged_animals(['LION', 'Elephant', 'dOg']), 3)
        #Checks if the function correctly counts four-legged animals regardless of the case (uppercase or lowercase) of the input strings.

    def test_unknown_animals(self):
        self.assertEqual(count_four_legged_animals(['lion', 'dragon', 'unicorn']), 1)
        '''Checks a list that contains both known four-legged animals and unknown animals, 
         ensuring that only the known four-legged animal is counted.'''
if __name__ == '__main__':
    '''This line checks if the script is being run directly by the user,
    if so, it will execute the unit tests defined in the TestAnimalCounter class.'''
    unittest.main(argv=[''], exit=False)
    '''tells the unittest library to go find every function starting with the word test_ and execute it,
    It also prevents unittest from interpreting any command-line arguments 
    and prevents it from calling sys.exit() after running the tests,
    this is useful in interactive environments like Jupyter notebooks. '''

