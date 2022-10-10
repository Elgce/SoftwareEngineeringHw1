import os
import sys
import unittest

from app.checkers.user import register_params_check

sys.path.append(os.path.join(os.getcwd(), ".."))


class BasicTestCase(unittest.TestCase):
    '''
    TODO: 在这里补充注册相关测试用例
    '''

    def setUp(self):
        # check when everything is OK
        self.case1_1 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.com",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        # check when some data is empty
        self.case2_1 = {
            "password": "Bqw1234_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.com",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        self.case2_2 = {
            "username": "bqw123",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.com",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        self.case2_3 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "url": "http://bqw.123.d-43.com",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        self.case2_4 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "nickname": "elgce",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        self.case2_5 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.com",
            "magic_number": 2,
        }
        self.case2_6 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.com",
            "mobile": "+86.123456789012",
        }
        # check if something wrong with username
        self.case3_1 = {
            "username": "b21qw123",
            "password": "Bqw1234*-^_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.com",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        # wrong length
        self.case3_2 = {
            "username": "bqw12312321123123",
            "password": "Bqw1234_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.com",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        # check if something wrong with password
        # no Upper letter
        self.case4_1 = {
            "username": "bqw123",
            "password": "bqw1234*-^_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.com",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        # no lower letter
        self.case4_2 = {
            "username": "bqw123",
            "password": "BQW1234*-^_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.com",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        # no digit
        self.case4_3 = {
            "username": "bqw123",
            "password": "bqw_dsffB",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.com",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        # no label
        self.case4_4 = {
            "username": "bqw123",
            "password": "bqw312dsffB",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.com",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        # wrong length
        self.case4_5 = {
            "username": "bqw123",
            "password": "bqw_B213***1239djfdklsj232",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.com",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        # check if nickname is empty
        self.case5_1 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "nickname": "",
            "url": "http://bqw.123.d-43.com",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        # check if something wrong with url
        # only digit last
        self.case6_1 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.124",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        # - for latter
        self.case6_2 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.124-",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        # too long
        self.case6_3 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.124.dfhkhdjhjkdsfhgkjdsfhgjksdfhgjkdfshsgdfhgds.com",
            "mobile": "+86.123456789012",
            "magic_number": 2,
        }
        # check if something wrong with mobile
        # wrong length for zone
        self.case7_1 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.124.com",
            "mobile": "+826.123456789012",
            "magic_number": 2,
        }
        # wrong length for phone
        self.case7_2 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.124.com",
            "mobile": "+86.1234567890212",
            "magic_number": 2,
        }
        # wrong symbols
        self.case7_3 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.124.com",
            "mobile": "826+123456789012",
            "magic_number": 2,
        }
        # check if something wrong with magic_number

        # not an int
        self.case8_1 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.124.com",
            "mobile": "+86.123456789012",
            "magic_number": "12",
        }
        # not bigger or equal to 0
        self.case8_2 = {
            "username": "bqw123",
            "password": "Bqw1234_",
            "nickname": "elgce",
            "url": "http://bqw.123.d-43.124.com",
            "mobile": "+86.123456789012",
            "magic_number": -1,
        }

    def test_register_params_check(self):
        # check when everything is OK
        self.assertEqual(register_params_check(self.case1_1), ("ok", True))

        # check when some data is empty
        # username empty
        self.assertEqual(
            register_params_check(
                self.case2_1), ("username", False))
        # password empty
        self.assertEqual(
            register_params_check(
                self.case2_2), ("password", False))
        # nickname empty
        self.assertEqual(
            register_params_check(
                self.case2_3), ("nickname", False))
        # url empty
        self.assertEqual(register_params_check(self.case2_4), ("url", False))
        # mobile empty
        self.assertEqual(
            register_params_check(
                self.case2_5), ("mobile", False))
        # magic_number empty
        self.assertEqual(register_params_check(self.case2_6), ("ok", True))

        # check if something wrong with username
        # wrong style
        self.assertEqual(
            register_params_check(
                self.case3_1), ("username", False))
        # wrong length
        self.assertEqual(
            register_params_check(
                self.case3_2), ("username", False))

        # check if something wrong with password
        # no upper letter
        self.assertEqual(
            register_params_check(
                self.case4_1), ("password", False))
        # no lower letter
        self.assertEqual(
            register_params_check(
                self.case4_2), ("password", False))
        # no digit
        self.assertEqual(
            register_params_check(
                self.case4_3), ("password", False))
        # no label
        self.assertEqual(
            register_params_check(
                self.case4_4), ("password", False))
        # wrong length
        self.assertEqual(
            register_params_check(
                self.case4_5), ("password", False))

        # check if nickname is empty
        self.assertEqual(
            register_params_check(
                self.case5_1), ("nickname", False))

        # check if something wrong with url
        # only digit last
        self.assertEqual(register_params_check(self.case6_1), ("url", False))
        # - for latter
        self.assertEqual(register_params_check(self.case6_2), ("url", False))
        # too long
        self.assertEqual(register_params_check(self.case6_3), ("url", False))

        # check if something wrong with mobile
        # wrong length for zone
        self.assertEqual(
            register_params_check(
                self.case7_1), ("mobile", False))
        # wrong length for phone
        self.assertEqual(
            register_params_check(
                self.case7_2), ("mobile", False))
        # wrong symbols
        self.assertEqual(
            register_params_check(
                self.case7_3), ("mobile", False))

        # check if something wrong with magic_number
        # not an int
        self.assertEqual(
            register_params_check(
                self.case8_1), ("magic_number", False))
        # not bigger or equal to 0
        self.assertEqual(
            register_params_check(
                self.case8_2), ("magic_number", False))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
