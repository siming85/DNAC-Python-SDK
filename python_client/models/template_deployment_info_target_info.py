# coding: utf-8

"""
    Swagger

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TemplateDeploymentInfoTargetInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'host_name': 'str',
        'id': 'str',
        'params': 'object',
        'type': 'str'
    }

    attribute_map = {
        'host_name': 'hostName',
        'id': 'id',
        'params': 'params',
        'type': 'type'
    }

    def __init__(self, host_name=None, id=None, params=None, type=None):  # noqa: E501
        """TemplateDeploymentInfoTargetInfo - a model defined in Swagger"""  # noqa: E501

        self._host_name = None
        self._id = None
        self._params = None
        self._type = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if id is not None:
            self.id = id
        if params is not None:
            self.params = params
        if type is not None:
            self.type = type

    @property
    def host_name(self):
        """Gets the host_name of this TemplateDeploymentInfoTargetInfo.  # noqa: E501


        :return: The host_name of this TemplateDeploymentInfoTargetInfo.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this TemplateDeploymentInfoTargetInfo.


        :param host_name: The host_name of this TemplateDeploymentInfoTargetInfo.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def id(self):
        """Gets the id of this TemplateDeploymentInfoTargetInfo.  # noqa: E501


        :return: The id of this TemplateDeploymentInfoTargetInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateDeploymentInfoTargetInfo.


        :param id: The id of this TemplateDeploymentInfoTargetInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def params(self):
        """Gets the params of this TemplateDeploymentInfoTargetInfo.  # noqa: E501


        :return: The params of this TemplateDeploymentInfoTargetInfo.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this TemplateDeploymentInfoTargetInfo.


        :param params: The params of this TemplateDeploymentInfoTargetInfo.  # noqa: E501
        :type: object
        """

        self._params = params

    @property
    def type(self):
        """Gets the type of this TemplateDeploymentInfoTargetInfo.  # noqa: E501


        :return: The type of this TemplateDeploymentInfoTargetInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TemplateDeploymentInfoTargetInfo.


        :param type: The type of this TemplateDeploymentInfoTargetInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["MANAGED_DEVICE_IP", "MANAGED_DEVICE_UUID", "PRE_PROVISIONED_SERIAL", "PRE_PROVISIONED_MAC", "DEFAULT", "MANAGED_DEVICE_HOSTNAME"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TemplateDeploymentInfoTargetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
