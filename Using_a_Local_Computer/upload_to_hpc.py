def upload_to_hpc(local_file, hpc_path):
    """
    Simulates uploading a file to an HPC system using SCP.

    :param local_file: Path of the file on the local machine.
    :param hpc_path: Destination path on the HPC system.
    """
    command = f"scp {local_file} username@hpc.server:{hpc_path}"
    print(f"Simulated Upload Command: {command}")

# Example usage
upload_to_hpc("titanic.csv", "/home/username/data/")
