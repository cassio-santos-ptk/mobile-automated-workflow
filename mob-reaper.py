import subprocess
import platform

# def ping(host):
#     # Determine the parameter for the operating system
#     param = '-n' if platform.system().lower() == 'windows' else '-c'
    
#     # Build the ping command
#     command = ['ping', param, '4', host]  # Ping 4 packets (you can adjust this)
    
#     try:
#         # Run the command
#         subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         print(f"Success: {host} is reachable.")
#     except subprocess.CalledProcessError:
#         print(f"Error: {host} is not reachable.")

# # Example usage: ping a machine by IP or hostname
# host_to_ping = '192.168.1.1'  # Replace with your target IP or hostname
# ping(host_to_ping)


def execute_command(command):
    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Print the command output
        print("Command Output:")
        print(result.stdout)
        
        # Print any error messages
        if result.stderr:
            print("Error Output:")
            print(result.stderr)
            
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print("Error Output:", e.stderr)

# Example: Execute a simple command
execute_command(["ls"])  # Replace with your desired command
