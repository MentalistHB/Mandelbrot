from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from pylab import *

def home(request):
	return render(request, 'mandelapp/index.html')

def show(request):
	w = int(request.GET.get('w', ''))
	h = int(request.GET.get('h', ''))
	it = int(request.GET.get('it', ''))
	path = show_mandel(w, h, it)
	return render(request, 'mandelapp/index.html', {'outputcode':1 })
	
def show_mandel(w, h, it):
	path = "brot.png"
	iterations = it
	density = 1000
	x_min, x_max = -2, 1
	y_min, y_max = -1.5, 1.5
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
	savefig("/home/herval/Documents/THB/Master/Semester1/SI/mandelbrot/Django-1.8.15/mandelbrot/assets/"+path)
	title('Mandelbrot Set')
	xlabel('Re(z)')
	ylabel('Im(z)')
	return path
