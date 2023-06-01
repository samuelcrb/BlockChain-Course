from brownie import accounts, config, SimpleStorage, network
import os

def deploy_simple_storage():
    """ account = accounts[0]
    print(account) """
    """ account = accounts.load("freeCodeCamp")
    print(account) """
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    """ account = accounts.add(config["wallets"]["from_key"])
    print(account) """
    account = getAccount()
    simple_storage = SimpleStorage.deploy({"from":account})
    stored_value = simple_storage.retrieve()
    transaction = simple_storage.store(15,{"from": account})
    transaction.wait(1)
    stored_value = simple_storage.retrieve()
    updated_stored_value = stored_value
    print(updated_stored_value )

def getAccount():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
def main():
    print(deploy_simple_storage())