import subprocess

def install_adb():
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'install', 'adb', '-y'])

def device_connect():
    while True:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        output = result.stdout.strip()
        if "List of devices attached" in output:
            break
        print("Waiting for device to connect...")

def packages_number():
    command = "adb shell pm list packages"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output_lines = result.stdout.splitlines()
   

    package_count = len(output_lines)
    print("Number of packages:", package_count)
    with open("bloatware_packages.txt", "r") as file:
        bloatware_packages = [f"{line.strip()}" for line in file.readlines()]

    num_bloatware_found = 0
    for package in output_lines:
        if any(bloatware in package for bloatware in bloatware_packages):
            num_bloatware_found += 1
            print("Number of bloatware packages found:170/", num_bloatware_found)

        
    for package in output_lines:
        if any(bloatware in package for bloatware in bloatware_packages):
            num_bloatware_found += 1
            package_name = package.split(":")[1]
            print(f"Uninstalling {package_name}...")
            command = f"adb shell pm uninstall -k --user 0 {package_name}"
            subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    command = "adb shell pm list packages"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output_lines = result.stdout.splitlines()
    num_bloatware_found = 0
    for package in output_lines:
        if any(bloatware in package for bloatware in bloatware_packages):
            num_bloatware_found += 1

    print("Number of bloatware packages after unistalling:170/", num_bloatware_found)

install_adb()
device_connect()
packages_number()
