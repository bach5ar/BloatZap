# Bloatzap
It sounds like you're looking to create a Python script that automates the installation of ADB (Android Debug Bridge) on Linux, followed by using ADB commands to uninstall bloatware and optimize settings on an Android device. 
# Android Bloatware Remover using ADB

This project aims to automate the removal of bloatware apps from an Android device using ADB (Android Debug Bridge) commands.

## Project Overview

Android devices often come with pre-installed bloatware apps that users may not need or want. This project provides a Python script that utilizes ADB commands to identify and uninstall bloatware apps from the device.

## Features

- Automated installation of ADB tools.
- Detect connected devices.
- List installed packages.
- Compare installed packages with a list of known bloatware apps.
- Uninstall bloatware apps using ADB commands.

## Getting Started

1. Install python on your linux machine.
   ```bash
    sudo apt update
    sudo apt install python3
    ```
2. Clone this repository to your local machine.
    ```bash
   git clone https://github.com/bach5ar/BloatZap.git
   ```

4. Run the Python script:

    ```bash
   python3 Bloatzap.py
    ```

5. Follow the instructions provided by the script.

## Configuration

- Edit the `bloatware_packages.txt` file to customize the list of known bloatware apps.

## Contributors

- [bachar bejaoui](https://github.com/bach5ar)

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify and improve this template according to your project's needs. You can add sections like "Usage," "Troubleshooting," "Future Enhancements," etc., to provide more detailed information to users.

Remember to create a `LICENSE` file in your repository with the actual license text if you're using a specific open-source license. Additionally, provide appropriate attribution for any code or resources you've used in your project.
