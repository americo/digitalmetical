#!/usr/bin/python3

from brownie import Token, accounts
from web3 import Web3

initial_supply = Web3.toWei(10000, "ether")


def main():
    return Token.deploy("Evil Coin", "EVIL", 18, initial_supply, {"from": accounts[0]})
