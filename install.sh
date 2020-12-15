#!/bin/bash
clear

cat <<"EOF"
    .&@&.             %%          .%@%           
   #@@@%           *&@@@&.         %@@@#         
  &@@&. .&@@%   .%@@@@@%/.   .%@@&. ,&@@%        
 %@@&. /@@@#  *&@@@@&&&@@@@&,  %@@&* .&@@&       
/@@@* .@@@#  &@@&(       (@@@%  #@@&, *@@@*      
%@@&. #@@&. (@@@,         ,&@@( .@@@(  &@@#      
%@@&. #@@&. /@@@,         *&@@( .@@@(  &@@#      
*@@@* .&@@#  %@@@#       %@@@#  #@@&, /@@@,      
 %@@&, *@@@%  .&@@@@@@@@@@@%. .&@@&, ,&@@%       
  %@@&*  %@@#     *#%%%#*     #@@%  *&@@%        
   (@@@&.                         .&@@&/         
     #@#                           #@#    

 _____ _       __      _      ______                      
/  ___(_)     / _|    | |     | ___ \                    
\ `--. ___  _| |_ __ _| |__   | |_/ /____      _____ _ __ 
 `--. \ \ \/ /  _/ _` | '_ \  |  __/ _ \ \ /\ / / _ \ '__|
/\__/ / |>  <| || (_| | |_) | | | | (_) \ V  V /  __/ |   
\____/|_/_/\_\_| \__,_|_.__/  \_|  \___/ \_/\_/ \___|_|   
==========================================================
EOF

print_info() {
  YELLOW='\033[0;33m'
  NC='\033[0m'
  printf "${YELLOW}[INFO]${NC}  $1\n"
}

print_error() {
  RED='\033[0;31m'
  NC='\033[0m'
  printf "${RED}[ERROR]${NC} $1\n"
}

if [ "$EUID" -ne 0 ]; then 
    print_error "Please run as root"
    exit
fi

print_info "Updating package index..."
sudo apt-get update > /dev/null 2>&1

print_info "Enabling i2c..."
sudo raspi-config nonint do_i2c 0   > /dev/null 2>&1
  
print_info "Looking for dependencies..."
# Check if git installed
if ! [ -x "$(command -v git)" ]; then
  print_info 'Git is not installed, installing...'
  apt-get install git -y  > /dev/null 2>&1
fi

# Check if pip3 installed
if ! [ -x "$(command -v pip3)" ]; then
  print_info 'Pip for python3 is not installed, installing...'
  apt-get install python3-pip -y  > /dev/null 2>&1
fi


print_info "Cloning source to /tmp/sixfab-power-api"
rm -r /tpm/sixfab-power-api > /dev/null 2>&1
git clone https://github.com/sixfab/sixfab-power-python-api.git /tmp/sixfab-power-api > /dev/null 2>&1

print_info "Installing package"
python3 /tmp/sixfab-power-api/setup.py install > /dev/null 2>&1

if [ ! -d "/opt/sixfab" ]; then
    mkdir /opt/sixfab
fi

if [ ! -d "/opt/sixfab/pms" ]; then
    mkdir /opt/sixfab/pms
fi

if [ ! -d "/opt/sixfab/pms/api" ]; then
    print_info "Downloading service source"
    git clone https://github.com/sixfab/power_distribution-service.git /opt/sixfab/pms/api > /dev/null 2>&1
    print_info "Installing service dependencies"
    pip3 install -r /opt/sixfab/pms/api/requirements.txt > /dev/null 2>&1
else
    print_info "Updating service source"
    cd /opt/sixfab/pms/api && git pull > /dev/null 2>&1 && cd - > /dev/null 2>&1
fi

if [ ! -f "/etc/systemd/system/power_request.service" ]; then

    print_info "Initializing systemd service for request service..."

    echo "[Unit]
Description=Sixfab UPS HAT Distributed API

[Service]
User=pi
ExecStart=/usr/bin/python3 /opt/sixfab/pms/api/run_server.py

[Install]
WantedBy=multi-user.target" | sudo tee /etc/systemd/system/power_request.service > /dev/null 2>&1

    print_info "Enabling and starting service."

    sudo systemctl daemon-reload
    sudo systemctl enable power_request > /dev/null 2>&1
    sudo systemctl start power_request

    print_info "Service initialized successfully."

else
    print_info "Request service installed already, restarting..."
    sudo systemctl restart power_request
fi

STATUS="$(systemctl is-active power_request.service)"
if [ "${STATUS}" = "active" ]; then
    print_info "Package installed and service running, visit http://localhost:6060/docs"
else 
    print_info "Couldn't initialize service. Please re-try"  
    exit 1  
fi