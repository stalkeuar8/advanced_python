
class DocstingMeta(type):

    def __new__(cls, name, bases, attrs):
        for attr_name, value in attrs.items():
            if callable(value) and value.__doc__ is None:
                raise TypeError(f"Method {attr_name} must have a docstring")
        return super().__new__(cls, name, bases, attrs)
    

class TestClass:
    def test_method():
        """
        Docstring for test_method
        """

        pass

    def __init__(self, name):
        self.name = name

    def __new__(cls, name):
        pass


new = TestClass('aaa')
print(type(new))