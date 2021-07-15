# 15 07 2021
# jaumendes @ zap

set -x
start_time="$(date -u +%s)"


# COPY FILE FROM EDIT MODE TO EXEC MODE
#cp E:/JAM/priber2019/icons/android-icon-36x36.png /home/pb/expenses/emailpic.png

#sudo rm /home/pb/projectos/expenses/emailbody.txt

#sudo cp /mnt/e/JAM2/Transferencias/$mymonth /home/pb/projectos/expenses/$mymonth


elap1="$(date -u +%s)"

metricsFile='/opt/send-mail-infos/metrics'-$(date +'%Y%m%d')'.xlsx'
lastRecomFile='metrics'-$(date -d @$(( $(date +"%s") - 86400)) +"%Y%m%d")'.xlsx'
# RUN CALCULATIONS
#
#sudo python3 get-alibaba-metrics.py

sudo chmod 777 $metricsFile
#sudo chmod 777 /s/expenses/$lastRecomFile
elap2="$(date -u +%s)"

var1='./plano.txt'
var2= $('./$lastRecomFile')
var3= $('./$metricsFile')

varpic= "./logo.jpg"
varhtml = './templates/hello.html'



# SEND EMAIL
sudo swaks --to jaumendes101@gmail.com --header "Subject: Report AliExpress - $(date)" --body "$start_time" --attach /opt/send-mail-infos/plano.txt --attach $metricsFile  -tls

checkpoint="$(($elap2-$elap1))"

echo "It took $checkpoint seconds in calculations"

end_time="$(date -u +%s)"

elapsed="$(($end_time-$start_time))"

echo "It took $elapsed seconds to complete this Job!..."
