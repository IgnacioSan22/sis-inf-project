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
        self.assertTrue(print(u1)==print(u2))

        # Update User
        u1 = User.getUserByUsername('testUser5')
        u1.email = 'testusermodified@gmail.com'
        u1.updateUser()
        u2 = User.getUserByUsername('testUser5')
        self.assertTrue(print(u1)==print(u2))

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
        self.assertTrue(print(p1)==print(p2))

        # Update Poster
        p1 = Poster.getPosterById(65535)
        p1.info = 'Info modified'
        p1.updatePoster()
        p2 = Poster.getPosterById(65535)
        self.assertTrue(print(p1)==print(p2))

        # Remove Poster
        p1 = Poster.getPosterById(65535)
        p1.removePoster()
        p2 = Poster.getPosterById(65535)
        self.assertTrue(p2==None)

    def testInsertUpdateRemoveStat(self):
        # Insert Stat
        s1 = Stat(id=65535, id_usuario=1, dato_estadistico_1='Dato 1 Test', dato_estadistico_2='Dato 2 Test')
        s1.addStat()
        s2 = Stat.getStatById(65535)
        self.assertTrue(print(s1)==print(s2))

        # Update Stat
        s1 = Stat.getStatById(65535)
        s1.dato_estadistico_1 = 'Dato 1 modified'
        s1.updateStat()
        s2 = Stat.getStatById(65535)
        self.assertTrue(print(s1)==print(s2))

        # Remove Stat
        s1 = Stat.getStatById(65535)
        s1.removeStat()
        s2 = Stat.getStatById(65535)
        self.assertTrue(s2==None)

if __name__ == '__main__':
    unittest.main()