# coding: utf-8

"""
ConversionsApi.py
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


class ConversionsApi(object):
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

    def getallconversions(self, business_id, **kwargs):
        """
        Get all conversions
        This endpoint provides a list of all conversions performed by a business.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.getallconversions(business_id, callback=callback_function)

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
                    " to method getallconversions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'business_id' is set
        if ('business_id' not in params) or (params['business_id'] is None):
            raise ValueError("Missing the required parameter `business_id` when calling `getallconversions`")

        resource_path = '/conversions/business/{businessId}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'business_id' in params:
            path_params['businessId'] = params['business_id']

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

    def initiateaconversion(self, **kwargs):
        """
        Initiate a conversion
        This endpoint provides information on the conversion rate between two currencies e.g NGN to USD\n\n\n\n\nREQUEST BODY\n\n\n| Field | Data Type | Description |\n|------| ------------- | ----------- |\n| business | string | This could be the ID of the business or the ID of a sub-account of the businessRequired |\n| quoteReference | string | To get a quote reference, you will need to call the generate quote endpoint Required |

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.initiateaconversion(callback=callback_function)

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
                    " to method initiateaconversion" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/conversions/initiate'.replace('{format}', 'json')
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

    def getaconversion(self, conversion_id, **kwargs):
        """
        Get a conversion
        This endpoint fetches a specific conversion performed by a business.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.getaconversion(conversion_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str conversion_id: The ID of the conversion (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['conversion_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getaconversion" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'conversion_id' is set
        if ('conversion_id' not in params) or (params['conversion_id'] is None):
            raise ValueError("Missing the required parameter `conversion_id` when calling `getaconversion`")

        resource_path = '/conversions/{conversionId}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'conversion_id' in params:
            path_params['conversionId'] = params['conversion_id']

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