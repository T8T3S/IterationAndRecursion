def recursively_get_factorial(num):
  if num == 0 or num == 1:
    return 1
  else:
    return num * recursively_get_factorial(num - 1)

def interatively_get_factorial(num):
  fact = 1
  for n in range(2, num+1):
    fact = n*fact
  return(fact)

def main():
  num_list = [0, 5, 10, 25, 50 ,100]
  print('Factrials from a  iterative function.')
  for num in num_list:
    print(f'{num} ! = {interatively_get_factorial(num)}')
  print('Factrials from a recursive function.')
  for num in num_list:
    print(f'{num} ! = {recursively_get_factorial(num)}')

if __name__ == "__main__":
  main()