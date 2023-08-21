import html

class commentsystem:
    def __init__(self):
        self.comments = []

    def add_comment(self, username, text):
        escaped_username = html.escape(username)
        escaped_text = html.escape(text)
        self.comments.append({'username': escaped_username, 'text': escaped_text})

    def display_comments(self):
        for comment in self.comments:
            print(f"Username: {comment['username']}")
            print(f"Comment: {comment['text']}")
            print()

# Create an instance of CommentSystem
comment_system = commentsystem()

# Simulate adding comments
comment_system.add_comment('Bala', '<script>alert("Malicious code");</script>')
comment_system.add_comment('Bob', 'This is a harmless comment.')

# Display comments
comment_system.display_comments()
