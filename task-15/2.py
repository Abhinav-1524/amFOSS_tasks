num_test_cases = int(input())
for i in range(num_test_cases):
  n = int(input())
  fib = [1, 2]
  sum = 0
  
  while fib[-1] + fib[-2] <= n:
   
    fib.append(fib[-1] + fib[-2])

  
  for i in fib:
    if i % 2 == 0:
      sum += i

  print(sum) 

        
        
    
