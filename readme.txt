Quick setup — if you’ve done this kind of thing before
git@github.com:ictn-klc-2025/ictn2025.git


Get started by creating a new file or uploading an existing file. We recommend every repository include a README, LICENSE, and .gitignore.
…or create a new repository on the command line

echo "# ictn2025" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:ictn-klc-2025/ictn2025.git
git push -u origin main

…or push an existing repository from the command line

git remote add origin git@github.com:ictn-klc-2025/ictn2025.git
git branch -M main
git push -u origin main


Adding Domain Name:

A Record
Hostname:       @
Will Direct To: IP Address
TTL:            3600 (Default)


CNAME:          www
Is An Alias Of: @
TTL:            43200 (Default)

ssh root@139.59.45.199
ssh step_lab_user@139.59.45.199
step@IITD2025TH
sudo systemctl restart ictn2025

======================================
SETTING UP ROOT OS OF THE HOST
sudo apt upgrade
sudo apt install python3-pip python3-dev libpq-dev postgresql-contrib nginx certbot python3-certbot-nginx supervisor

======================================
SETUP DATABASE

sudo -u postgres psql

CREATE DATABASE ictndatabase;
CREATE USER ictndatabaseuser WITH PASSWORD 'ictndatabasepassword';
ALTER ROLE ictndatabaseuser SET client_encoding TO'utf8';
ALTER ROLE ictndatabaseuser SET default_transaction_isolation TO "read committed";
ALTER ROLE ictndatabaseuser SET timezone TO "UTC";
GRANT ALL PRIVILEGES ON DATABASE ictndatabase TO ictndatabaseuser;


sudo pip3 install --upgrade pip

=========================================
CREATE 