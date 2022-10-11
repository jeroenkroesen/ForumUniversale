# Sass install on ubuntu

## Install Dart
Links:
* [Lindevs guide](https://lindevs.com/install-dart-on-ubuntu/)
* [Official Dart](https://dart.dev/get-dart#install-using-apt-get)

```bash
# Download gpg key
sudo wget -qO /etc/apt/trusted.gpg.d/dart_linux_signing_key.asc https://dl-ssl.google.com/linux/linux_signing_key.pub
#  Add repo
sudo wget -qO /etc/apt/sources.list.d/dart_stable.list https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list
# Update repo list
sudo apt update
# install dart
sudo apt install dart
# Disable analytics
dart --disable-analytics
```

## Install Sass
```bash
# Install Sass via dart
dart pub global activate sass
# Or possibly sudo is required
sudo dart pub global activate sass
```
