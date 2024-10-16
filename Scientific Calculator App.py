{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPqUF2n/iNeTX3hxV8qR9pg",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sudaidhanif/Scientific-Calculator-2/blob/main/Scientific%20Calculator%20App.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import math\n",
        "from scipy.special import erf\n",
        "\n",
        "# Function to calculate scientific operations\n",
        "def scientific_calculator(expression):\n",
        "    try:\n",
        "        result = eval(expression, {\"__builtins__\": None}, {\n",
        "            \"sin\": np.sin,\n",
        "            \"cos\": np.cos,\n",
        "            \"tan\": np.tan,\n",
        "            \"log\": np.log,\n",
        "            \"exp\": np.exp,\n",
        "            \"pi\": np.pi,\n",
        "            \"e\": np.e,\n",
        "            \"sqrt\": np.sqrt,\n",
        "            \"abs\": abs,\n",
        "            \"pow\": pow,\n",
        "            \"factorial\": math.factorial,\n",
        "            \"erf\": erf  # Include error function\n",
        "        })\n",
        "        return result\n",
        "    except Exception as e:\n",
        "        return str(e)\n",
        "\n",
        "# Function to plot graphs\n",
        "def plot_graph(func, x_range):\n",
        "    x = np.linspace(x_range[0], x_range[1], 400)\n",
        "    try:\n",
        "        y = eval(func, {\"__builtins__\": None}, {\n",
        "            \"sin\": np.sin,\n",
        "            \"cos\": np.cos,\n",
        "            \"tan\": np.tan,\n",
        "            \"log\": np.log,\n",
        "            \"exp\": np.exp,\n",
        "            \"pi\": np.pi,\n",
        "            \"e\": np.e,\n",
        "            \"sqrt\": np.sqrt,\n",
        "            \"abs\": abs,\n",
        "            \"erf\": erf  # Include error function\n",
        "        })\n",
        "        plt.figure(figsize=(10, 5))\n",
        "        plt.plot(x, y, label=f'y = {func}')\n",
        "        plt.title('Graph of the function')\n",
        "        plt.xlabel('x')\n",
        "        plt.ylabel('y')\n",
        "        plt.grid()\n",
        "        plt.axhline(0, color='black', lw=1)\n",
        "        plt.axvline(0, color='black', lw=1)\n",
        "        plt.legend()\n",
        "        st.pyplot(plt)\n",
        "    except Exception as e:\n",
        "        st.error(f\"Error in plotting: {str(e)}\")\n",
        "\n",
        "# Streamlit app layout\n",
        "st.title(\"Scientific Graphical Calculator\")\n",
        "st.write(\"### You can use the following functions:\")\n",
        "st.write(\"- Basic: +, -, *, /\")\n",
        "st.write(\"- Trigonometric: sin(x), cos(x), tan(x)\")\n",
        "st.write(\"- Logarithmic: log(x)\")\n",
        "st.write(\"- Exponential: exp(x)\")\n",
        "st.write(\"- Square root: sqrt(x)\")\n",
        "st.write(\"- Factorial: factorial(n)\")\n",
        "st.write(\"- Error function: erf(x)\")\n",
        "st.write(\"- Constants: pi, e\")\n",
        "\n",
        "# Calculation section\n",
        "st.subheader(\"Calculate\")\n",
        "expression = st.text_input(\"Enter a mathematical expression (e.g., 2 * sin(pi / 4) + log(10) + erf(1)):\")\n",
        "if st.button(\"Calculate\"):\n",
        "    result = scientific_calculator(expression)\n",
        "    st.write(f\"Result: {result}\")\n",
        "\n",
        "# Plotting section\n",
        "st.subheader(\"Plot a Function\")\n",
        "function = st.text_input(\"Enter a function of x (e.g., sin(x), x**2, erf(x)): \")\n",
        "x_start = st.number_input(\"Start of x range\", value=-10.0)\n",
        "x_end = st.number_input(\"End of x range\", value=10.0)\n",
        "\n",
        "if st.button(\"Plot\"):\n",
        "    plot_graph(function, (x_start, x_end))\n"
      ],
      "metadata": {
        "id": "4ZXOYvoXMBJd"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}