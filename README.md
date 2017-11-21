# Projecteuler Questions Scraper
Simple python script that scrapes questions from projecteuler.net

# How to Use
* Install git (if not already installed) 

For Debian:

```bash
sudo apt-get install git 
```

For Fedora/Redhat/Centos:

```bash
sudo yum install git
```

Install `virtualenv`

```bash
sudo pip install virtualenv
```

* Clone this repo to your machine

```bash
git clone https://github.com/abhisekpadhi/projecteuler-questions-scraper.git
```

* Enter the directory and create a virtualenv

```bash
cd projecteuler-questions-scraper/ && virtualenv venv
```

* Install requirements

```bash
venv/bin/pip install -r requirements.txt
```

* Run the script 

```bash
venv/bin/python crawler.py 
```

* The output will be stored in a file named `Project-Euler-Questions.txt`

# Contributing

* Contributing to this repo is easy
* Create a branch and raise a pull request
* For feature request you can raise issues 
