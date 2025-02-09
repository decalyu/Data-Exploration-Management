def download_from_hpc(hpc_file, local_path):
    """
    Simulates downloading a file from an HPC system using SCP.

    :param hpc_file: Path of the file on the HPC system.
    :param local_path: Destination path on the local machine.
    """
    command = f"scp username@hpc.server:{hpc_file} {local_path}"
    print(f"Simulated Download Command: {command}")

# Example usage
download_from_hpc("/home/username/data/titanic.csv", "./")
