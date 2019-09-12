import turtle


def main():
	depth = input("How many layers of depth do you want?")
	turtle.left(90)
	make_triangle(300, depth)
	turtle.done()
	

def make_triangle(size, layers):
	"""
		param: size
		param: layers
		
		precondition: pen is down
		precondition: turtle is facing up
	"""
	
	
	if layers < 1:
		return 0
	else:
		layers = layers - 1
		turtle.left(30)
		turtle.forward(size)
		turtle.right(120)
		turtle.forward(size)
		turtle.right(120)
		turtle.forward(size)
		turtle.right(150)
		make_triangle(size // 2, layers)
main()
