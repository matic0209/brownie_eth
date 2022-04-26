# NOTE: The following tests begin by transferring assets to the deployed flashloan
# contract. this ensures that the tests pass with the base Flashloan implementation,
# i.e. one that does not implement any custom logic.

# The initial transfer should be removed prior to testing your final implementation.
import pytest
from brownie import *

from scripts.helpful_scripts import get_account, get_contract
from conftest import *
from brownie import (
    Wei,
    address,
    accounts,
    Contract,
    config,
    network,
    interface,




)
def log(text, desc=''):
    print('\033[32m' + text + '\033[0m' + desc)

def test_can_get_latest_price(strategy):
    """
    Test that the strategy can get the latest price.
    """

    # get the latest price
    variabledebttoken = get_contract('variabledebttoken')

    variabledebttoken.approveDelegation(
            strategy.address,
            Wei("3 ether"),
            {'from': accounts[0]}
        )
    tokens = []
    tokens.append("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
    funds = Wei("1 ether")
    flashLoanFunds = (funds * 230) / 100;
    amounts = []
    amounts.append(flashLoanFunds)

    strategy.go(
            tokens,
            amounts,
            {'from': accounts[0],"value": Wei("1 ether")}
        )


    aave = get_contract('aaveAddress')
    (totalCollateralETH,totalDebtETH,availableBorrowsETH,currentLiquidationThreshold,ltv,healthFactor)= aave.getUserAccountData(accounts[0])
    assert ltv == 7000
