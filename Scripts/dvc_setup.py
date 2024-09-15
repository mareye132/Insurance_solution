import os
import subprocess

class DVCSetup:
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def install_dvc(self):
        """Install DVC using pip"""
        subprocess.run(["pip", "install", "dvc"], check=True)
        print("DVC installed successfully.")

    def initialize_dvc(self):
        """Initialize DVC in the current project"""
        subprocess.run(["dvc", "init"], check=True)
        print("DVC initialized successfully.")

    def setup_remote(self):
        """Set up local storage for DVC and configure remote"""
        # Create local storage directory
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)
            print(f"Storage directory created at: {self.storage_path}")
        
        # Add DVC remote storage
        subprocess.run(["dvc", "remote", "add", "-d", "localstorage", self.storage_path], check=True)
        print("Remote storage configured.")

    def add_data(self, data_file):
        """Add data to DVC for version control"""
        subprocess.run(["dvc", "add", data_file], check=True)
        print(f"Data file {data_file} added to DVC.")

    def commit_changes(self, commit_message):
        """Commit changes to Git repository"""
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"Changes committed with message: {commit_message}")

    def push_data(self):
        """Push data to DVC remote storage"""
        subprocess.run(["dvc", "push"], check=True)
        print("Data pushed to remote storage.")

# Example usage:
if __name__ == "__main__":
    # Define the path to local storage
    local_storage_path = '/path/to/your/local/storage'
    
    # Initialize DVCSetup class with storage path
    dvc_setup = DVCSetup(local_storage_path)

    # Step 1: Install DVC
    dvc_setup.install_dvc()

    # Step 2: Initialize DVC
    dvc_setup.initialize_dvc()

    # Step 3: Set up local remote storage
    dvc_setup.setup_remote()

    # Step 4: Add a data file to DVC
    dvc_setup.add_data('C:/Users/user/Desktop/Github/InsuranceData_analysis/Insurance_solution/MachineLearningRating_v3.txt')  # Replace with the actual data file

    # Step 5: Commit changes to version control
    dvc_setup.commit_changes('Added data.txt to DVC tracking')

    # Step 6: Push data to local remote storage
    dvc_setup.push_data()
