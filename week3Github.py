def fibonacci_series(n):
  if n <= 0:
    print("Please enter a positive integer.")
  elif n == 1:
    print([0])
  else:
    series = [0, 1]
    for _ in range(2, n):
      series.append(series[-1] + series[-2])
    print(series)
n_terms = int(input("Enter the number of terms: "))
fibonacci_series(n_terms)
