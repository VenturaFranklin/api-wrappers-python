# coding: utf-8

"""
    Moosend API

    TODO: Add a description

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Context17(object):
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
        'active_member_count': 'float',
        'bounced_member_count': 'float',
        'created_by': 'str',
        'created_on': 'str',
        'custom_fields_definition': 'list[CustomFieldsDefinition]',
        'id': 'str',
        'import_operation': 'ImportOperation19',
        'name': 'str',
        'removed_member_count': 'float',
        'status': 'float',
        'unsubscribed_member_count': 'float',
        'updated_by': 'str',
        'updated_on': 'str'
    }

    attribute_map = {
        'active_member_count': 'ActiveMemberCount',
        'bounced_member_count': 'BouncedMemberCount',
        'created_by': 'CreatedBy',
        'created_on': 'CreatedOn',
        'custom_fields_definition': 'CustomFieldsDefinition',
        'id': 'ID',
        'import_operation': 'ImportOperation',
        'name': 'Name',
        'removed_member_count': 'RemovedMemberCount',
        'status': 'Status',
        'unsubscribed_member_count': 'UnsubscribedMemberCount',
        'updated_by': 'UpdatedBy',
        'updated_on': 'UpdatedOn'
    }

    def __init__(self, active_member_count=None, bounced_member_count=None, created_by=None, created_on=None, custom_fields_definition=None, id=None, import_operation=None, name=None, removed_member_count=None, status=None, unsubscribed_member_count=None, updated_by=None, updated_on=None):
        """
        Context17 - a model defined in Swagger
        """

        self._active_member_count = None
        self._bounced_member_count = None
        self._created_by = None
        self._created_on = None
        self._custom_fields_definition = None
        self._id = None
        self._import_operation = None
        self._name = None
        self._removed_member_count = None
        self._status = None
        self._unsubscribed_member_count = None
        self._updated_by = None
        self._updated_on = None

        if active_member_count is not None:
          self.active_member_count = active_member_count
        if bounced_member_count is not None:
          self.bounced_member_count = bounced_member_count
        if created_by is not None:
          self.created_by = created_by
        if created_on is not None:
          self.created_on = created_on
        if custom_fields_definition is not None:
          self.custom_fields_definition = custom_fields_definition
        if id is not None:
          self.id = id
        if import_operation is not None:
          self.import_operation = import_operation
        if name is not None:
          self.name = name
        if removed_member_count is not None:
          self.removed_member_count = removed_member_count
        if status is not None:
          self.status = status
        if unsubscribed_member_count is not None:
          self.unsubscribed_member_count = unsubscribed_member_count
        if updated_by is not None:
          self.updated_by = updated_by
        if updated_on is not None:
          self.updated_on = updated_on

    @property
    def active_member_count(self):
        """
        Gets the active_member_count of this Context17.
        

        :return: The active_member_count of this Context17.
        :rtype: float
        """
        return self._active_member_count

    @active_member_count.setter
    def active_member_count(self, active_member_count):
        """
        Sets the active_member_count of this Context17.
        

        :param active_member_count: The active_member_count of this Context17.
        :type: float
        """

        self._active_member_count = active_member_count

    @property
    def bounced_member_count(self):
        """
        Gets the bounced_member_count of this Context17.
        

        :return: The bounced_member_count of this Context17.
        :rtype: float
        """
        return self._bounced_member_count

    @bounced_member_count.setter
    def bounced_member_count(self, bounced_member_count):
        """
        Sets the bounced_member_count of this Context17.
        

        :param bounced_member_count: The bounced_member_count of this Context17.
        :type: float
        """

        self._bounced_member_count = bounced_member_count

    @property
    def created_by(self):
        """
        Gets the created_by of this Context17.
        

        :return: The created_by of this Context17.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Context17.
        

        :param created_by: The created_by of this Context17.
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """
        Gets the created_on of this Context17.
        

        :return: The created_on of this Context17.
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """
        Sets the created_on of this Context17.
        

        :param created_on: The created_on of this Context17.
        :type: str
        """

        self._created_on = created_on

    @property
    def custom_fields_definition(self):
        """
        Gets the custom_fields_definition of this Context17.
        

        :return: The custom_fields_definition of this Context17.
        :rtype: list[CustomFieldsDefinition]
        """
        return self._custom_fields_definition

    @custom_fields_definition.setter
    def custom_fields_definition(self, custom_fields_definition):
        """
        Sets the custom_fields_definition of this Context17.
        

        :param custom_fields_definition: The custom_fields_definition of this Context17.
        :type: list[CustomFieldsDefinition]
        """

        self._custom_fields_definition = custom_fields_definition

    @property
    def id(self):
        """
        Gets the id of this Context17.
        

        :return: The id of this Context17.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Context17.
        

        :param id: The id of this Context17.
        :type: str
        """

        self._id = id

    @property
    def import_operation(self):
        """
        Gets the import_operation of this Context17.

        :return: The import_operation of this Context17.
        :rtype: ImportOperation19
        """
        return self._import_operation

    @import_operation.setter
    def import_operation(self, import_operation):
        """
        Sets the import_operation of this Context17.

        :param import_operation: The import_operation of this Context17.
        :type: ImportOperation19
        """

        self._import_operation = import_operation

    @property
    def name(self):
        """
        Gets the name of this Context17.
        

        :return: The name of this Context17.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Context17.
        

        :param name: The name of this Context17.
        :type: str
        """

        self._name = name

    @property
    def removed_member_count(self):
        """
        Gets the removed_member_count of this Context17.
        

        :return: The removed_member_count of this Context17.
        :rtype: float
        """
        return self._removed_member_count

    @removed_member_count.setter
    def removed_member_count(self, removed_member_count):
        """
        Sets the removed_member_count of this Context17.
        

        :param removed_member_count: The removed_member_count of this Context17.
        :type: float
        """

        self._removed_member_count = removed_member_count

    @property
    def status(self):
        """
        Gets the status of this Context17.
        

        :return: The status of this Context17.
        :rtype: float
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Context17.
        

        :param status: The status of this Context17.
        :type: float
        """

        self._status = status

    @property
    def unsubscribed_member_count(self):
        """
        Gets the unsubscribed_member_count of this Context17.
        

        :return: The unsubscribed_member_count of this Context17.
        :rtype: float
        """
        return self._unsubscribed_member_count

    @unsubscribed_member_count.setter
    def unsubscribed_member_count(self, unsubscribed_member_count):
        """
        Sets the unsubscribed_member_count of this Context17.
        

        :param unsubscribed_member_count: The unsubscribed_member_count of this Context17.
        :type: float
        """

        self._unsubscribed_member_count = unsubscribed_member_count

    @property
    def updated_by(self):
        """
        Gets the updated_by of this Context17.
        

        :return: The updated_by of this Context17.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """
        Sets the updated_by of this Context17.
        

        :param updated_by: The updated_by of this Context17.
        :type: str
        """

        self._updated_by = updated_by

    @property
    def updated_on(self):
        """
        Gets the updated_on of this Context17.
        

        :return: The updated_on of this Context17.
        :rtype: str
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """
        Sets the updated_on of this Context17.
        

        :param updated_on: The updated_on of this Context17.
        :type: str
        """

        self._updated_on = updated_on

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
        if not isinstance(other, Context17):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other