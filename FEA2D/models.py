from django.db import models
import time, random

START_TIME = int(time.time()*1000)

def gen_id():
	'''
	Generate unique primary key
	'''

	t = int(time.time()*1000) - START_TIME
	u = random.SystemRandom().getrandbits(23)
	id = (t << 23 ) | u

	return id

class InputStructure(models.Model):
	'''
	Input structure
	'''
	
	id = models.BigIntegerField(default = gen_id, primary_key=True)  
	created = models.DateTimeField(auto_now_add=True)
	ip_address = models.CharField(max_length=50)
	outer_diameter = models.DecimalField(max_digits=10, decimal_places=2)
	inner_diameter = models.DecimalField(max_digits=10, decimal_places=2)
	modulus_elasticity = models.DecimalField(max_digits=10, decimal_places=2)
	yield_strength = models.DecimalField(max_digits=10, decimal_places=2)
	connectivity_table = models.TextField()
	nodal_coordinates = models.TextField()
	boundary_conditions = models.TextField()
	frame_or_truss = models.CharField(max_length=5)
	
	class Meta:
		ordering = ('created',)
		
class OutputStructure(models.Model):
	'''
	Output structure
	'''
	
	id = models.BigIntegerField(default = gen_id, primary_key=True)  
	created = models.DateTimeField(auto_now_add=True)
	nodal_coordinates = models.TextField()
	factor_of_safety = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		ordering = ('created',)
		
# class InputOutputLink(models.Model):
	# '''
	# Link between InputStructure and OutputStructure
	# '''
	
	# id = models.BigIntegerField(default = gen_id, primary_key=True)  
	# created = models.DateTimeField(auto_now_add=True)
	# input_id = models.BigIntegerField()
	# output_id = models.BigIntegerField()

	# class Meta:
		# ordering = ('created',)
		