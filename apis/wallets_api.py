# coding: utf-8

"""
WalletsApi.py
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


class WalletsApi(object):
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

    def getallthewalletsfora_business(self, business_id, **kwargs):
        """
        Get all the wallets for a Business
        This endpoints lists all wallets belonging to a business.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.getallthewalletsfora_business(business_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str business_id: This could be the ID of the business or the ID of a sub-account of the business (required)
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
                    " to method getallthewalletsfora_business" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_id' is set
        if ('business_id' not in params) or (params['business_id'] is None):
            raise ValueError("Missing the required parameter `business_id` when calling `getallthewalletsfora_business`")

        resource_path = '/wallets'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'business_id' in params:
            query_params['businessID'] = params['business_id']

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

    def getawallet(self, wallet_id, **kwargs):
        """
        Get a wallet
        This endpoint provides the information regarding a specific wallet.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.getawallet(wallet_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str wallet_id: The ID of the wallet (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wallet_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getawallet" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'wallet_id' is set
        if ('wallet_id' not in params) or (params['wallet_id'] is None):
            raise ValueError("Missing the required parameter `wallet_id` when calling `getawallet`")

        resource_path = '/wallets/{walletID}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'wallet_id' in params:
            path_params['walletID'] = params['wallet_id']

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
