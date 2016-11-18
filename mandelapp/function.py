from pylab import *

def show_mandel(w, h, it):
	iterations = it
	density = 1000
	x_min, x_max = -2, w
	y_min, y_max = -1*y/2, y/2
	x, y = meshgrid(linspace(x_min, x_max, density), linspace(y_min, y_max, density))
	c = x + 1j*y
	z = c.copy()
	m = zeros((density, density))
	for n in range(iterations):
		print("Completed %d %%" % (100 * float(n)/iterations))
		indices = (abs(z) <= 10)
		z[indices] = z[indices]**2 + c[indices]
		m[indices] = n
	imshow(log(m), cmap=cm.hot, extent=(x_min, x_max, y_min, y_max))
	imshow.savefig("brot.png")
	title('Mandelbrot Set')
	xlabel('Re(z)')
	ylabel('Im(z)')
	show()
