from app import app
from server.models import db, Enclosure

class TestEnclosure:
    '''Enclosure model in models.py'''

    def test_can_be_instantiated(self):
        '''can be invoked to create a Python object.'''
        a = Enclosure()
        assert a
        assert isinstance(a, Enclosure)

    def test_has_name_and_species(self):
        '''can be instantiated with a name and species.'''
        a = Enclosure(environment='Phil', open_to_vistors=True)
        assert a.environment == 'Phil'
        assert a.open_to_visitors == True