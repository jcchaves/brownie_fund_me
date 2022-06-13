from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    print(f"The current decimals are {fund_me.getDecimals()}")
    print(f"The current price is {fund_me.getPrice()}")
    entrance_fee = fund_me.getEntranceFee()
    print(f"Current entrance fee is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
