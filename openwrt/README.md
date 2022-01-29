
## onerng @ openwrt

```
opkg install rng-tools at coreutils-nohup python-pip gnupg kmod-usb-acm

pip install python-gnupg

cp onerng.sh /sbin
cp onerng_verify.py /sbin
cp 79-onerng.rules /etc/udev/rules.d

udevadm control --reload

```

### running by hand

```
/sbin/onerng.sh daemon ttyACM0
```
```
rngd -f -n 1 -d 1 -r /dev/stdin
```
