class Heap:

	def __init__(self, h=[]):
		self.h = h

	def is_empty(self):
		return self.h == []
#manera recursiva 
	def _float_(self, e): #toma la posicion []
		
		padre = e//2
		while self.h[padre] != 0 or self.h[padre] < self.h[self.e]: #Fuera de rango
			self._swap_(padre, e)
			e = self._float_(e)
	
	def _sync_(self):
		padre = 0 
		while True:
			der = self._righ_index_(padre)
			izq = self._left_index_(padre)
			if self.h[der] > self.h[izq] and self.h[der] < self.h[padre]:
				self._swap_(padre, der)
			elif self.h[izq] > self.h[der] and self.h[izq] < self.h[padre]:
				self._swap_(padre, izq)



	def _swap_(self, i, j):
		temp = self.heap[i]
		self.heap[i] = self.heap[j]
		self.heap[j] = temp
			
		
	def enqueue(self,e):
		self.h.append(e)
		e = self.h[e]#<<<-------quiero guardar el indice de e ---pero parece que no es asi :(
		self._float_(e)# la idea seria que tome la e = [e] (como indice)
		
		
		
		
	def dequeue(self):
		self._swap_(0, -1)
		elem = self.h.pop()
		self._sink_()

#	def _parent_(self, i):
#		self.h[i] = (i//2)

	def _righ_index_(self, i):
		return (2 * i) + 2
	
	def _left_index_(self, i):
		return (2 * i) + 1


	def __str__(self):
		print(self.h)  
		
h=Heap()
print(h.is_empty())

#http://www.maestrosdelweb.com/curso-django-entendiendo-como-trabaja-django/

"""


		padre = /2
		while not self.h[i] == self.h[0] or self.h[i] >= self.h[padre]:
			if self.h[i] < self.h[padre]:
				aux = self.h[i]
				self.h[i] = self.h[padre]
				self.h[i] = aux
			self._float_(padre)

			"""