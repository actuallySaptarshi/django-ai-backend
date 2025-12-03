from rest_framework import serializers

class TestSerializer(serializers.Serializer):
    f1 = serializers.CharField(max_length=100)
    f2 = serializers.IntegerField()
    # Add more fields as needed

"""
class MessageSerializer(serializers.Serializer):
    Validates a single message dictionary with 'role' and 'content'.
    role = serializers.CharField(max_length=100)
    content = serializers.CharField()
"""

class ChatSerializer(serializers.Serializer):
    """
    This serializer handles a custom payload in the form of a
    dictionary with string key-value pairs.
    """
    # This field will accept any dictionary where keys are strings
    # and values are also strings.
    #messages = serializers.ListField(
    #    child=MessageSerializer()
    #)
    id = serializers.IntegerField(allow_null=True, required=False)
    messages = serializers.JSONField()