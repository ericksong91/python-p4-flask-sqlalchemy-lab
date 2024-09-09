from app import app
from server.models import db, Zookeeper

class TestEnclosure:
    '''Zookeeper model in models.py'''

    def test_can_be_instantiated(self):
        '''can be invoked to create a Python object.'''
        a = Zookeeper()
        assert a
        assert isinstance(a, Zookeeper)

    def test_has_name_and_species(self):
        '''can be instantiated with a name and species.'''
        a = Zookeeper(name='Phil', birthday="07/01")
        assert a.name == 'Phil'
        assert a.birthday == "07/01"