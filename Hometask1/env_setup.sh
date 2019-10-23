#!/usr/bin/bash

sudo apt-get update

# dependencies for wsl
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev

# pyenv
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
echo '
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
' >> ~/.bashrc
source ~/.bashrc

pyenv install 2.7.17
pyenv install 3.7.4

# pyenv-virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

# pip + virtualenv
sudo apt install -y python-pip python3-pip python-virtualenv python3-virtualenv

# make environments
pyenv virtualenv 2.7.17
pyenv virtualenv 3.7.4

mkdir venv2.7 && echo "Virtualenv directory" > venv2.7/README
mkdir venv3.7 && echo "Virtualenv directory" > venv3.7/README

virtualenv --prompt="2.7.17" venv2.7
virtualenv --prompt="3.7.4" venv3.7virt


