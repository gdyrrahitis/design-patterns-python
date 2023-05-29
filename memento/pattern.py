class TextEditorState:
    """Memento"""
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text

class TextEditor:
    """Originator"""
    def __init__(self):
        self.text = ""

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text += text
    
    def save(self):
        return TextEditorState(self.text)
    
    def undo(self, version):
        self.text = version.get_text()

class VersionControl:
    """Caretaker"""
    def __init__(self):
        self.versions = []

    def push(self, version):
        self.versions.append(version)

    def rollback(self):
        version = self.versions.pop()
        return version
