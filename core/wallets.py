import os
import json

WalletsFile = 'wallets.dat'  # 保存所有钱包地址的文件


def getExistWallets():
    if not os.path.isfile(WalletsFile):
        with open(WalletsFile,'w') as f:
            f.write(json.dumps({}))
    with open(WalletsFile,'r') as f:
        content = f.read()
        return json.loads(content)


def saveNewWallet(wallets):
    with open(WalletsFile,'w') as f:
        f.write(json.dumps(wallets))