# Will cork on it to make it precise

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

print(
  "\nHey, " + name + "." " Let's begin by finding out what your body weight(in kg) is?\n"
)
weight = int(input())

print(
  """
  Cool!
  .
  How about your height(in cm)?\n
  """
)
height = int(input())

bmi = (weight / height) * 100

if bmi < 18.5:
  print(
    """
    Huh, we need to add some more weight.
    You fall within the underweight range..\n
    """
  )
elif bmi > 18.5 and bmi < 24.9:
  print(
    f"Hey " + name + ",\n" + str(bmi) + " is within the Healthy Weight range.\n" + "Awesome!\n"
  )
elif bmi > 25.0 and bmi < 29.9:
  print(
    """
    Huh, we need to cut it up a little.
    You fall within the overweight range..\n
    """
  )
else:
  print(
    f"Whoa! " + str(bmi) + " is within obese range!!!"
  )
