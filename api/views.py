# api/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import guestChats
from homepage.models import users
import requests

# Change this import from: from . import serializer
from .serializer import TestSerializer, ChatSerializer

class Test(APIView):
    def post(self, request):
        # Now, you can use CustomRequestSerializer directly
        serializer_instance = TestSerializer(data=request.data)
        
        # Use the new variable name
        if serializer_instance.is_valid():
            # You can access validated data like this:
            # field1_data = serializer_instance.validated_data['field1']
            response_data = {
                "message": "Data Recieved successfully",
                "Body" : serializer_instance.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
            
        # Return the errors from the serializer instance
        return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)


class Chat(APIView):
    """
    This view processes a request containing a dictionary payload.
    """
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        
        if serializer.is_valid():
            # Access the validated dictionary
            validated_messages = serializer.validated_data['messages']
            
            message_data = {
                "model": "gemma3",
                "messages": validated_messages,
                "stream": False
            }
            
            try:
                chat_id = serializer.validated_data.get('id')
                ollama_response = requests.post("http://localhost:11434/api/chat", json=message_data).json()
                validated_messages.append(ollama_response["message"])
                User = users.objects.get(name="public")
                if not chat_id:
                    obj = guestChats.objects.create(
                        chats=validated_messages
                    )
                    User.chats += 1
                    User.promptsAnswered += 1
                    User.save()
                    return Response({"message": ollama_response["message"], "id": obj.id}, status=status.HTTP_200_OK)
                else:
                    messageTable = guestChats.objects.get(id=chat_id)
                    messageTable.chats = validated_messages
                    messageTable.save()
                    User.promptsAnswered += 1
                    User.save()
                    return Response({"message": ollama_response["message"], "id": messageTable.id}, status=status.HTTP_200_OK)
                
            except Exception as e:
                ollama_response = requests.post("http://localhost:11434/api/chat", json=message_data).json()
                validated_messages.append(ollama_response["message"])
                obj = guestChats.objects.create(
                    chats=validated_messages
                )
                User.chats += 1
                User.promptsAnswered += 1
                User.save()
                return Response({"message": ollama_response["message"], "id": obj.id}, status=status.HTTP_200_OK)

            except requests.exceptions.RequestException as e:
                return Response({"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


"""
API Usage:
This API Can be used to integrate complex frontend applications using React, Flutter. Django does the heavy lifting of AI Handling and Chat Storage!

---

- New Conversation:
When no chat id is mentioned, the server will assign you with a new chat id
{
    "messages": [
        {
            "role":"user",
            "content":"Hello"
        }
    ]
}

Response:
{
    "message": {
        "role": "assistant",
        "content": "Hello there! How can I help you today? 😊 \n\nDo you want to:\n\n*   Chat about something?\n*   Ask me a question?\n*   Play a game?\n*   Get some information?\n\nJust let me know what you'd like to do."
    },
    "id": 2 # This chat id is used to store chat history in the database and can be used to append old messages
}

- Old conversation (with chat id):

{"id": 2 ,"messages": [{
        "role":"user",
        "content":"Hello"
    },
    {
        "role": "assistant",
        "content": "Hello there! How can I help you today? 😊 \n\nDo you want to:\n\n*   Chat about something?\n*   Ask me a question?\n*   Play a game?\n*   Get some information?\n\nJust let me know what you'd like to do."
    },
    {
        "role":"user",
        "content":"Coding is quite easy!"
    }]
}

Response:

{
    "message": {
        "role": "assistant",
        "content": "That’s fantastic to hear! It’s really rewarding when you start to grasp the basics. \n\nIt *can* be easy to get started with some languages like Python, which is often recommended for beginners. But it's also true that coding can become quite complex as you delve into more advanced topics. \n\nWhat kind of coding are you finding easy? Are you working with a particular language?"
    },
    "id": 2 # Stores this chat in the database in id 2
}

"""