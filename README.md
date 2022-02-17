Hezekiah Branch <br/>
Wed Feb 16 2022 <br/>
Partial Sums

# Partial-Sum-Playground
Analyze a given series with useful calculations, including the nth partial sum

Assumes terminal/command line usage

# Example
\>>> from partial_sum import PartialSum <br/>
\>>> fx = lambda x : (-1)**x / (x)**0.5 <br/>
\>>> p = PartialSum(fx, 1, 1000000, True) <br/>
Final result available at .result or by calling 'print()' on PartialSum object. <br/>
To view the output of f(x) for each n as n approaches infinity, use .test to view the entire list. <br/>
To view the nth partial sum (i.e. the limit if input is an infinite series), use .tail to view output. <br/>
To observe if tail approaches zero, use .zero_tail (checks margin of 1e-7). <br/>
\>>> p.tail <br/>
5.000011249218367e-10 <br/>
\>>> p.zero_tail <br/>
True <br/>
