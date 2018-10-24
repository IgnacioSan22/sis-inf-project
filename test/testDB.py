import app
from app import app
from app.models import User, Poster, Stat, QuestionOption
import unittest

class TestBD(unittest.TestCase):

    def testInsertUpdateRemoveUser(self):
        # Insert User
        u1 = User(username='testUser5', email='testuser5@gmail.com')
        u1.addUser()
        u2 = User.getUserByUsername('testUser5')
        self.assertTrue(u1.__repr__==u2.__repr__)

        # Update User
        u1 = User.getUserByUsername('testUser5')
        u1.email = 'testusermodified@gmail.com'
        u1.updateUser()
        u2 = User.getUserByUsername('testUser5')
        self.assertTrue(u1.__repr__==u2.__repr__)

        #Remove User
        u1 = User.getUserByUsername('testUser5')
        u1.removeUser()
        u2 = User.getUserByUsername('testUser5')
        self.assertTrue(u2==None)

    def testInsertUpdateRemovePoster(self):
        # Insert Poster
        p1 = Poster(id=65535, id_usuario=1, info='Info Test')
        p1.addPoster()
        p2 = Poster.getPosterById(65535)
        self.assertTrue(p1.__repr__==p2.__repr__)

        # Update Poster
        p1 = Poster.getPosterById(65535)
        p1.info = 'Info modified'
        p1.updatePoster()
        p2 = Poster.getPosterById(65535)
        self.assertTrue(p1.__repr__==p2.__repr__)

        # Remove Poster
        p1 = Poster.getPosterById(65535)
        p1.removePoster()
        p2 = Poster.getPosterById(65535)
        self.assertTrue(p2==None)

if __name__ == '__main__':
    unittest.main()