![Static Badge](https://img.shields.io/badge/release-v1.0-blue?style=flat)
![Static Badge](https://img.shields.io/badge/Windows-passing-brightgreen?style=flat&logo=Windows)
![Static Badge](https://img.shields.io/badge/Linux-passing-brightgreen?style=flat&logo=Linux)
![Static Badge](https://img.shields.io/badge/macOs-passing-brightgreen?style=flat&logo=macOs)
![Static Badge](https://img.shields.io/badge/License-GPL--3.0-orange?style=flat)

# sshBruteForce-Python

This is a simple python script to bruteforce ssh server. It's really not optimized and really not made to bruteforce real ssh server. **Really the law does not differentiate between involuntary attacks and intentional attacks.**

## Requirements

To use this keylogger, you need to install the `paramiko` package. You can install it using pip:

```
pip install paramiko
```

## SSH BruteForce Configuration Parameters

This script allows you to configure various parameters for the keylogger functionality.

- **HOST** : The IP address of the server you want to attack.
- **USERS_LIST** : Either a list of usernames or a file that contain a list of usernames.
- **PASSWORDS_LIST** : Either a list of passwords or a file that contain a list of passwords.
- **CONTINUE_ON_SUCCESS** : If you want to stop at the first user that work or want to have other user.
- **SAVE_FAIL** : If you want to save all attempts in a file.
- **SAVE_FAIL_FILE** : The name of the file that save all attempts.
- **SAVE_SUCCESS** : If you want to save all success in a file.
- **SAVE_SUCCESS_FILE** : The name of the file that save all success.


## Disclaimer

**This project is intended for educational and research purposes only. The author does not condone any illegal use of this software. Be responsible and respect the privacy and rights of others. You are warned the law is strict about this.**
