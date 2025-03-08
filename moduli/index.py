import streamlit as st

def calculate(num1, num2, operation):
    if operation == 'Addiction':
        result = num1+num2
    elif operation == 'Subtraction':
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == 'Division':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Nuk munesh me pjestu me zero"
    return result

def main():
      st.title("Streamlit Calculater")
      num1 = st.number_input("Enter your first number" , step=1)
      num2 = st.number_input("Enter your second number" , step=2)
      operation = st.radio("Select operation", ['Addiction', 'Subtraction', 'Multiply', 'Division'])

      result = calculate(num1, num2, operation)

      st.write(f"Result of the {operation} of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()


