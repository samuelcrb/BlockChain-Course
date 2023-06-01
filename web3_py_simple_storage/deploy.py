from solcx import compile_standard, install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

install_solc("0.8.0")

with open("./SimpleStorage.sol","r") as file:
    simple_storage_file = file.read()

    #Compile our solidity

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"] 
#get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

#for connecting to sepolia
w3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/0011db7d16bf448492b272fe355ab932"))
chainId = 11155111
myAddress = "0x31A1d9461a8524CcB7b9B451bB2C910F06778E21"
privateKey = os.getenv("PRIVATE_KEY")


#Create the contract in python

SimpleStorage =  w3.eth.contract(abi=abi, bytecode=bytecode)
#Get the lastest transaction
nonce = w3.eth.get_transaction_count(myAddress)

#1. Build transaction
transaction = SimpleStorage.constructor().build_transaction({"gasPrice": w3.eth.gas_price,"chainId":chainId,"from":myAddress,"nonce":nonce})
#2. Sign transaction
signed_txn = w3.eth.account.sign_transaction(transaction,privateKey)
#3. Send transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

#Working with the contract, you always need
#Contract address
#Contract ABI
simple_storage = w3.eth.contract(address = tx_receipt.contractAddress, abi=abi)

#Initial value of fav number
print(simple_storage.functions.retrieve().call())
store_transaction = simple_storage.functions.store(15).build_transaction({"gasPrice": w3.eth.gas_price,"chainId":chainId,"from":myAddress,"nonce":nonce + 1})
signed_store_tx = w3.eth.account.sign_transaction(store_transaction,privateKey)
send_store_tx = w3.eth.send_raw_transaction(signed_store_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
print(simple_storage.functions.retrieve().call())