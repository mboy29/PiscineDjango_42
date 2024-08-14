import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from chat.models.room import ChatRoom
from chat.models.message import ChatMessage

class ChatConsumer(WebsocketConsumer):

    """
    Consumer class for the chat application.

    Attributes:
        room_name (str): The name of the chat room.
    
    Methods:
        connect: Connects the user to the chat room.
        disconnect: Disconnects the user from the chat room.
        receive: Receives a message from the user and broadcasts it to the chat room.
        send_recent_messages: Sends the most recent messages to the user.
        send_user_list: Sends the list of users in the chat room to the user.
        send_join_notification: Sends a notification to the chat room when a user joins.
        send_leave_notification: Sends a notification to the chat room when a user leaves.
        chat_message: Sends a chat message to the user.
        user_list_update: Sends an updated user list to the user.
    """

    def connect(self):

        """
        Connects the user to the chat room, adds the user to the group, 
        and sends the most recent messages and user list.

        Args:
            self (ChatConsumer): The ChatConsumer instance.
        
        Returns: None
        """

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        try:
            self.room = ChatRoom.fetch(self.room_name)
        except ChatRoom.DoesNotExist:
            self.close()
            return
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.room.users_add(self.scope["user"])
        self.accept()
        self.send_recent_messages()
        self.send_user_list()
        self.send_join_notification()

    def disconnect(self, close_code):

        """
        Disconnects the user from the chat room, removes the user 
        from the group, and sends a notification to the chat room.

        Args:
            self (ChatConsumer): The ChatConsumer instance.
            close_code (int): The close code.
        
        Returns: None
        """

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
        self.room.users_remove(self.scope["user"])
        self.send_leave_notification()
        self.send_user_list()

    def receive(self, text_data):

        """
        Receives a message from the user and broadcasts it to the 
        chat room. 

        Args:
            self (ChatConsumer): The ChatConsumer instance.
            text_data (str): The message data.
        
        Returns: None
        """
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message")
        username = self.scope["user"].username

        if message:
            ChatMessage.create(room=self.room, user=self.scope["user"], message=message)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name, {
                    "type": "chat.message",
                    "message": message,
                    "username": username
                }
            )

    def send_recent_messages(self):

        """
        Sends the most recent messages to the user (up to 3 
        messages).

        Args:
            self (ChatConsumer): The ChatConsumer instance.
        
        Returns: None
        """


        recent_messages = self.room.fetch_messages()[:3]
        messages = [
            {
                'username': msg.user.username,
                'message': msg.message,
                'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            }
            for msg in recent_messages
        ]
        self.send(text_data=json.dumps({
            'type': 'recent_messages',
            'messages': messages
        }))

    def send_user_list(self):

        """
        Sends the list of users in the chat room to the user.

        Args:
            self (ChatConsumer): The ChatConsumer instance.
        
        Returns: None
        """

        users = [user.username for user in self.room.fetch_users()]
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'user_list_update',
                'users': users
            }
        )

    def send_join_notification(self):

        """
        Sends a notification to the chat room when a user joins.

        Args:
            self (ChatConsumer): The ChatConsumer instance.

        Returns: None
        """

        username = self.scope["user"].username
        join_message = f"{username} has joined the chat"

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                "type": "chat.message",
                "message": join_message,
                "username": "System"
            }
        )

    def send_leave_notification(self):

        """
        Sends a notification to the chat room when a user leaves.

        Args:
            self (ChatConsumer): The ChatConsumer instance.

        Returns: None
        """

        username = self.scope["user"].username
        leave_message = f"{username} has left the chat"
        print("LEAVE MESSAGE", leave_message)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                "type": "chat.message",
                "message": leave_message,
                "username": "System"
            }
        )

    def chat_message(self, event):

        """
        Sends a chat message to the user.

        Args:
            self (ChatConsumer): The ChatConsumer instance.
            event (dict): The event data.
        
        Returns: None
        """

        message = event["message"]
        username = event.get("username", "Anonymous")

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            "message": message,
            "username": username
        }))

    def user_list_update(self, event):

        """
        Sends an updated user list to the user.

        Args:
            self (ChatConsumer): The ChatConsumer instance.
            event (dict): The event data.
        
        Returns: None
        """

        users = event['users']
        self.send(text_data=json.dumps({
            'type': 'user_list',
            'users': users
        }))
