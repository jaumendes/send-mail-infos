>> Script to read a file (plano.txt) with alibaba links and create a price control report, to send via email every day

# CENT OS INSTALL#

yum -y update

yum install swaks 

yum install python3

yum -y install python-pip


pip3 install requests pandas xlsxwriter

locale

cd /opt

git clone  https://github.com/jaumendes/send-mail-infos.git

cd /opt/send-mail-infos

sudo python3 get_recommendation.py plano.txt

sudo sh send_recommendation.sh


# WINDOWS INSTALL

PS> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

PS> choco install python3 --pre 

PS> choco install python-pip3

PS> pip3 install requests pandas xlsxwriter

# CRONTAB #

crontab -l

crontab -e 


8 * * * * sh /opt/send-mail-infos/send_recommendation.sh

cat /etc/crontab

