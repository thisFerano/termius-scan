

## termius-scan

Scans a ip range with a specific port and sets automatically groups and hosts in termius.

1. Set password and username
2. Set ip range(s)
3. Always find updated hosts in your termius client

## Who should use it?

- Anyone who has to setup a lot of hosts
- Anyone who uses different kind of servers or pcs

## Installation

Install the termius package

    pip install termius

Login in with your termius account

    termius login

Clone the project

    git clone https://github.com/thisFerano/termius-scan.git
    cd termius-scan

Edit main.py with your password, username, ip range and port

    password = "your_password"
    username = "your_username"
    def scanmultiple():
        scan(port, ip, range_start, range_end, group)

And run:

    py main.py

** And here you go! **

## License

termius-scan is provided under the <a href="https://github.com/thisFerano/blob/master/LICENSE">MIT license</a>

