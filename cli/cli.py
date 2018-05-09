from core.wallets import getExistWallets
from core.wallet import createWallet


SupportCommands = ['createblockchain','createwallet', 'getbalance', 'listaddresses','printchain','send']


def createWalletCli():
    wallets = getExistWallets()
    address = createWallet()
    wallets

class CLI(object):
    def __init__(self,args):
        self.args = args
        self.run()

    def printHelp(self):
        print("""
    Usage:
	  createblockchain -address ADDRESS - Create a blockchain and send genesis block reward to ADDRESS)
	  createwallet - Generates a new key-pair and saves it into the wallet file)
	  getbalance -address ADDRESS - Get balance of ADDRESS)
	  listaddresses - Lists all addresses from the wallet file)
	  printchain - Print all the blocks of the blockchain)
	  send -from FROM -to TO -amount AMOUNT -mine - Send AMOUNT of coins from FROM address to TO. Mine on the same node, when -mine is set.)
        """)

    def run(self):
        if self.args <= 1 or self.args[1] not in SupportCommands:
            self.printHelp()
            exit(1)
        if self.args[1] == 'createwallet': #创建一个新的钱包地址
            createWalletCli()
        elif self.args[1] == 'createblockchain':
            pass
