import base64
import requests

class ContentManager:
    def __init__(self, owner, repo):
        self.owner = owner
        self.repo = repo
        
    def create_file(self, path, content, message="Add file", branch="main"):
        """Create a new file in the repository."""
        try:
            # Encode content
            content_bytes = content.encode('utf-8')
            encoded_content = base64.b64encode(content_bytes).decode('utf-8')
            
            # Prepare request data
            data = {
                'message': message,
                'content': encoded_content,
                'branch': branch
            }
            
            return data
            
        except Exception as e:
            print(f"Error creating file: {str(e)}")
            raise
