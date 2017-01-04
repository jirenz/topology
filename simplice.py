'''
This file defines a class for simplice and operations for it.
'''
import random
import numpy as np
import sys

class Vertex:
	def __init__(self, name):
		self.name = name

	def __eq__(self, other):
		return isinstance(other, self.__class__) and self.name == other.name

class Simplex:
	# verticies is a ordered list
	def __init__(self, verticies):
		self.verticies = verticies
		self.name = ""
		for vertex in verticies:
			self.name += vertex.name + '-'

	def getFaces(self):
		if len(self.verticies) <= 1:
			return []
		faces = []
		for i in range(len(self.verticies)):
			new_face = Simplex(self.name + '-' + str(i)
				, self.verticies[0:i] 
				+ self.verticies[i+1:len(self.verticies)])
			faces.append(new_face)
		return faces

	def getUniqueLabel(self):
		label = ""
		for i in range(len(self.verticies)):
			label += self.verticies[i].name
		return label

	def getDimension(self):
 		return len(self.verticies) - 1

# class ChainSingleton:
# 	def __init__(self, simplex, coefficient = 1):
# 		self.coefficient = coefficient
# 		self.simplex = simplex
		
# 	def __add__(self, ChainSingleton):
# 		pass

# class Chain:
# 	def __init__(self, chains):
# 		self.chains = chains

class SimplicialComplex:
	@staticmethod
	def sanitizeVerticies(verticies):
		for index, vertex in enumerate(verticies):
			if not isinstance(vertex, Vertex):
				verticies[index] = Vertex(str(vertex))


	def __init__(self, verticies, max_dimension = None, name = ""):
		SimplicialComplex.sanitizeVerticies(verticies)
		self.name = name
		self.verticies = verticies
		if max_dimension == None:
			max_dimension = len(verticies)
		self.max_dimension = max_dimension
		self.simplicies = [ {} for i in range(max_dimension)]
		for vertex in self.verticies:
			simplex = Simplex([vertex])
			self.simplicies[0][simplex.name] = simplex

	def addSimplex(self, verticies):
		SimplicialComplex.sanitizeVerticies(verticies)
		if len(verticies) == 0:
			return
		new_simplex = Simplex(verticies)
		cur_dim = new_simplex.getDimension()
		if cur_dim >= self.max_dimension:
			raise Exception('Dimension to large')
		if new_simplex.name in self.simplicies[cur_dim]:
			return
		else:
			self.simplicies[cur_dim][new_simplex.name] = new_simplex
			for i in range(len(verticies)):
				self.addSimplex(verticies[0:i] + verticies[i + 1:])
			return
	
	def getDimension(self):
		return self.max_dimension

	def computeHomology(self):
		pass

	def registerSimplex(self):
		max_dim = self.getDimension
		self.basis = []
		for dim in range(max_dim + 1):
			self.basis[dim] = {}
		for simplex in self.simplicies:
			pass

	def maximize(self):
		pass
		# self.verticies = {}
		# self.name = name
		# for vertex in verticies:
		# 	self.verticies[vertex.name] = vertex

# a = Vertex('ada')
# b = Vertex('b')
# c = Vertex('c')
# tri = Simplex([a,b,c])
# print(tri.name)
# print({'a': ['b'], 'c': ['dd']})
# print(tri.getUniqueLabel())
cplx = SimplicialComplex(['a','b', 'c', 'd', 56], 3)
cplx.addSimplex([Vertex('c'), Vertex('b')])
cplx.addSimplex([Vertex('c'), Vertex('a'), Vertex('b')])
cplx.addSimplex([Vertex('c'), Vertex('a'), Vertex('d')])
print(cplx.simplicies)