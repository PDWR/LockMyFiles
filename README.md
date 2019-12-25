# LockMyFiles
Using AES and RSA to encrypt all files except the system files, so the computer can run normally, but the private files will be locked! Of course, you can change and select which files can be except, just only add them to WHITE_DIRS or WHITE_FILES, you can read the code, and change it!

## How to use this project

Before we starting, we need to install some packets , use the following command!

	pip install -r requirements.txt
	
First of all, we need to use pyinstaller to packet it as exe files, we need to packet 3 files they are generate_rsa_keys.py, encrypt.py, decrypt.py!

	pyinstaller -F generate_rsa_keys.py
	pyinstaller -F encrypt.py
	pyinstaller -F decrypt.py 

	Tips: only use -F argument will use the python icon and show the running windows, you can use the -i argument to change the icon and use the -w argument to display the windows!
![image](https://github.com/PDWR/LockMyFiles/blob/master/images/gen_exe_files.png)

Before encrypt the files, we need to generate the RSA public and private key. Run the generate_rsa_keys.exe is ok,and it will generate two files in this folder. It will apply the administrator privilege, that's ok, you can turn it off at generate_rsa_keys.py file.
![image](https://github.com/PDWR/LockMyFiles/blob/master/images/ask_admin_pri.png)
![image](https://github.com/PDWR/LockMyFiles/blob/master/images/gen_rsa_files.png)

### OK, the most import step is here, we need to move our rsapri.pem file out of our computer, you can move it to your server, your U-driver, your phone whatever you want, and you better make a backup, this file is the most import, if you lost it, your files can NOT be decrypted.

After that, we can running the encrypt.exe file, and it will start encrypting the files, after that, the windows will display and your files is encrypted! And it will generate a decrypt_key.txt file in the folder! This is the most import key! Don't delet it! Or you can NOT decrypt your files! No one can!
	Tips：the speed of encrypting files is depended on your CPU Cores Number! 
	
![image](https://github.com/PDWR/LockMyFiles/blob/master/images/encrypt_files.png)
![image](https://github.com/PDWR/LockMyFiles/blob/master/images/decrypt_keys.png)
![image](https://github.com/PDWR/LockMyFiles/blob/master/images/cannot_open.png)

If we wanna decrypt the files, we only need to copy our rsapri.pem to this folder, and run it, that's easy!
	Tips: change the rsa key everytime we used!
	
![image](https://github.com/PDWR/LockMyFiles/blob/master/images/decrypt_keys.png)
![image](https://github.com/PDWR/LockMyFiles/blob/master/images/file_open.png)







