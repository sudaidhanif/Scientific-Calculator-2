import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.special import erf

# Function to calculate scientific operations
def scientific_calculator(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {
            "sin": np.sin,
            "cos": np.cos,
            "tan": np.tan,
            "log": np.log,
            "exp": np.exp,
            "pi": np.pi,
            "e": np.e,
            "sqrt": np.sqrt,
            "abs": abs,
            "pow": pow,
            "factorial": math.factorial,
            "erf": erf  # Include error function
        })
        return result
    except Exception as e:
        return str(e)

# Function to plot graphs
def plot_graph(func, x_range):
    x = np.linspace(x_range[0], x_range[1], 400)
    try:
        y = eval(func, {"__builtins__": None}, {
            "sin": np.sin,
            "cos": np.cos,
            "tan": np.tan,
            "log": np.log,
            "exp": np.exp,
            "pi": np.pi,
            "e": np.e,
            "sqrt": np.sqrt,
            "abs": abs,
            "erf": erf  # Include error function
        })
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, label=f'y = {func}')
        plt.title('Graph of the function')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.axhline(0, color='black', lw=1)
        plt.axvline(0, color='black', lw=1)
        plt.legend()
        st.pyplot(plt)
    except Exception as e:
        st.error(f"Error in plotting: {str(e)}")

# Streamlit app layout
st.title("Scientific Graphical Calculator")
st.write("### You can use the following functions:")
st.write("- Basic: +, -, *, /")
st.write("- Trigonometric: sin(x), cos(x), tan(x)")
st.write("- Logarithmic: log(x)")
st.write("- Exponential: exp(x)")
st.write("- Square root: sqrt(x)")
st.write("- Factorial: factorial(n)")
st.write("- Error function: erf(x)")
st.write("- Constants: pi, e")

# Calculation section
st.subheader("Calculate")
expression = st.text_input("Enter a mathematical expression (e.g., 2 * sin(pi / 4) + log(10) + erf(1)):")
if st.button("Calculate"):
    result = scientific_calculator(expression)
    st.write(f"Result: {result}")

# Plotting section
st.subheader("Plot a Function")
function = st.text_input("Enter a function of x (e.g., sin(x), x**2, erf(x)): ")
x_start = st.number_input("Start of x range", value=-10.0)
x_end = st.number_input("End of x range", value=10.0)

if st.button("Plot"):
    plot_graph(function, (x_start, x_end))
