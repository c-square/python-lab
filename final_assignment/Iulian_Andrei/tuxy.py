#!/usr/bin/env python
# *-* coding: UTF-8 *-*
 
"""
Tuxy își dorește un sistem care să automatizeze instalării unui proiect
pe infrastructura din `TuxyLand`.
 
Acest proiect de automatizare va primi un fișier de configurare ce va
conține toate instrucțiunile necesare pentru pregătirea mediului ideal
în care va rula `TuxyApp`.
 
Un exemplu de fișier de configurare ar putea fi:
 


{
    "before_install": [
        {
            "download": {
                "source": "https://localhost/file",
                "destination": "/home/alex/script.sh",
            }
        },
    ],
    "install": [
        {
            "run_script": {
                # How many times to retry running the command.
                "attempts": 3,
                # Single bool, int, or list of allowed exit codes.
                "check_exit_code": True,
                # The command passed to the command runner.
                "command": "bash /home/alex/script.sh",
                # Set the current working directory
                "cwd": "/home/alex/",
                # Environment variables and their values that
                # will be set for the process.
                "env_variables": {"tuxy": "Tuxy Pinguinescu"},
                # Interval between execute attempts, in seconds.
                "retry_interval": 3,
                # Whether or not there should be a shell used to
                # execute this command.
                "shell": True,
            },
            # ...
        }
    ],
    "after_install": [
        {
            "reboot": {
                "method": "soft",
            }
        }
    ],
 
    "install_failed": [
        {
            "delete": {
                "method": "force",
                "path": "/home/alex"
            },
        },
        {
            "shutdown": {
                "method": "hard",
            },
        },
    ],
    "config": {
        "hostname": "TuxyNode-1",
        "users": {
            "acoman": {
                "full_name": "Alexandru Coman",
                "primary-group": "admin",
                "groups": ["users"],
                "expiredate": "2016-09-01",
                "password": ""
            },
            # ...
        },
        "write_files": {
            0: {
                "path": "/home/alex/test",
                "permissions": "0555",
                "encoding": "gzip",
                "content": "",
            },
            # ...
        },
    }
}
 
Trebuie să dezvoltați o aplicație care să primească un fișier de
configurare și să rezolve toate sarcinile precizate în acesta.
 
La sfârșit va trebui să ofere un fișier build.log care să descrie
toate lucrurile care s-au întâmplat.
"""


import os
import json
import time


def main():
    
    try:
        with open('config.tuxy') as config_file:
            data = json.load(config_file)
        config_file.close()
    except IOError:
        print "Error reading file!"
        return
    
    if 'before_install' in data.keys():
        os.system('echo "Running before install script..." >> info.log')

        command = data['before_install']
        for index in range(len(command)):
            command = command[0]
            command = command['download']
            source = command['source']
            destination = command['destination']
            file_name = os.path.basename(destination)
            print "File name: ", file_name
            path = os.path.dirname(destination)
            path += "/"
            print "The path param is: ", path
            command = "./before_install.sh " + source + " " + path + " " + file_name
            print "Command is: ", command
            os.system(command)

    if 'install' in data.keys():
        pass

    if 'after_install' in data.keys():
        print "YAY!"
    if 'install_failed' in data.keys():
        print "YAY!"
    if 'config' in data.keys():
        print "YAY!"

if __name__ == "__main__":
    main()

