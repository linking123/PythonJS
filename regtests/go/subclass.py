'''
simple class
'''
class A:
	{
		x:int,
		y:int,
		z:int,
	}
	def __init__(self, x:int, y:int, z:int=1):
		self.x = x
		self.y = y
		self.z = z

	def mymethod(self, m:int) -> int:
		return self.x * m

class B(A):
	{
		w:string
	}

	def method2(self, v:string) ->string:
		self.w = v
		return self.w

def call_method( cb:func(int)(int), mx:int ) ->int:
	return cb(mx)

def main():
	a = A( 100, 200, z=9999 )
	print( a.x )
	print( a.y )
	print( a.z )

	b = a.mymethod(3)
	print( b )

	c = call_method( a.mymethod, 4 )
	print( c )

	x = B(1,2,z=3)
	print( x.method2('hello world') )