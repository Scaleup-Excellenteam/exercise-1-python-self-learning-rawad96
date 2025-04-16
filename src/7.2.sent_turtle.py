"""
Created on Sat Apr  5 17:41:08 2025

@author: USER
"""

class PostOffice:
    """A Post Office class. Allows users to message each other.
    
    Parameters
    ----------
    usernames : list
        Users for which we should create PO Boxes.

    Attributes
    ----------
    message_id : int
        Incremental id of the last message sent.
    boxes : dict
        Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        Parameters
        ----------
        sender : str
            The message sender's username.
        recipient : str
            The message recipient's username.
        message_body : str
            The body of the message.
        urgent : bool, optional
            The urgency of the message.
            Urgent messages appear first.

        Returns
        -------
        int
            The message ID, auto incremented number.

        Raises
        ------
        KeyError
            If the recipient does not exist.

        Examples
        --------
        After creating a PO box and sending a letter,
        the recipient should have 1 messege in the
        inbox.

        >>> po_box = PostOffice(['a', 'b'])
        >>> message_id = po_box.send_message('a', 'b', 'Hello!')
        >>> len(po_box.boxes['b'])
        1
        >>> message_id
        1
        """
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

def sent_turtle_read_inbox(self, username, n=None):
    """A Method that returns the unreaded messages.

     Parameters
     ----------
     username : str
         Username whose inbox we want to read
     N : int
         Number of messages to read (optional).

     Returns
        -------
        list
           A list of messages (dicts).
     
     Raises
        ------
        KeyError
            if the user does not exist.
    """
    if username not in self.boxes:
        raise KeyError(f"User '{username}' not found")

    user_box = self.boxes[username]
    if n is None:
        messages = user_box[:]
        self.boxes[username] = []
    else:
        messages = user_box[:n]
        self.boxes[username] = user_box[n:]

    return messages


def sent_turtle_search_inbox(self, username, string):
    """A Method that return a messages list that contain the string.

        Parameters
        ----------
        username : str
            Username whose inbox we want to search
        string : str
            The search string.

        Returns
        -------
        list
           List of messages that contain the string.
     
        Raises
        ------
        KeyError
            if the user does not exist.
    """
    if username not in self.boxes:
        raise KeyError(f"User '{username}' not found")

    return [
        msg for msg in self.boxes[username]
        if string in msg.get('body', '') or string in msg.get('subject', '')
            ]

if __name__ == '__main__':
    """
    Main function
    """