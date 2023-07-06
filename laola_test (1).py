import unittest

from laola import (
    convert,
)

class LaolaTest(unittest.TestCase):
    def test_hello(self):
         self.assertEqual(convert("hello"), ['Hello','hEllo','heLlo','helLo','hellO'])

    def test_empty(self):
        self.assertEqual(convert(" "), [" "])

    def test_helloSpace(self):
        self.assertEqual(convert("hello, world"), [  'Hello, world',
                                                     'hEllo, world',
                                                     'heLlo, world',
                                                     'helLo, world',
                                                     'hellO, world',
                                                     'hello, world',
                                                     'hello, world',
                                                     'hello, World',
                                                     'hello, wOrld',
                                                     'hello, woRld',
                                                     'hello, worLd',
                                                     'hello, worlD'])
    def test_unicode(self):
        self.assertEqual(convert("héllø"), ['Héllø', 'hÉllø', 'héLlø', 'hélLø', 'héllØ'])
