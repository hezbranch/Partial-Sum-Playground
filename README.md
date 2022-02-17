Hezekiah Branch <br/>
Wed Feb 16 2022 <br/>
Partial Sums

# Partial Sum Playground
Purpose: Analyze a given series with useful calculations, including the nth partial sum

Usage: Designed for terminal/command line usage. Clone, unzip, and launch a terminal from repo location.

Alternate Environments: Jupyter Notebooks, analysis programs, scripts, etc.

# Example
\>>> from partial_sum import PartialSum <br/>
\>>> fx = lambda x : (-1)**x / (x)**0.5 <br/>
\>>> p = PartialSum(fx, 1, 1000000, True) <br/>
Final result available at .result or by calling 'print()' on PartialSum object. <br/>
To view the output of f(x) for each n as n approaches infinity, use .test to view the entire list. <br/>
To view the nth partial sum (i.e. the limit if input is a convergent infinite series), use .tail to view output. <br/>
To observe if tail approaches zero, use .zero_tail (checks margin of 1e-7). <br/>
\>>> p.tail <br/>
5.000011249218367e-10 <br/>
\>>> p.zero_tail <br/>
True <br/>

# Displaying graphs

The output from .result integrates well with data analysis and plotting libraries such as pandas and matplotlib. 

\>>> import pandas as pd <br/>
\>>> import matplotlib.pyplot as plt <br/>

\>>> small_data = {i : p.test[i-1] for i in range(p.lower, 100)} <br/>
\>>> pd.Series(small_data).plot.line(title="Terms of Series Distributed by N", xlim=(1, len(small_data))) <br/>
<matplotlib.axes._subplots.AxesSubplot object at > <br/>
\>>> plt.show() <br/>

![Sample visualization of series terms](https://github.com/hezbranch/DemoImages/blob/main/Figure_1.png)

\>>> small_sum_data = {i : p.result[i-1] for i in range(1, 100)} <br/>
\>>> pd.Series(small_sum_data).plot.line(title="Partial Sums Distributed by N", xlim=(1, len(small_sum_data))) <br/>
<matplotlib.axes._subplots.AxesSubplot object at > <br/>
\>>> plt.show() <br/>

![Sample visualization of partial sums as n approaches infinity](https://github.com/hezbranch/DemoImages/blob/main/Figure_2.png)

# Additional Info
In the images above, we have an alternating series with non-increasing term magnitude and a limit that approaches zero, indicating convergence. This tool provides visual artifacts of convergence which can supplement tests such as the Alternating Series Test.

For more information about mathematical analysis and convergence tests, see:

https://en.wikipedia.org/wiki/Alternating_series_test

Citation: Wikipedia contributors. (2022, January 24). Alternating series test. In Wikipedia, The Free Encyclopedia. Retrieved 03:33, February 17, 2022, from https://en.wikipedia.org/w/index.php?title=Alternating_series_test&oldid=1067674590


