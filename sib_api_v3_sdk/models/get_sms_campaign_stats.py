# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  | 

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetSmsCampaignStats(object):
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
        'delivered': 'int',
        'sent': 'int',
        'processing': 'int',
        'soft_bounces': 'int',
        'hard_bounces': 'int',
        'unsubscriptions': 'int',
        'answered': 'int'
    }

    attribute_map = {
        'delivered': 'delivered',
        'sent': 'sent',
        'processing': 'processing',
        'soft_bounces': 'softBounces',
        'hard_bounces': 'hardBounces',
        'unsubscriptions': 'unsubscriptions',
        'answered': 'answered'
    }

    def __init__(self, delivered=None, sent=None, processing=None, soft_bounces=None, hard_bounces=None, unsubscriptions=None, answered=None):
        """
        GetSmsCampaignStats - a model defined in Swagger
        """

        self._delivered = None
        self._sent = None
        self._processing = None
        self._soft_bounces = None
        self._hard_bounces = None
        self._unsubscriptions = None
        self._answered = None

        self.delivered = delivered
        self.sent = sent
        self.processing = processing
        self.soft_bounces = soft_bounces
        self.hard_bounces = hard_bounces
        self.unsubscriptions = unsubscriptions
        self.answered = answered

    @property
    def delivered(self):
        """
        Gets the delivered of this GetSmsCampaignStats.
        Number of delivered SMS

        :return: The delivered of this GetSmsCampaignStats.
        :rtype: int
        """
        return self._delivered

    @delivered.setter
    def delivered(self, delivered):
        """
        Sets the delivered of this GetSmsCampaignStats.
        Number of delivered SMS

        :param delivered: The delivered of this GetSmsCampaignStats.
        :type: int
        """
        if delivered is None:
            raise ValueError("Invalid value for `delivered`, must not be `None`")

        self._delivered = delivered

    @property
    def sent(self):
        """
        Gets the sent of this GetSmsCampaignStats.
        Number of sent SMS

        :return: The sent of this GetSmsCampaignStats.
        :rtype: int
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """
        Sets the sent of this GetSmsCampaignStats.
        Number of sent SMS

        :param sent: The sent of this GetSmsCampaignStats.
        :type: int
        """
        if sent is None:
            raise ValueError("Invalid value for `sent`, must not be `None`")

        self._sent = sent

    @property
    def processing(self):
        """
        Gets the processing of this GetSmsCampaignStats.
        Number of processing SMS

        :return: The processing of this GetSmsCampaignStats.
        :rtype: int
        """
        return self._processing

    @processing.setter
    def processing(self, processing):
        """
        Sets the processing of this GetSmsCampaignStats.
        Number of processing SMS

        :param processing: The processing of this GetSmsCampaignStats.
        :type: int
        """
        if processing is None:
            raise ValueError("Invalid value for `processing`, must not be `None`")

        self._processing = processing

    @property
    def soft_bounces(self):
        """
        Gets the soft_bounces of this GetSmsCampaignStats.
        Number of softbounced SMS

        :return: The soft_bounces of this GetSmsCampaignStats.
        :rtype: int
        """
        return self._soft_bounces

    @soft_bounces.setter
    def soft_bounces(self, soft_bounces):
        """
        Sets the soft_bounces of this GetSmsCampaignStats.
        Number of softbounced SMS

        :param soft_bounces: The soft_bounces of this GetSmsCampaignStats.
        :type: int
        """
        if soft_bounces is None:
            raise ValueError("Invalid value for `soft_bounces`, must not be `None`")

        self._soft_bounces = soft_bounces

    @property
    def hard_bounces(self):
        """
        Gets the hard_bounces of this GetSmsCampaignStats.
        Number of hardbounced SMS

        :return: The hard_bounces of this GetSmsCampaignStats.
        :rtype: int
        """
        return self._hard_bounces

    @hard_bounces.setter
    def hard_bounces(self, hard_bounces):
        """
        Sets the hard_bounces of this GetSmsCampaignStats.
        Number of hardbounced SMS

        :param hard_bounces: The hard_bounces of this GetSmsCampaignStats.
        :type: int
        """
        if hard_bounces is None:
            raise ValueError("Invalid value for `hard_bounces`, must not be `None`")

        self._hard_bounces = hard_bounces

    @property
    def unsubscriptions(self):
        """
        Gets the unsubscriptions of this GetSmsCampaignStats.
        Number of unsubscription SMS

        :return: The unsubscriptions of this GetSmsCampaignStats.
        :rtype: int
        """
        return self._unsubscriptions

    @unsubscriptions.setter
    def unsubscriptions(self, unsubscriptions):
        """
        Sets the unsubscriptions of this GetSmsCampaignStats.
        Number of unsubscription SMS

        :param unsubscriptions: The unsubscriptions of this GetSmsCampaignStats.
        :type: int
        """
        if unsubscriptions is None:
            raise ValueError("Invalid value for `unsubscriptions`, must not be `None`")

        self._unsubscriptions = unsubscriptions

    @property
    def answered(self):
        """
        Gets the answered of this GetSmsCampaignStats.
        Number of replies to the SMS

        :return: The answered of this GetSmsCampaignStats.
        :rtype: int
        """
        return self._answered

    @answered.setter
    def answered(self, answered):
        """
        Sets the answered of this GetSmsCampaignStats.
        Number of replies to the SMS

        :param answered: The answered of this GetSmsCampaignStats.
        :type: int
        """
        if answered is None:
            raise ValueError("Invalid value for `answered`, must not be `None`")

        self._answered = answered

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
        if not isinstance(other, GetSmsCampaignStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other