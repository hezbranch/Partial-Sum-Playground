# Calculate Partial Sums
# Hezekiah Branch
# Feb 16, 2022

class PartialSum:
    # Object initialization
    def __init__(self, fx=None, lower=0, upper=0, auto=False):
        self.fx = fx
        self.lower = lower
        self.upper = upper
        self.test = None
        self.result = None
        self.tail = None
        self.zero_tail = None
        self.auto = auto
        
        # Run partial sum on auto-mode if user specifies
        # else, user will call each function manually
        if auto:
            self.driver()
       
    # Custom define print function
    def __str__(self):
        return "{}".format(self.result)

    # Validate function inputted correctly
    def validate_function(self):
        try:
            str(type(self.fx)) == "<class 'function'>"
        except TypeError:
           print('First parameter must be a function.')
           
    # Validate bound inputs are numberic
    def validate_bounds(self):
        try:
            str(self.lower).isnumeric() and str(self.upper).isnumeric()
        except TypeError:
           print('Upper and lower bounds must be numbers.')
           
    # Chain input validation
    def validate(self):
        try:
            self.validate_function() and self.validate_bounds()
        except TypeError:
            print("Use syntax {VAR_NAME} = PartialSum(function, lower, upper, auto=True).")
        
    # Calculate the terms of the partial sum
    def initialize(self):
        self.test = [self.fx(x) for x in range(self.lower, self.upper)]
    
    # Calculate partial sum using contiguous values
    def partial_sum(self):
        sum = lambda test : [self.test[0]] + [self.test[i] + self.test[i-1] for i in range(1, len(self.test))]
        self.result = sum(self.test)
        self.tail = self.result[-1]
        if abs(0 - self.tail) < 1e-7:
            self.zero_tail = True
    
    # Driver function for the class
    def driver(self):
        # Validate input
        self.validate()
        # Begin analysis
        self.initialize()
        # Calculate summation
        self.partial_sum()
        # Output location of result
        print("Final result available at .result or by calling 'print()' on PartialSum object.")
        print("To view the output of f(x) for each n as n approaches infinity, use .test to view the entire list.")
        print("To view the nth partial sum (i.e. the limit if input is an infinite series), use .tail to view output.")
        print("To observe if tail approaches zero, use .zero_tail (checks margin of 1e-7).")
           
