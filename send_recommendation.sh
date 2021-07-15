# 15 07 2021
# jaumendes @ zap

set -x
start_time="$(date -u +%s)"






elap1="$(date -u +%s)"

metricsFile='/opt/send-mail-infos/metrics'-$(date +'%Y%m%d')'.xlsx'
# RUN CALCULATIONS
#

sudo chmod 777 $metricsFile
elap2="$(date -u +%s)"



# SEND EMAIL
sudo swaks --to jaumendes101@gmail.com --header "Subject: Report AliExpress - $(date)" --body "$start_time" --attach /opt/send-mail-infos/plano.txt --attach $metricsFile --attach-type text/html --attach-body /opt/send-mail-infos/templates/hello.html  -tls

checkpoint="$(($elap2-$elap1))"


end_time="$(date -u +%s)"

elapsed="$(($end_time-$start_time))"

echo "It took $elapsed seconds to complete this Job!..."
