print(
  """
  Hallo,
  Welcome to Python.
  In this program, we are going to try help you determine your Body Mass Index(BMI).
  .
  Let's begin with the introductions,
  What's your name?\n
  """
)
name = input()

print("\nHey, " + name + "." "Let's begin by finding out what your body weight is?\n")
weight = input()

print(
  """
  \nCool!
  .
  How about your height?\n
  """
)
height = int(input())

bmi = weight/height

if bmi < 18.5:
  print(
    """
    \nHuh, we need to add some more weight.
    You fall within the underweight range..\n
    """
  )
elif bmi > 18.5 & bmi < 24.9:
  print(
    "\nHey " + name + ",\n" + bmi + " is within the Healthy Weight range.\n" + "Awesome!\n"
  )
elif bmi > 25.0 & bmi < 29.9:
  print(
    """
    \nHuh, we need to cut it up a little.
    You fall within the overweight range..\n
    """
  )
else:
  print(
    "\nWhoa! " + bmi + " is within obese range!!!"
  )
