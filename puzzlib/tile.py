class Tile(object):
	'''
		A data class representing tile object
	'''

	DEFAULT_VALUE = 0
	
	# CONSTRUCTORS
	def __init__( self, init_val = DEFAULT_VALUE):
		self.__value = init_val

	# PUBLIC METHODS
	def get_value( self):
		return self.__value

	def set_value( self, value):
		self.__value = value