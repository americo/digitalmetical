#!/usr/bin/python3

from brownie import Token, accounts
from web3 import Web3

from scripts.helpful_scripts import get_account

initial_supply = Web3.toWei(10000, "ether")


def main():
    account = get_account()
    return Token.deploy("Evil Coin", "EVIL", 18, initial_supply, {"from": account})
