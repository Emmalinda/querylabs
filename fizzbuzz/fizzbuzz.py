def fizz_buzz(n):
	a=3
	b=5

	if n%a == 0 and n%b == 0:
		return 'FizzBuzz'

	elif n%a == 0:
		return 'Fizz'

	elif n%b == 0:
		return 'Buzz'

	else:
		return n	
