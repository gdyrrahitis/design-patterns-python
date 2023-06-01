from abc import ABC, abstractmethod

class FilesUpdater(ABC):
    """AbstractClass for Template method pattern"""
    @abstractmethod
    def download_source(self):
        pass

    @abstractmethod
    def update_files(self):
        pass

    @abstractmethod
    def validate_updates(self):
        pass

    @abstractmethod
    def save_to_disk(self):
        pass

    @abstractmethod
    def push_changes(self):
        pass

    def run(self):
        """Template method"""
        """This is the common algorithm"""
        self.download_source()
        self.update_files()
        self.validate_updates()
        self.save_to_disk()
        self.push_changes()


class S3FileUpdater(FilesUpdater):
    """Concrete class for template method"""
    def download_source(self):
        print("Downloading s3 objects")

    def update_files(self):
        print("Updating s3 objects")

    def validate_updates(self):
        print("Validate changes to s3 objects")

    def save_to_disk(self):
        """No need to implement this"""
        pass

    def push_changes(self):
        print("Uploading objects to s3")


class GitFileUpdater(FilesUpdater):
    """Concrete class for template method"""
    def download_source(self):
        print("Cloning git repository locally")

    def update_files(self):
        print("Updating git files locally")

    def validate_updates(self):
        print("Validating changes to repository files")

    def save_to_disk(self):
        print("git commit to local")

    def push_changes(self):
        print("git push to remote")
