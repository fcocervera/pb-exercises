### Problems

1. What is the double-sha256 hash of this block? Notice anything?

020000208ec39428b17323fa0ddec8e887b4a7c53b8c0a0a220cfd0000000000000000005b0750fce0a889502d40508d39576821155e9c9e3f5c3157f961db38fd8b25be1e77a759e93c0118a4ffd71d

### Make these tests pass

in block.py:

    def test_parse(self):

    def test_serialize(self):

    def test_hash(self):
   