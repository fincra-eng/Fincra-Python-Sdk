# coding: utf-8

"""
DisbursementsApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DisbursementsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def make_a_payout(self, **kwargs):
        """
        Make A Payout
        This endpoint is used for making a payment out to the beneficiaries of the business who are not registered on our platform\n\nREQUEST BODY\n\n* * *\n\n| Field | Data Type | description |\n| --- | --- | --- |\n| sourceCurrency | string | The currency which the business is to send payment in `required` |\n| destinationCurrency | string | The currency which the beneficiary is to receive payment in`required` |\n| amount | string | The amount to be paid out`required` |\n| business | string | This could be the ID of the business or the ID of a sub-account of the business `required` |\n| description | string | `required` |\n| customerReference | string | This is the unique reference generated for the transaction on your platform `optional` |\n| beneficiary | object | See the description of the beneficiary object below`required` |\n| paymentDestination | string | This is where the payment is to be made. the value will be one of the following: *bank_account*, *mobile_money_wallet* `required` |\n| quoteReference | string | This is required if the payout is a cross currency payout(e.g, NGN to USD). If this is a single currency payout (e.g, EUR to EUR), a quote reference is not required. To get a quote reference, you will need to call the generate quote endpoint below |\n| paymentScheme | string | This is the valid payment scheme for the destination currency.Payment scheme is required for all USD,EUR and GBP payouts |\n\nThe beneficiaries information varies based on the currency and beneficiary type (individual or corporate). Find the breakdown of the beneficiaries object below:\n\nDescription of `INDIVIDUAL` or `CORPORATE` Beneficiary information for `NGN` and `KES` payout:\n\n| Field | Data Type | description |\n| --- | --- | --- |\n| lastName | string | The last name of the beneficiary. it is `required` if type is **individual** and `optional` if type is **corporate** |\n| firstName | string | The first name of the beneficiary if type is **individual** or the name of the corporation if type is **corporate** `required` |\n| accountNumber | string | This is the bank account number of the beneficiary or phone number if the account is a mobile money wallet. `required` |\n| accountHolderName | string | This is the name on the bank account of the beneficiary. `required` |\n| bankCode | string | This value is either the code for your bank or mobile money wallet provider. To get this value, you will need to call the get bank code endpoint below `required` |\n| type | string | the value can either be **individual** or **corporate** `required` |\n| country | string | `optional` |\n| email | string | `optional` |\n\nDescription of `INDIVIDUAL` or `CORPORATE` Beneficiary information for `GHS` and `ZAR` payout:\n\n| Field | Data Type | description |\n| --- | --- | --- |\n| lastName | string | The last name of the beneficiary. it is `required` if type is **individual** and `optional` if type is **corporate** |\n| firstName | string | The first name of the beneficiary if type is **individual** or the name of the corporation if type is **corporate** `required` |\n| accountHolderName | string | This is the name on the bank account of the beneficiary. `required` |\n| accountNumber | string | This is the bank account number of the beneficiary or phone number if the account is a mobile money wallet. `required` |\n| bankCode | string | This value is either the code for your bank or mobile money wallet provider. To get this value, you will need to call the get bank code endpoint below `required` |\n| sortCode(branchCode) | string | To get this code, you will need to call the get bank branch endpoint below `required` |\n| type | string | the value can either be **individual** or **corporate** `required` |\n| country | string | `optional` |\n| email | string | `optional` |\n\nDescription of `INDIVIDUAL` Beneficiary information for `EUR` payout:\n\n| Field | Data Type | description |\n| --- | --- | --- |\n| lastName | string | The last name of the beneficiary. it is `required` |\n| firstName | string | The first name of the beneficiary |\n| accountHolderName | string | This is the name on the bank account of the beneficiary. `required` |\n| accountNumber | string | This value of this field will be IBAN of the beneficiary. Depending on the country, the IBAN is mostly made up of the following format: *Country code + check digits + bank code + sort code + account number*. Kindly visit this page to see the IBAN format for different countries.`required` |\n| type | string | the value can either be **individual** or **corporate** `required` |\n| country | string | `optional` |\n| email | string | `optional` |\n| mobile | string | `optional` |\n| bankSwiftCode | string | `optional` |\n| birthDate | string | `optional` |\n| birthPlace | string | `optional` |\n| address | object | This contains all the optional address information. They are:    \+ country: country of origin `optional`  \+ zip `optional`  \+ street `optional`  \+ state `optional`  \+ city `optional` |\n| document | object | This contains the optional information in your means of identification. They are:    \+ type: type of ID document e.g International Passport `optional`  \+ number `optional`  \+ issuedCountryCode e.g NG `optional`  \+ issuedBy `optional`  \+ issuedDate with Format \"YYYY-mm-dd\" `optional`  \+ expirationDate with Format \"YYYY-mm-dd\" `optional` |\n\nDescription of `CORPORATE` Beneficiary information for `EUR` payout:\n\n| Field | Data Type | description |\n| --- | --- | --- |\n| accountHolderName | string | This is the name on the bank account of the beneficiary. `required` |\n| accountNumber | string | This value of this field will be IBAN of the beneficiary. Depending on the country, the IBAN is mostly made up of the following format: *Country code + check digits + bank code + sort code + account number*. Kindly visit this page to see the IBAN format for different countries.`required` |\n| type | string | the value can either be **individual** or **corporate** `required` |\n| country | string | `optional` |\n| email | string | `optional` |\n| mobile | string | `optional` |\n| bankSwiftCode | string | `optional` |\n| registrationNumber | string | `optional` |\n| address | object | This contains all the optional address information. They are:    \+ country: country of origin `optional`  \+ zip `optional`  \+ street `optional`  \+ state `optional`  \+ city `optional` |\n| document | object | This contains the optional information in your means of identification. They are:    \+ type: type of ID document e.g International Passport `optional`  \+ number `optional`  \+ issuedCountryCode e.g NG `optional`  \+ issuedBy `optional`  \+ issuedDate with Format \"YYYY-mm-dd\" `optional`  \+ expirationDate with Format \"YYYY-mm-dd\" `optional` |\n\nDescription of `CORPORATE` Beneficiary information for `GBP` payout:\n\n| Field | Data Type | description |\n| --- | --- | --- |\n| accountHolderName | string | This is the name on the bank account of the beneficiary. `required` |\n| accountNumber | string | This should be the beneficiary's account number`required` |\n| type | string | the value can either be **individual** or **corporate** `required` |\n| country | string | `optional` |\n| email | string | `optional` |\n| mobile | string | `optional` |\n| bankSwiftCode | string | `optional` |\n| sortCode | string | `required` |\n| registrationNumber | string | `optional` |\n| address | object | This contains all the optional address information. They are:    \+ country: country of origin `optional`  \+ zip `optional`  \+ street `optional`  \+ state `optional`  \+ city `optional` |\n| document | object | This contains the optional information in your means of identification. They are:    \+ type: type of ID document e.g International Passport `optional`  \+ number `optional`  \+ issuedCountryCode e.g NG `optional`  \+ issuedBy `optional`  \+ issuedDate with Format \"YYYY-mm-dd\" `optional`  \+ expirationDate with Format \"YYYY-mm-dd\" `optional` |\n\nDescription of `INDIVIDUAL` Beneficiary information for `GBP` payout:\n\n| Field | Data Type | description |\n| --- | --- | --- |\n| lastName | string | The last name of the beneficiary. it is `required` |\n| firstName | string | The first name of the beneficiary |\n| accountHolderName | string | This is the name on the bank account of the beneficiary. `required` |\n| accountNumber | string | This should be the beneficiary's account number`required` |\n| type | string | the value can either be **individual** or **corporate** `required` |\n| country | string | `optional` |\n| email | string | `optional` |\n| mobile | string | `optional` |\n| bankSwiftCode | string | `optional` |\n| sortCode | string | `required` |\n| birthDate | string | `optional` |\n| birthPlace | string | `optional` |\n| address | object | This contains all the optional address information. They are:    \+ country: country of origin `optional`  \+ zip `optional`  \+ street `optional`  \+ state `optional`  \+ city `optional` |\n| document | object | This contains the optional information in your means of identification. They are:    \+ type: type of ID document e.g International Passport `optional`  \+ number `optional`  \+ issuedCountryCode e.g NG `optional`  \+ issuedBy `optional`  \+ issuedDate with Format \"YYYY-mm-dd\" `optional`  \+ expirationDate with Format \"YYYY-mm-dd\" `optional` |\n\nDescription of `CORPORATE` Beneficiary information for `USD` payout:\n\n| Field | Data Type | description |\n| --- | --- | --- |\n| accountHolderName | string | This is the name on the bank account of the beneficiary. `required` |\n| accountNumber | string | This should be the beneficiary's account number`required` |\n| type | string | the value can either be **individual** or **corporate** `required` |\n| country | string | `optional` |\n| email | string | `optional` |\n| mobile | string | `optional` |\n| bankSwiftCode | string | `required` |\n| sortCode | string | `required` |\n| registrationNumber | string | `optional` |\n| address | object | This contains all the optional address information. They are:    \+ country: country of origin `optional`  \+ zip `optional`  \+ street `optional`  \+ state `optional`  \+ city `optional` |\n| document | object | This contains the optional information in your means of identification. They are:    \+ type: type of ID document e.g International Passport `optional`  \+ number `optional`  \+ issuedCountryCode e.g NG `optional`  \+ issuedBy `optional`  \+ issuedDate with Format \"YYYY-mm-dd\" `optional`  \+ expirationDate with Format \"YYYY-mm-dd\" `optional` |\n\nDescription of `INDIVIDUAL` Beneficiary information for `USD` payout:\n\n| Field | Data Type | description |\n| --- | --- | --- |\n| lastName | string | The last name of the beneficiary. it is `required` |\n| firstName | string | The first name of the beneficiary |\n| accountHolderName | string | This is the name on the bank account of the beneficiary. `required` |\n| accountNumber | string | This should be the beneficiary's account number`required` |\n| type | string | the value can either be **individual** or **corporate** `required` |\n| country | string | `optional` |\n| email | string | `optional` |\n| mobile | string | `optional` |\n| bankSwiftCode | string | `required` |\n| sortCode | string | `required` |\n| birthDate | string | `optional` |\n| birthPlace | string | `optional` |\n| address | object | This contains all the optional address information. They are:    \+ country: country of origin `optional`  \+ zip `optional`  \+ street `optional`  \+ state `optional`  \+ city `optional` |\n| document | object | This contains the optional information in your means of identification. They are:    \+ type: type of ID document e.g International Passport `optional`  \+ number `optional`  \+ issuedCountryCode e.g NG `optional`  \+ issuedBy `optional`  \+ issuedDate with Format \"YYYY-mm-dd\" `optional`  \+ expirationDate with Format \"YYYY-mm-dd\" `optional` |

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.make_a_payout(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method make_a_payout" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/disbursements/payouts'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def make_an_internal_payout(self, **kwargs):
        """
        Make  An Internal  Payout
        This endpoint is used for making a payment out to a customer/user/subaccount on our platform\n\nREQUEST BODY\n\n* * *\n\n| Field | Data Type | description |\n| --- | --- | --- |\n| amount | string | The amount to be paid out`required` |\n| business | string | This could be the ID of the business or the ID of a sub-account of the business `required` |\n| customerReference | string | This is the unique reference generated for the transaction on your platform. `required` |\n| description | string | `required` |\n| beneficiaryWalletNumber | string | This is the unique wallet of the beneficiary you want to pay to `required` |

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.make_an_internal_payout(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method make_an_internal_payout" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/disbursements/payouts/wallets'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def getallsettlementsfora_business(self, business_id, **kwargs):
        """
        Get all settlements for a Business
        This endpoint provides a list of all the settlements for a business.\n\n\nREQUEST BODY\n\n\n| Field | Data Type | Description |\n|------| ------------- | ----------- |\n| page | string | Specify exactly what page you want to retrieve optional|\n| perPage | string | Specify how many records you want to retrieve per page optional|\n| from | string| Specify start date with format \"YYYY-mm-dd\"  optional|\n| to | string| Specify end date with format \"YYYY-mm-dd\" optional|

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.getallsettlementsfora_business(business_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_id: businessID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getallsettlementsfora_business" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_id' is set
        if ('business_id' not in params) or (params['business_id'] is None):
            raise ValueError("Missing the required parameter `business_id` when calling `getallsettlementsfora_business`")

        resource_path = '/disbursements/settlements/search/business/{businessID}'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        if 'business_id' in params:
            path_params['businessID'] = params['business_id']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def getasettlementforabusiness(self, settlement_id, **kwargs):
        """
        Get a settlement for a business
        This endpoint provides the details of a settlement through the use of its ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.getasettlementforabusiness(settlement_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str settlement_id: settlementId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settlement_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getasettlementforabusiness" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'settlement_id' is set
        if ('settlement_id' not in params) or (params['settlement_id'] is None):
            raise ValueError("Missing the required parameter `settlement_id` when calling `getasettlementforabusiness`")

        resource_path = '/disbursements/settlements/{settlementId}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'settlement_id' in params:
            path_params['settlementId'] = params['settlement_id']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
