# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.data_management_transform_request_parameters import DataManagementTransformRequestParameters  # noqa: F401,E501
from swagger_server import util


class DataManagementTransformRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, dataset_url: str=None, transformation_type: str=None, parameters: DataManagementTransformRequestParameters=None):  # noqa: E501
        """DataManagementTransformRequest - a model defined in Swagger

        :param dataset_url: The dataset_url of this DataManagementTransformRequest.  # noqa: E501
        :type dataset_url: str
        :param transformation_type: The transformation_type of this DataManagementTransformRequest.  # noqa: E501
        :type transformation_type: str
        :param parameters: The parameters of this DataManagementTransformRequest.  # noqa: E501
        :type parameters: DataManagementTransformRequestParameters
        """
        self.swagger_types = {
            'dataset_url': str,
            'transformation_type': str,
            'parameters': DataManagementTransformRequestParameters
        }

        self.attribute_map = {
            'dataset_url': 'dataset_url',
            'transformation_type': 'transformation_type',
            'parameters': 'parameters'
        }
        self._dataset_url = dataset_url
        self._transformation_type = transformation_type
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt) -> 'DataManagementTransformRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataManagementTransformRequest of this DataManagementTransformRequest.  # noqa: E501
        :rtype: DataManagementTransformRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dataset_url(self) -> str:
        """Gets the dataset_url of this DataManagementTransformRequest.

        URL to the dataset to transform.  # noqa: E501

        :return: The dataset_url of this DataManagementTransformRequest.
        :rtype: str
        """
        return self._dataset_url

    @dataset_url.setter
    def dataset_url(self, dataset_url: str):
        """Sets the dataset_url of this DataManagementTransformRequest.

        URL to the dataset to transform.  # noqa: E501

        :param dataset_url: The dataset_url of this DataManagementTransformRequest.
        :type dataset_url: str
        """

        self._dataset_url = dataset_url

    @property
    def transformation_type(self) -> str:
        """Gets the transformation_type of this DataManagementTransformRequest.

        Type of transformation to apply (e.g., normalization, encoding).  # noqa: E501

        :return: The transformation_type of this DataManagementTransformRequest.
        :rtype: str
        """
        return self._transformation_type

    @transformation_type.setter
    def transformation_type(self, transformation_type: str):
        """Sets the transformation_type of this DataManagementTransformRequest.

        Type of transformation to apply (e.g., normalization, encoding).  # noqa: E501

        :param transformation_type: The transformation_type of this DataManagementTransformRequest.
        :type transformation_type: str
        """

        self._transformation_type = transformation_type

    @property
    def parameters(self) -> DataManagementTransformRequestParameters:
        """Gets the parameters of this DataManagementTransformRequest.


        :return: The parameters of this DataManagementTransformRequest.
        :rtype: DataManagementTransformRequestParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: DataManagementTransformRequestParameters):
        """Sets the parameters of this DataManagementTransformRequest.


        :param parameters: The parameters of this DataManagementTransformRequest.
        :type parameters: DataManagementTransformRequestParameters
        """

        self._parameters = parameters
