# -----------------------------------------------------------------------------
# The MIT License (MIT)
# Copyright (c) 2018 Robbie Coenmans
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------

import unittest
import pkcsutil
import os

class PkcsUtilTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_read_certificate(self):
        # Arrange
        path = 'minica.pem'

        # Act
        cert = pkcsutil.read_certificate(path)

        # Assert
        self.assertIsNotNone(cert)

    def test_read_private_key(self):
        # Arrange
        path = 'minica-key.pem'

        # Act
        key = pkcsutil.read_private_key(path, b'passphrase')

        # Assert
        self.assertIsNotNone(key)

    def test_export_to_pkcs(self):
        # Arrange
        if os.path.isfile('minica.pfx'):
            os.remove('minica.pfx')

        cert = pkcsutil.read_certificate('minica.pem')
        key  = pkcsutil.read_private_key('minica-key.pem', b'passphrase')

        # Act
        pkcsutil.export_to_pkcs12('minica.pfx', key, cert, b'passphrase')

        # Assert
        os.path.isfile('minica.pfx') 

if __name__ == '__main__':
    unittest.main()