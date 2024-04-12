# Firewall Configuration Directions

How to block stuff known to be bad.
Determine reasonable rules for this experiment.
```
git clone https://https://github.com/rempel1234/playground.git

# make sure the file inherits the goodies from the directory
sudo touch /usr/local/bin/blacklist.sh

sudo cp {playground/ufw,/usr/local/bin}/blacklist.sh
sudo chmod 755 /usr/local/bin/blacklist.sh

# make sure the file inherits the goodies from the directory
sudo touch /etc/cron.daily/getBlacklist
sudo cp {playground/ufw,/etc/cron.daily}/getBlacklist.sh
```
