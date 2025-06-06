# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GeospatialAnalysisResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, heatmap_url: str=None, geojson_data: object=None):  # noqa: E501
        """GeospatialAnalysisResponse - a model defined in Swagger

        :param heatmap_url: The heatmap_url of this GeospatialAnalysisResponse.  # noqa: E501
        :type heatmap_url: str
        :param geojson_data: The geojson_data of this GeospatialAnalysisResponse.  # noqa: E501
        :type geojson_data: object
        """
        self.swagger_types = {
            'heatmap_url': str,
            'geojson_data': object
        }

        self.attribute_map = {
            'heatmap_url': 'heatmap_url',
            'geojson_data': 'geojson_data'
        }
        self._heatmap_url = heatmap_url
        self._geojson_data = geojson_data

    @classmethod
    def from_dict(cls, dikt) -> 'GeospatialAnalysisResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GeospatialAnalysisResponse of this GeospatialAnalysisResponse.  # noqa: E501
        :rtype: GeospatialAnalysisResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def heatmap_url(self) -> str:
        """Gets the heatmap_url of this GeospatialAnalysisResponse.

        URL to the generated heatmap.  # noqa: E501

        :return: The heatmap_url of this GeospatialAnalysisResponse.
        :rtype: str
        """
        return self._heatmap_url

    @heatmap_url.setter
    def heatmap_url(self, heatmap_url: str):
        """Sets the heatmap_url of this GeospatialAnalysisResponse.

        URL to the generated heatmap.  # noqa: E501

        :param heatmap_url: The heatmap_url of this GeospatialAnalysisResponse.
        :type heatmap_url: str
        """

        self._heatmap_url = heatmap_url

    @property
    def geojson_data(self) -> object:
        """Gets the geojson_data of this GeospatialAnalysisResponse.

        Habitat data in GeoJSON format.  # noqa: E501

        :return: The geojson_data of this GeospatialAnalysisResponse.
        :rtype: object
        """
        return self._geojson_data

    @geojson_data.setter
    def geojson_data(self, geojson_data: object):
        """Sets the geojson_data of this GeospatialAnalysisResponse.

        Habitat data in GeoJSON format.  # noqa: E501

        :param geojson_data: The geojson_data of this GeospatialAnalysisResponse.
        :type geojson_data: object
        """

        self._geojson_data = geojson_data
