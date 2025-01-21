import subprocess
import platform

def ping(host):
    # Determine the parameter for the operating system
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    # Build the ping command
    command = ['ping', param, '4', host]  # Ping 4 packets (you can adjust this)
    
    try:
        # Run the command
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Success: {host} is reachable.")
    except subprocess.CalledProcessError:
        print(f"Error: {host} is not reachable.")

# Example usage: ping a machine by IP or hostname
host_1 = '192.168.0.102'  # Replace with your target IP or hostname
host_2 = '10.51.16.172'  # Replace with your target IP or hostname
host_3 = '169.254.22.125'  # Replace with your target IP or hostname
host_4 = '192.168.1.1'  # Replace with your target IP or hostname

ping(host_1)
ping(host_2)
ping(host_3)
ping(host_4)