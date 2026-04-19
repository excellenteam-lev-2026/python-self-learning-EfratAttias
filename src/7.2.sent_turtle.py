class PostOffice:
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}
        
    def send_message(self, sender, recipient, message_body, urgent=False):
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id
    
    def read_inbox(self, username, n):
        '''Returns the n most recent messages in the user's inbox and marking them as read.
        
        Args:
            username: The user whose inbox to read.
            n: The number of messages to read. If n is 0, read all messages.

        Returns:
            A list of messages, where each message is a dictionary with keys 'id', 'body

        Raises:
            KeyError: If the username is not found in the PostOffice.

        Example:
            po_box = PostOffice(['a', 'b'])
        '''

        if username not in self.boxes:
            raise KeyError(f"User {username} not found.")
        
        to_read = self.boxes[username]
        messages = to_read[:n] if n else to_read

        for message in messages:
            message['read'] = True

        return messages

    
    def search_inbox(self, username, string):
        '''
        Returns a list of messages in the user's inbox that contain the given string in their body.
        
        Args:
            username: The user whose inbox to search.
            string: The string to search for in the message bodies.
            
        Returns:
            A list of messages that contain the string in their body.

        Raises:            
            KeyError: If the username is not found in the PostOffice.

        Example:
            po_box = PostOffice(['a', 'b'])
        '''
        if username not in self.boxes:
            raise KeyError(f"User {username} not found.")
        return [message for message in self.boxes[username] if string in message['body']]


def sent_turtle():
    '''A simple test of the PostOffice class.'''
    po_box = PostOffice(['a', 'b'])
    po_box.send_message('a', 'b', 'Hello!')
    print(po_box.read_inbox('b', 1))  
    print(po_box.search_inbox('b', 'Hello'))

if __name__ == "__main__":
    '''Run the sent_turtle function to test the PostOffice class.'''
    print(sent_turtle())

