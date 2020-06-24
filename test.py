import parse_dat_url as pdu
import testdata
import unittest

class TestUrlParser(unittest.TestCase):
    def test_urls(self):
        res = list(map(pdu.parse_dat_url,testdata.INPUT ) )
        for i in range(0,len(res)):
            self.assertDictEqual(res[i],testdata.OUTPUT[i])
if __name__ == '__main__':
    unittest.main()