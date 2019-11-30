#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import Eth Account Package
from eth_account import Account

# Import Deterministic Ganache Account Information (Address, Private Key)
from core.constants.console_constant import DETERMINISTIC_ACCOUNT_INFORMATION as ganache_data

# Import HexBytes Package
from hexbytes import HexBytes
from enum import Enum

STRING_DASHES = '---------' * 10


class TypeOfAccount(Enum):
    LOCAL_ACCOUNT = 'LocalAccount'
    RINKEBY_ACCOUNT = 'RinkebyAccount'
    MAINNET_ACCOUNT = 'MainnetAccount'
    ROPSTEN_ACCOUNT = 'RopstenAccount'


class ConsoleAccounts:
    """ ConsoleSessionAccounts

    """
    def __init__(self, logger, ethereum_client, silence_flag=False):
        self.logger = logger
        self.ethereum_client = ethereum_client
        self.silence_flag = silence_flag
        # convert to ether
        self.account_data = {
            'NULL': {
                'network': TypeOfAccount.LOCAL_ACCOUNT,
                'balance': 0,
                'address': '0x' + '0' * 40,
                'private_key': HexBytes(''),
                'instance': None
            }
        }

        self._setup_ganache_accounts()
        self._setup_random_accounts()
        # todo: web3.eth.getBalance(address)

    def command_view_accounts(self):
        self.logger.debug0(STRING_DASHES)
        for item in self.account_data:
            self.logger.info(' | {0:^15} | {1:^25} | {2:^25} | {3:^50} | '.format(
                item, self.account_data[item]['network'], self.account_data[item]['balance'],
                self.account_data[item]['address'])
            )
        self.logger.debug0(STRING_DASHES)

    def new_account_entry(self, network, local_account):
        return {
                'network': network, 'balance': self.ethereum_client.w3.eth.getBalance(local_account.address),
                'address': local_account.address, 'private_key': local_account.privateKey,
                'instance': local_account
        }

    def add_account(self, address, private_key='', alias='uAccount', network=TypeOfAccount.LOCAL_ACCOUNT):
        """ Add Account

        This function will add a new account to the ConsoleAccountArtifacts
            :param address:
            :param private_key:
            :param alias:
            :return:
        """
        local_account = None
        if private_key != '':
            try:
                local_account = Account.privateKeyToAccount(private_key)
                self.account_data[(alias + str(len(self.account_data)-1))] = self.new_account_entry(network, local_account)
                return self.account_data
            except Exception as err:
                self.logger.error('Unable to add_account() {0} {1}'.format(type(err), err))
        else:
            try:
                local_account = Account.privateKeyToAccount(private_key)
                if local_account.address != address:
                    self.logger.error('Miss Match in generated address via private_key and provided address')
                    raise Exception
            except Exception as err:
                self.logger.error('Unable to add_account() {0} {1}'.format(type(err), err))
            self.account_data[(alias + str(len(self.account_data)-1))] = self.new_account_entry(network, local_account)
            return self.account_data

    def _setup_random_accounts(self, account_number=10):
        """ Setup Random Accounts
        This function will setup n number of random accounts to interact with during the console execution
        :param account_number:
        :return:
        """
        self.logger.info(STRING_DASHES)
        for index in range(1, account_number, 1):
            tmp_account = Account.create()
            self.add_account(tmp_account.address, tmp_account.privateKey, alias='rAccount')

        if not self.silence_flag:
            self.logger.info('Setup Random Accounts')
            self.logger.info('(+) Added {0} Random Accounts'.format(account_number))

    def _setup_ganache_accounts(self):
        """ Setup Ganache Accounts
        This function will retrieve and setup ten ganache accounts to interact with during the console execution
        :return:
        """
        for index, data in enumerate(ganache_data):
            tmp_account = Account.privateKeyToAccount(ganache_data[data]['private_key'])
            self.add_account(tmp_account.address, tmp_account.privateKey, alias='gAccount')

        if not self.silence_flag:
            self.logger.info('Setup Ganache Accounts')
            self.logger.info('(+) Added {0} Ganache Accounts'.format(len(ganache_data)))

    def get_account_data(self, stream):
        """ Get Account Data
        This function will retrieve the data from a given value
        :param stream:
        :return:
        """
        for item in self.account_data:
            if stream.startswith(item):
                key = stream.split('.')[1]
                print(stream, item, self.account_data[item][key])
                return self.account_data[item][key]