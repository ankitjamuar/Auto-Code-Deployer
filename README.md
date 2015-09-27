# Auto-Code-Deployer
A flask app that will auto deploy code from Bitbucket when ever a code is pushed to Master branch

Note: For this app to auto pull commits from Bitbucket you need to take care of following things:
 
 Since Webhook App is running via uwsgi which in turn has USER "www-data" , we need to add SSH key for this user to Bitbucket
 STEP 1: Login as www-data   sudo su -s /bin/bash www-data
 STEP 2: Generate SSH keys and addd to sssh -agent and then copy the key to bitbucket Account
         Follow the process from here  https://help.github.com/articles/generating-ssh-keys/
Few things to note  the key pair you generate will spit these two file "id_rsa", "id_rsa.pub" make sure the name are same since git command will search file with same name 
Directory Structure:  owner and group of www and its internal folders are  sudo chown www-data:www-data -R /var/www
/var/www/.ssh/
	id_rsa.pub
	id_rsa
