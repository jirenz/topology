# 0 is preserved value for identity
class AlgebraSingleton:
	def __init__(self, value = 0):
		self.value = value

	def inverse(self):
		# example
		return AlgebraSingleton(0 - self.value)

	def __pow__(self, power):
		# assume (power == int(power))
		return AlgebraExpression([self for i in range(power)])

	def __str__(self):
		return str(self.value)

class AlgebraExpression:
	# Generators
	# Rules
	
	def __init__(self, expression = []): # aba is written as [a, b, a]
		self.expression = expression

	def __add__(self, other):
		return AlgebraExpression(self.expression + other.expression)

	def inverse(self):
		# we assume that all elements in it are singletons so we use slicing to copy
		copied_expression = self.expression[:]
		copied_expression.reverse()
		for singleton in copied_expression:
			singleton = singleton.inverse()
		return AlgebraExpression(copied_expression)

	def __str__(self):
		ans = ""
		for singleton in self.expression:
			ans += str(singleton)
		return ans

a = AlgebraSingleton(2)
b = AlgebraSingleton(3)
print((pow(a, 5)+ pow(b,2)).inverse())