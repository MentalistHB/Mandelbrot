from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from pylab import *
import matplotlib
#matplotlib.use('Agg')

import datetime
import boto
import boto.s3.connection



#for bucket in conn.get_all_buckets():
#        print("{name}\t{created}".format(
#                name = bucket.name,
#                created = bucket.creation_date,
#        ))

#for bucket in conn.get_all_buckets():
#        print("{name}\t{created}".format(
#                name = bucket.name,
#                created = bucket.creation_date,
#        ))


def home(request):
	return render(request, 'mandelapp/index.html')

def bucketableeren(request):
	access_key = 'AKIAIRBBN7ZV7UPV7F6A'
	secret_key = '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'
	conn = boto.connect_s3(
	        aws_access_key_id = access_key,
	        aws_secret_access_key = secret_key,
	        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
	)
	bucket = conn.get_bucket('mandelbrots3')
	for key in bucket.list():	
		print("Deleting file: {}".format(key.name))
		bucket.delete_key(key.name)
	return render(request, 'mandelapp/index.html', {'outputcode':-1})

def show(request):
	w = int(request.GET.get('w', ''))
	h = int(request.GET.get('h', ''))
	it = int(request.GET.get('it', ''))
	access_key = 'AKIAIRBBN7ZV7UPV7F6A'
	secret_key = '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'
	conn = boto.connect_s3(
	        aws_access_key_id = access_key,
	        aws_secret_access_key = secret_key,
	        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
	)
	bucket = conn.create_bucket('mandelbrots3')
	path = show_mandel(w, h, it, bucket)
	return render(request, 'mandelapp/index.html', {'outputcode':1, 'path': path, 'brots': get_all_brot(bucket)})

def get_all_brot(bucket):
	return bucket.list()

def show_mandel(w, h, it, bucket):
	path = "mandelbrot.png"
	now = datetime.datetime.now()
	
	key = bucket.new_key('mandelbrot_{}-{}-{}_{}-{}-{}.png'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))
	iterations = it
	density = 1000
	x_min, x_max = -2, 1
	y_min, y_max = -1.5, 1.5
	x, y = meshgrid(linspace(x_min, x_max, density), linspace(y_min, y_max, density))
	c = x + 1j*y
	z = c.copy()
	m = zeros((density, density))
	for n in range(iterations):
		indices = (abs(z) <= 10)
		z[indices] = z[indices]**2 + c[indices]
		m[indices] = n
	imshow(log(m), cmap=cm.hot, extent=(x_min, x_max, y_min, y_max))
	path_save = "/home/ubuntu/Django-1.8.15/django/bin/Mandelbrot/assets/"+path
	savefig(path_save)
	title('Mandelbrot Set')
	xlabel('Re(z)')
	ylabel('Im(z)')
	key.set_contents_from_filename(path_save)
	key.set_canned_acl('public-read')
	url = key.generate_url(expires_in=10, query_auth=False, force_http=True)
	return url
