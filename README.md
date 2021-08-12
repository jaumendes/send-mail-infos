>> Script to read a file (plano.txt) with alibaba links and create a price control report, to send via email every day

# send-mail-infos


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

