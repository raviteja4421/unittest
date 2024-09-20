def logincheck(uname,pwd):
    if(uname=='admin' and pwd=='admin123'):
        return 'login sucess'
    if (uname!='admin' and pwd=='admin123'):
        return 'wrong uname'
    if (uname=='admin' and pwd!='admin123'):
        return 'wrong pwd'
    if (uname!='admin' and pwd!='admin123'):
        return 'login fail'

    
import unittest
class loginclass(unittest.TestCase):
    def test1(self):
        result = logincheck('admin','admin123')
        self.assertEqual(result,'login sucess')
        
    def test2(self):
        result = logincheck('admi','admin123')
        self.assertEqual(result,'wrong uname')

    def test3(self):
        result = logincheck('admin','admin1234')
        self.assertEqual(result,'wrong pwd')

    def test4(self):
        result = logincheck('admin1','admin12345')
        self.assertEqual(result,'login fail')

if __name__ == '__main__':
    unittest.main()
