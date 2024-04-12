# How to store the logs

Rotate the logs every minute
```
*/1 * * * * /etc/cron.daily/logrotate
```
## Testing environment
```
# https://github.com/minio/minio-service/blob/master/linux-systemd/minio.service
cd /usr/local/bin
wget https://dl.min.io/server/minio/release/linux-amd64/minio
chmod +x minio
./minio server /tmp/logs
```
