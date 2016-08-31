# /bin/bash
for pid in $(ps aux|grep blogserver.py | awk '{print $2}')
do
sudo kill -9 $pid
done
sudo nohup python blogserver.py &
