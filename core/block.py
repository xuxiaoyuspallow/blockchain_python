class BlockHeader(object):
    def __init__(self):
        self.Version = 1
        self.hashPrevBlock = ''
        self.hashMerkleRoot = ''
        self.Time = None
        self.Nonce = None


class Block(object):
    def __init__(self):
        self.MagicNo = b'D9B4BEF9'
        self.Transactions = []
        self.Blockheader = BlockHeader()


