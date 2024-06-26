#!/usr/bin/python3

# Classes
# -------

class Text(str):
	
    """
	A Text class to represent a text you could use with your HTML elements.

	Because directly using str class was too mainstream.
	"""

    def __str__(self) -> str:
		
        """
		Do you really need a comment to understand this method? Yes I do.
		Method to return the string representation of the Text object with
		HTML characters replaced by their respective HTML entities :
		- '<' by '&lt;'
		- '>' by '&gt;'
		- '"' by '&quot;'
		- '\n' by '\n<br />\n'.
		
		Parameters: None
		
		Returns:
            - str: The string representation of the Text object.
		"""
		
        new = super().__str__().replace('>', '&gt;').replace('<', '&lt;')
        if new == '"':
            new = new.replace('"', '&quot;')
        return new.replace('\n', '\n<br />\n')


class Elem:

	"""
	Elem will permit us to represent our HTML elements.
	"""

	class ValidationError(Exception):

		"""
		An exception to raise when a type error occurs.
		"""

		def __init__(self, msg="This content is not a Text or a elem.") -> None:
			
			"""
			The __init__() method to initialize the ValidationError object 
			with a message.

			Parameters:
				- msg (str): The message to display.
			
			Returns: None
			"""
			Exception.__init__(self, msg)

	def __init__(self, tag='div', attr=dict(), content=None, tag_type='double') -> None:
		
		"""
		The __init__() method to initialize the Elem object with a tag, attributes,
		content and tag_type.

		Parameters:
			- tag (str): The tag of the element.
			- attr (dict): The attributes of the element.
			- content (str, list): The content of the element.
			- tag_type (str): The type of the tag ('double' or 'simple').
		
		Returns: None
		"""

		self.tag = tag
		self.attr = attr
		self.content = []
		if content:
			self.add_content(content)
		elif content is not None and not isinstance(content, Text):
			raise Elem.ValidationError
		self.tag_type = tag_type

	def __str__(self) -> str:
		
		"""
		The __str__() method to return the HTML representation of our elements.
		
		Parameters: None

		Returns:
			- str: The HTML representation of our elements.
		"""
		
		result = ""
		if self.tag_type == 'double':
			result = "<{0}{1}>{2}</{0}>".format(self.tag, self.__make_attr(), self.__make_content())
		elif self.tag_type == 'simple':
			result = "<{0}{1} />".format(self.tag, self.__make_attr())
		return result

	def __make_attr(self) -> str:
		
		"""
		Method to render the attributes of the element.

		Parameters: None

		Returns:
			- str: The attributes of the element.
		"""
		
		result = ''
		for pair in sorted(self.attr.items()):
			result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
		return result

	def __make_content(self) -> str:
		
		"""
		Method to render the content, including embedded elements.

		Parameters: None

		Returns:
			- str: The content of the element.
		"""

		if len(self.content) == 0:
			return ''
		result = '\n'
		for item in self.content:
			item = str(item).replace('\n', '\n  ')
			result += '  ' + item + '\n'
		return result

	def add_content(self, content) -> None:

		"""
		Method to add content to the element.

		Parameters:
			- content (str, list): The content to add to the element.
		
		Returns: None
		"""

		if not Elem.check_type(content):
			raise Elem.ValidationError
		if type(content) == list:
			self.content += [item for item in content if item != Text('')]
		elif content != Text(''):
			self.content.append(content)

	@staticmethod
	def check_type(content) -> bool:
		
		"""
		
		Static method to check if the content is a Text or an Elem.

		Parameters:
			- content (str, list): The content to check.
		
		Returns:
			- bool: True if the content is a Text or an Elem, False otherwise.
		"""
		
		return (isinstance(content, Elem) or type(content) == Text or
				(type(content) == list and all([type(elem) == Text or
												isinstance(elem, Elem)
												for elem in content])))
