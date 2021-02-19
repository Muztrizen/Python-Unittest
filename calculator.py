# Simple calculator
# author: Muztrizen

def add(x, y):
  """Simple addition function"""
  return x + y


def subtract(x, y):
  """Simple subtraction function"""
  return x - y


def multiply(x, y):
  "Simple multiplication function"
  return x * y


def divide(x, y):
  "Simple division function"
  if y == 0:
    raise ValueError("Can not divide a number by 0.")
  return x / y
