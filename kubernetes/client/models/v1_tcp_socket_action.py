# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1TCPSocketAction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'host': 'str',
        'port': 'object'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port'
    }

    def __init__(self, host=None, port=None):
        """
        V1TCPSocketAction - a model defined in Swagger
        """

        self._host = None
        self._port = None
        self.discriminator = None

        if host is not None:
          self.host = host
        self.port = port

    @property
    def host(self):
        """
        Gets the host of this V1TCPSocketAction.
        Optional: Host name to connect to, defaults to the pod IP.

        :return: The host of this V1TCPSocketAction.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this V1TCPSocketAction.
        Optional: Host name to connect to, defaults to the pod IP.

        :param host: The host of this V1TCPSocketAction.
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """
        Gets the port of this V1TCPSocketAction.
        Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.

        :return: The port of this V1TCPSocketAction.
        :rtype: object
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this V1TCPSocketAction.
        Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.

        :param port: The port of this V1TCPSocketAction.
        :type: object
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")

        self._port = port

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1TCPSocketAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
