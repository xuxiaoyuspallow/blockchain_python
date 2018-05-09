import hashlib

import base58
import rsa

version = bytearray(0x00)
addressChecksumLen = 4

class Wallet(object):
    def __init__(self):
        self.privateKey = None
        self.publicKey = None

    def hashPublicKey(self):
        if not self.publicKey:
            return
        pubkeysha256 = hashlib.sha256(self.publicKey).hexdigest()
        pubkeyripemd160 = hashlib.new('ripemd160').update(pubkeysha256).hexdigest()
        return pubkeyripemd160

    def checksum(self,payload):
        firstPayload = hashlib.sha256(payload).hexdigest()
        secondPayload = hashlib.sha256(firstPayload).hexdigest()
        return secondPayload[:addressChecksumLen]

    def getAddress(self):
        pubkeyhash = self.hashPublicKey()
        versionPayload = bytearray(version) + bytearray(pubkeyhash)
        checksum = self.checksum(versionPayload)
        fullPayload = versionPayload + bytearray(checksum)
        address = base58.b58encode(fullPayload)
        return address


def createWallet():
    wallet = Wallet()
    wallet.publicKey, wallet.privateKey = rsa.newkeys(256)
    address = wallet.getAddress()
    return address