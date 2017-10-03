from binascii import unhexlify
from io import BytesIO
from unittest import TestCase, skip

from helper import (
    double_sha256,
    int_to_little_endian,
    little_endian_to_int,
)


class Block:

    def __init__(self, version, prev_block, merkle_root, timestamp, bits, nonce):
        self.version = version
        self.prev_block = prev_block
        self.merkle_root = merkle_root
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = nonce

    @classmethod
    def parse(cls, s):
        '''Takes a byte stream and parses a block. Returns a Block object'''
        # version - 4 bytes, little endian
        # prev_block - 32 bytes, little endian
        # merkle_root - 32 bytes, little endian
        # timestamp - 4 bytes, little endian
        # bits - 4 bytes
        # nonce - 4 bytes
        raise NotImplementedError

    def serialize(self):
        '''Returns the 80 byte block header'''
        raise NotImplementedError

    def hash(self):
        '''Returns the double-sha256 interpreted little endian of the block'''
        raise NotImplementedError

    def bip9(self):
        '''Returns whether this block is signaling readiness for BIP9'''
        # BIP9 is signalled if the top 3 bits are 001
        raise NotImplementedError

    def bip91(self):
        '''Returns whether this block is signaling readiness for BIP91'''
        # BIP91 is signalled if the top 5th bit from the right is 1
        raise NotImplementedError
    
    def bip141(self):
        '''Returns whether this block is signaling readiness for BIP141'''
        # BIP91 is signalled if the top 2nd bit from the right is 1
        raise NotImplementedError

    def target(self):
        '''Returns the proof-of-work target based on the bits'''
        # note bits is in little-endian and the first byte is the exponent
        # the other three bytes are the coefficient.
        # the formula is:
        # coefficient * 2**(8*(exponent-3))
        raise NotImplementedError

    def difficulty(self):
        '''Returns the block difficulty based on the bits'''
        # note difficulty is (target of lowest difficulty) / (self's target)
        # lowest difficulty has bits that equal 0xffff001d
        raise NotImplementedError

    def check_pow(self):
        '''Returns whether this block satisfies proof of work'''
        # You will need to get the hash of this block and interpret it
        # as an integer. If the hash of the block is lower, pow is good.
        # hint: int.from_bytes('', 'big')
        raise NotImplementedError


class BlockTest(TestCase):

    @skip('unimplemented')
    def test_parse(self):
        block_raw = unhexlify('020000208ec39428b17323fa0ddec8e887b4a7c53b8c0a0a220cfd0000000000000000005b0750fce0a889502d40508d39576821155e9c9e3f5c3157f961db38fd8b25be1e77a759e93c0118a4ffd71d')
        stream = BytesIO(block_raw)
        block = Block.parse(stream)
        self.assertEqual(block.version, 0x20000002)
        want = unhexlify('000000000000000000fd0c220a0a8c3bc5a7b487e8c8de0dfa2373b12894c38e')
        self.assertEqual(block.prev_block, want)
        want = unhexlify('be258bfd38db61f957315c3f9e9c5e15216857398d50402d5089a8e0fc50075b')
        self.assertEqual(block.merkle_root, want)
        self.assertEqual(block.timestamp, 0x59a7771e)
        self.assertEqual(block.bits, unhexlify('e93c0118'))
        self.assertEqual(block.nonce, unhexlify('a4ffd71d'))

    @skip('unimplemented')
    def test_serialize(self):
        block_raw = unhexlify('020000208ec39428b17323fa0ddec8e887b4a7c53b8c0a0a220cfd0000000000000000005b0750fce0a889502d40508d39576821155e9c9e3f5c3157f961db38fd8b25be1e77a759e93c0118a4ffd71d')
        stream = BytesIO(block_raw)
        block = Block.parse(stream)
        self.assertEqual(block.serialize(), block_raw)

    @skip('unimplemented')
    def test_hash(self):
        block_raw = unhexlify('020000208ec39428b17323fa0ddec8e887b4a7c53b8c0a0a220cfd0000000000000000005b0750fce0a889502d40508d39576821155e9c9e3f5c3157f961db38fd8b25be1e77a759e93c0118a4ffd71d')
        stream = BytesIO(block_raw)
        block = Block.parse(stream)
        self.assertEqual(block.hash(), unhexlify('0000000000000000007e9e4c586439b0cdbe13b1370bdd9435d76a644d047523'))


    @skip('unimplemented')
    def test_bip9(self):
        block_raw = unhexlify('020000208ec39428b17323fa0ddec8e887b4a7c53b8c0a0a220cfd0000000000000000005b0750fce0a889502d40508d39576821155e9c9e3f5c3157f961db38fd8b25be1e77a759e93c0118a4ffd71d')
        stream = BytesIO(block_raw)
        block = Block.parse(stream)
        self.assertTrue(block.bip9())
        block_raw = unhexlify('0400000039fa821848781f027a2e6dfabbf6bda920d9ae61b63400030000000000000000ecae536a304042e3154be0e3e9a8220e5568c3433a9ab49ac4cbb74f8df8e8b0cc2acf569fb9061806652c27')
        stream = BytesIO(block_raw)
        block = Block.parse(stream)
        self.assertFalse(block.bip9())

    @skip('unimplemented')
    def test_bip91(self):
        block_raw = unhexlify('1200002028856ec5bca29cf76980d368b0a163a0bb81fc192951270100000000000000003288f32a2831833c31a25401c52093eb545d28157e200a64b21b3ae8f21c507401877b5935470118144dbfd1')
        stream = BytesIO(block_raw)
        block = Block.parse(stream)
        self.assertTrue(block.bip91())
        block_raw = unhexlify('020000208ec39428b17323fa0ddec8e887b4a7c53b8c0a0a220cfd0000000000000000005b0750fce0a889502d40508d39576821155e9c9e3f5c3157f961db38fd8b25be1e77a759e93c0118a4ffd71d')
        stream = BytesIO(block_raw)
        block = Block.parse(stream)
        self.assertFalse(block.bip91())

    @skip('unimplemented')
    def test_bip141(self):
        block_raw = unhexlify('020000208ec39428b17323fa0ddec8e887b4a7c53b8c0a0a220cfd0000000000000000005b0750fce0a889502d40508d39576821155e9c9e3f5c3157f961db38fd8b25be1e77a759e93c0118a4ffd71d')
        stream = BytesIO(block_raw)
        block = Block.parse(stream)
        self.assertTrue(block.bip141())
        block_raw = unhexlify('0000002066f09203c1cf5ef1531f24ed21b1915ae9abeb691f0d2e0100000000000000003de0976428ce56125351bae62c5b8b8c79d8297c702ea05d60feabb4ed188b59c36fa759e93c0118b74b2618')
        stream = BytesIO(block_raw)
        block = Block.parse(stream)
        self.assertFalse(block.bip141())

    @skip('unimplemented')
    def test_target(self):
        block_raw = unhexlify('020000208ec39428b17323fa0ddec8e887b4a7c53b8c0a0a220cfd0000000000000000005b0750fce0a889502d40508d39576821155e9c9e3f5c3157f961db38fd8b25be1e77a759e93c0118a4ffd71d')
        stream = BytesIO(block_raw)
        block = Block.parse(stream)
        self.assertEqual(block.target(), 0x13ce9000000000000000000000000000000000000000000)
        self.assertEqual(int(block.difficulty()), 888171856257)

    @skip('unimplemented')
    def test_check_pow(self):
        block_raw = unhexlify('04000000fbedbbf0cfdaf278c094f187f2eb987c86a199da22bbb20400000000000000007b7697b29129648fa08b4bcd13c9d5e60abb973a1efac9c8d573c71c807c56c3d6213557faa80518c3737ec1')
        stream = BytesIO(block_raw)
        block = Block.parse(stream)
        self.assertTrue(block.check_pow())
        block_raw = unhexlify('04000000fbedbbf0cfdaf278c094f187f2eb987c86a199da22bbb20400000000000000007b7697b29129648fa08b4bcd13c9d5e60abb973a1efac9c8d573c71c807c56c3d6213557faa80518c3737ec0')
        stream = BytesIO(block_raw)
        block = Block.parse(stream)
        self.assertFalse(block.check_pow())
