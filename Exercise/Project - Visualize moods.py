import streamlit as st
from plotly.express import line
from backend import sent

## I kept getting: ValueError: Cannot accept list of column references or list of columns for both `x` and `y`. Turns out it had something to do with directories
## Possible Solution: https://www.udemy.com/course/the-python-mega-course/learn/lecture/34604936#questions/22136191
## See the doc string at the end to see why this issue was resolved using os library.
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script directory
os.chdir(script_dir)


d, p, n = sent()

st.title("Dairy Tone")
st.subheader("Positivity Chart")
figp = line(x=d, y=p, labels={"x": "Dates", "y": "Positivity"})
st.plotly_chart(figp)

st.subheader("Negativity Chart")
fign = line(x=d, y=n, labels={"x": "Dates", "y": "Negativity"})
st.plotly_chart(fign)

"""
Execution Context Differences

Standard Python Execution:
When you run a Python script, the print function outputs directly to the console. This is a straightforward operation that doesn’t depend on the working directory or the execution context as long as the data is correctly retrieved.

Streamlit Execution:
Streamlit runs your script in a slightly different environment. It watches for changes in the script and reruns it to update the web app dynamically. This can sometimes lead to issues if the working directory isn’t set correctly, as Streamlit might not be able to find the necessary files or modules.

Working Directory Impact

Without os.chdir(script_dir):
When you import and call sent(), it retrieves the data correctly because the import statement works based on the script’s directory.
However, when Streamlit tries to display the data using st.write(d, p, n), it might be running in a different working directory. This discrepancy can cause Streamlit to fail in accessing the data correctly, leading to empty lists being displayed.

With os.chdir(script_dir):
By explicitly setting the working directory to the script’s directory, you ensure that both the data retrieval and Streamlit’s data display operations are consistent.
This means that when Streamlit reruns the script, it does so in the correct directory, allowing it to access and display the data properly.

Why print Works but st.write Doesn’t:
print(d, p, n):
Directly outputs the data to the console. The data is already in memory, so it doesn’t depend on the working directory.

st.write(d, p, n):
Streamlit’s st.write function tries to display the data in the web app. If the working directory is incorrect, Streamlit might not be able to access the data correctly, leading to empty lists.
"""