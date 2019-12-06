#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.constants.console_constant import STRING_DASHES
from hexbytes import HexBytes

class LogMessageFormatter:
    """ Logging Message Formatter

    """
    def __init__(self, logger):
        self.name = self.__class__.__name__
        self.logger = logger

    def log_error_footer(self, msg='Error.'):
        message = self.header_block(msg, '-')
        self.logger.error(message)

    def log_header(self, msg='Success.'):
        message = self.header_block(msg, '-')
        self.logger.info(message)

    def log_banner_header(self, msg='Head Banner'):
        message = self.header_block(msg, '=')
        self.logger.info(' ' + message)

    def log_entry_message(self, msg='Entry Message'):
        self.logger.info(' ' + STRING_DASHES)
        self.logger.info('|{0}|'.format(self.header_block(msg=msg, filler=' ')))
        self.logger.info(' ' + STRING_DASHES)

    @staticmethod
    def header_block(msg, filler=' ', str_count=140):
        """ Format Header
        This function will perform formatting a header like message being prompted in the console
        :return:
        """
        text = ':[ {0} ]:'.format(msg.title())
        return text.center(str_count, filler)

    def tx_data_formatter(self, sender_data, payload_data):
        header_data = '-:[ {0} ]:-'.format('Data')
        self.logger.info(' {0}{1}'.format(header_data, '-' * (140 - len(header_data))))
        information_data = ' (#) Sender Data: {0}'.format(sender_data)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))
        information_data = ' (#) Payload Data: {0}'.format(payload_data)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))
        self.logger.info(' ' + STRING_DASHES)

    def tx_receipt_formatter(self, data):
        transaction_hash = HexBytes(data.transactionHash).hex()
        transaction_index = data.transactionIndex
        block_hash = HexBytes(data.blockHash).hex()
        block_number = data.blockNumber
        to_address = data.to
        gas_used = data.gasUsed
        cumulative_gas_used = data.cumulativeGasUsed
        contract_address = data.contractAddress
        status = data.status
        logs_bloom = HexBytes(data.logsBloom).hex()
        signature_v = HexBytes(data.v).hex()
        signature_r = HexBytes(data.r).hex()
        signature_s = HexBytes(data.s).hex()

        header_data = '-:[ {0} ]:-'.format('Safe Tx Receipt')
        self.logger.info(' {0}{1}'.format(header_data, '-' * (140 - len(header_data))))

        information_data = ' (#) Address To: {0} Contract Address: {1}'.format(to_address, contract_address)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        information_data = ' (#) Status: {0} | Tx Index: {1} | Tx Hash: {2}'.format(status, transaction_index,
                                                                                    transaction_hash)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        information_data = ' (#) Block Number: {0} | Block Hash: {1}'.format(block_number, block_hash)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        information_data = ' (#) Gas Used: {0} | Cumulative Gas Used: {1}'.format(gas_used, cumulative_gas_used)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        information_data = ' (#) Signature v: {0}'.format(signature_v)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        information_data = ' (#) Signature r: {0}'.format(signature_r)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        information_data = ' (#) Signature s: {0}'.format(signature_s)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        log0_transaction_hash = HexBytes(data.logs[0]['transactionHash']).hex()
        log0_block_hash = HexBytes(data.logs[0]['blockHash']).hex()
        log0_block_number = data.logs[0]['blockNumber']
        log0_address = data.logs[0]['address']
        log0_data = data.logs[0]['data']
        log0_topic = HexBytes(data.logs[0]['topics'][0]).hex()
        log0_mined = data.logs[0]['type']

        header_data = '-:[ {0} ]:-'.format('Tx Log Number 0')
        self.logger.info(' {0}{1}'.format(header_data, '-' * (140 - len(header_data))))

        information_data = ' (#) Address To: {0}'.format(log0_address)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        information_data = ' (#) Tx Hash: {0}'.format(log0_transaction_hash)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        information_data = ' (#) Block Number: {0} | Block Hash: {1}'.format(log0_block_number, log0_block_hash)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        information_data = ' (#) Data:'
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))
        self.logger.info('|    {0}{1}|'.format(log0_data, ' ' * (140 - len(log0_data) - 4)))

        information_data = ' (#) Topic: {0} | Type: {1}'.format(log0_topic, log0_mined)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        log1_transaction_hash = HexBytes(data.logs[1]['transactionHash']).hex()
        log1_block_hash = HexBytes(data.logs[1]['blockHash']).hex()
        log1_block_number = data.logs[1]['blockNumber']
        log1_address = data.logs[1]['address']
        log1_data = data.logs[1]['data']
        log1_topic = HexBytes(data.logs[1]['topics'][0]).hex()
        log1_mined = data.logs[1]['type']

        header_data = '-:[ {0} ]:-'.format('Tx Log Number 1')
        self.logger.info(' {0}{1}'.format(header_data, '-' * (140 - len(header_data))))

        information_data = ' (#) Address To: {0}'.format(log1_address)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        information_data = ' (#) Tx Hash: {0}'.format(log1_transaction_hash)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        information_data = ' (#) Block Number: {0} | Block Hash: {1}'.format(log1_block_number, log1_block_hash)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))

        information_data = ' (#) Data:'
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))
        self.logger.info('|    {0}{1}|'.format(log1_data, ' ' * (140 - len(log1_data) - 4)))

        information_data = ' (#) Topic: {0} | Type: {1}'.format(log1_topic, log1_mined)
        self.logger.info('| {0}{1}|'.format(information_data, ' ' * (140 - len(information_data) - 1)))
        self.logger.info(' ' + STRING_DASHES)
