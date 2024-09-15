import os
import subprocess

def setup_dvc():
    # Initialize DVC
    subprocess.run(['dvc', 'init'], check=True)

    # Add local remote storage
    local_storage = "C:/Users/user/Desktop/Github/storage"
    subprocess.run(['mkdir', '-p', local_storage], check=True)
    subprocess.run(['dvc', 'remote', 'add', '-d', 'localstorage', local_storage], check=True)

    # Add dataset to DVC tracking
    dataset_path = "C:/Users/user/Desktop/Github/Insurance_solution/data/MachineLearningRating_v3.txt"
    subprocess.run(['dvc', 'add', dataset_path], check=True)

    # Push data to the local remote storage
    subprocess.run(['dvc', 'push'], check=True)

    print("DVC setup complete and data pushed to local remote storage.")

if __name__ == "__main__":
    setup_dvc()
