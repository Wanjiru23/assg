def main():
 dollars=dollars_to_float(input("how much was the meal?"))
 percent=percent_to_float("what percentage would you like to tip?")
 tip=dollars*percent
 print(f"leave$(tip:.2f)")
 def dollars_to_float(d):
  dollars_to_float= float (dollars)
  return dollars_to_float
 def percent_to_float(p):
  percent_to_float= float (p)
  return percent_to_float
 main()
  