# Auto-Code-Deployer
A flask app that will auto deploy code from Bitbucket when ever a code is pushed to Master branch
<br><br>
Note: For this app to auto pull commits from Bitbucket you need to take care of following things:
 <br>
 Since Webhook App is running via uwsgi which in turn has USER "www-data" , we need to add SSH key for this user to Bitbucket.<br>
 STEP 1: Login as www-data   sudo su -s /bin/bash www-data<br>
 STEP 2: Generate SSH keys and addd to sssh -agent and then copy the key to bitbucket Account<br>
         Follow the process from here  https://help.github.com/articles/generating-ssh-keys/<br><br>
Few things to note  the key pair you generate will spit these two file "id_rsa", "id_rsa.pub" make sure the name are same since git command will search file with same name <br><br>
Directory Structure:  owner and group of www and its internal folders are  <br>
```
sudo chown www-data:www-data -R /var/www
```

```
/var/www/.ssh/<br>
	id_rsa.pub
	id_rsa
```
