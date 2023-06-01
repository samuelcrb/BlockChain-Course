from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage
    print(len(simple_storage))

def main():
    read_contract()

    #0x2b10CF1EfB24a7a0648376147446276060bdC52d