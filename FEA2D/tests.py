from django.test import TestCase

from .models import InputStructure, OutputStructure
from .serializers import InputStructureSerializer, OutputStructureSerializer
from .views import FEA2D_input, FEA2D_output

from rest_framework.test import APIRequestFactory

from .fea import node, element

import numpy as np
	
class InputStructureModelTests(TestCase):

	def test_object_creation_with_normal_values(self):
		'''
		Check that InputStructure objects are created and saved properly
		'''
		struc = InputStructure(ip_address='999.999.999.999', 
								outer_diameter=99.99,
								inner_diameter=99.99,
								modulus_elasticity=99.99,
								yield_strength=99.99,
								connectivity_table='testct',
								nodal_coordinates='testnc',
								boundary_conditions='testbc',
								frame_or_truss='tesft')
		
		self.assertEqual(struc.ip_address, '999.999.999.999')
		self.assertEqual(struc.outer_diameter, 99.99)
		self.assertEqual(struc.inner_diameter, 99.99)
		self.assertEqual(struc.modulus_elasticity, 99.99)
		self.assertEqual(struc.yield_strength, 99.99)
		self.assertEqual(struc.connectivity_table, 'testct')
		self.assertEqual(struc.nodal_coordinates, 'testnc')
		self.assertEqual(struc.boundary_conditions, 'testbc')
		self.assertEqual(struc.frame_or_truss, 'tesft')
	
	def test_object_save(self):
		'''
		Check InputStructure are saved properly
		'''
		struc = InputStructure(ip_address='999.999.999.999', 
								outer_diameter=99.99,
								inner_diameter=99.99,
								modulus_elasticity=99.99,
								yield_strength=99.99,
								connectivity_table='testct',
								nodal_coordinates='testnc',
								boundary_conditions='testbc',
								frame_or_truss='tesft')
		struc.save()
		
		self.assertEqual(InputStructure.objects.order_by('created')[0].nodal_coordinates, 'testnc')
	
class OutputStructureModelTests(TestCase):

	def test_object_creation_with_normal_values(self):
		'''
		Check that OutputStructure objects are created properly
		'''
		struc = OutputStructure(nodal_coordinates='test123', factor_of_safety=99.99)
		
		self.assertEqual(struc.nodal_coordinates, 'test123')
		self.assertEqual(struc.factor_of_safety, 99.99)
	
	def test_object_save(self):
		'''
		Check OutputStructure are saved properly
		'''
		struc = OutputStructure(nodal_coordinates='test123', factor_of_safety=99.99)
		struc.save()
		
		self.assertEqual(OutputStructure.objects.order_by('created')[0].nodal_coordinates, 'test123')
		
class InputStructureSerializerTests(TestCase):
	def test_serializer_with_normal_data(self):
		'''
		Check serializer output with normal data
		'''
		struc = InputStructure(ip_address='999.999.999.999', 
								outer_diameter=99.99,
								inner_diameter=99.99,
								modulus_elasticity=99.99,
								yield_strength=99.99,
								connectivity_table='testct',
								nodal_coordinates='testnc',
								boundary_conditions='testbc',
								frame_or_truss='tesft')
		
		serializer = InputStructureSerializer(struc)
		
		self.assertEqual(serializer.data, {'ip_address': '999.999.999.999', 'outer_diameter': '99.99', 'inner_diameter': '99.99', 'modulus_elasticity': '99.99', 'yield_strength': '99.99', 'connectivity_table': 'testct', 'nodal_coordinates': 'testnc', 'boundary_conditions': 'testbc', 'frame_or_truss': 'tesft'})
	
class OutputStructureSerializerTests(TestCase):		
	def test_serializer_with_normal_data(self):
		'''
		Check serializer output with normal data
		'''
		struc = OutputStructure(nodal_coordinates='test123', factor_of_safety=99.99)
		
		serializer = OutputStructureSerializer(struc)
		
		self.assertEqual(serializer.data, {'nodal_coordinates': 'test123', 'factor_of_safety': '99.99'})
			
class FEA2DInputViewTests(TestCase):		
	def test_Json_input_object(self):
		'''
		Check for a valid status given valid data
		'''
		
		factory = APIRequestFactory()
		
		data = {
			"ip_address":"999.999.999.999", 
			"outer_diameter":"99.99",
			"inner_diameter":"99.99",
			"modulus_elasticity":"99.99",
			"yield_strength":"99.99",
			"connectivity_table":"testct",
			"nodal_coordinates":"testnc",
			"boundary_conditions":"testbc",
			"frame_or_truss":"tesft"
		}
		request = factory.post('input/',data, format='json')
		view = FEA2D_input
		response = view(request)
		
		self.assertEqual(response.status_code, 201)
		
class FEA2DOutputViewTests(TestCase):				
	def test_json_output_object(self):
		'''
		Check for a valid status given valid key
		'''
		struc = OutputStructure(nodal_coordinates='test123', factor_of_safety=99.99)
		struc.save()
		id = OutputStructure.objects.all()[0].id
		
		url = 'output/' + str(id)
		
		factory = APIRequestFactory()
		request = factory.get(url)
		view = FEA2D_output
		response = view(request, id)
		
		self.assertEqual(response.status_code, 200)
		
class FEA2DNodeTests(TestCase):
	def test_fea_node_creation(self):
		'''
		Check for node creation
		'''
		test_node = node(1,2,3)
		
		self.assertEqual(test_node.id, 1)
		self.assertEqual(test_node.x, 2)
		self.assertEqual(test_node.y, 3)
		
class FEA2DElementTests(TestCase):
	def test_fea_element_creation(self):
		'''
		Check for element creation
		'''
		nodei = node(1,2,3)
		nodej = node(2,4,6)
		test_element = element(nodei, nodej, 99.99, 99.99, 99.99, 99.99, 'frame')
		
		self.assertEqual(test_element.nodei, nodei)
		self.assertEqual(test_element.nodej, nodej)
		self.assertEqual(test_element.E, 99.99)
		self.assertEqual(test_element.ID, 99.99)
		self.assertEqual(test_element.OD, 99.99)
		self.assertEqual(test_element.Sy, 99.99)
		self.assertEqual(test_element.frame_or_truss, 'frame')
		
	def test_fea_element_calc_properties_normal_values(self):
		'''
		Test the calc_properties function with normal values
		'''
		nodei = node(1,0,0)
		nodej = node(2,0,1)
		test_element = element(nodei, nodej, 1, 10, 20, 100, 'frame')
		test_element.calc_properties()
		
		self.assertEqual(test_element.L, 1)
		self.assertEqual(test_element.Cx, 0)
		self.assertEqual(test_element.Cy, 1)
		self.assertEqual(test_element.I, (20**4 - 10**4) * np.pi / 64)
		self.assertEqual(test_element.A, (20**2 - 10**2) * np.pi / 4)
		self.assertEqual(test_element.frame_or_truss, 'frame')
		
	def test_fea_element_calc_stiffness_frame(self):
		'''
		Test the calculation of the stiffness matrix for a frame
		'''
		nodei = node(1, 0, 0)
		nodej = node(2, 0, 10)
		test_element = element(nodei, nodej, 10, 10, 20, 100, 'frame')
		test_element.E = 10
		test_element.I = 10
		test_element.A = 1
		test_element.L = 10
		test_element.Cx = 0
		test_element.Cy = 1
		test_element.calc_stiffness()
		
		equal = (test_element.K == np.matrix([[1.2, 0., 6., -1.2, 0., 6.],
											  [0., 1., 0., 0., -1., 0.],
											  [6., 0., 40., -6., 0., 20.],
											  [-1.2, 0., -6., 1.2, 0., -6.],
											  [0., -1., 0., 0., 1., 0.],
											  [6.0, 0., 20., -6., 0., 40.]])).all()

		self.assertEqual(equal, True)
		
	def test_fea_element_calc_stiffness_truss(self):
		'''
		Test the calculation of the stiffness matrix for a frame
		'''
		nodei = node(1, 0, 0)
		nodej = node(2, 4, 3)
		test_element = element(nodei, nodej, 10, 10, 20, 100, 'truss')
		test_element.E = 10
		test_element.I = 10
		test_element.A = 1
		test_element.L = 5
		test_element.Cx = 4/5
		test_element.Cy = 3/5
		test_element.calc_stiffness()
		
		equal = (test_element.K.round(2) == np.matrix([[1.28, 0.96, -1.28, -0.96],
													   [0.96, 0.72, -0.96, -0.72],
													   [-1.28, -0.96, 1.28, 0.96],
													   [-0.96, -0.72, 0.96, 0.72]])).all()
										  
		self.assertEqual(equal, True)

# class FEA2DFrameTests(TestCase):