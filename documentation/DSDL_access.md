# How to access DSDL

## Step 1 Turn on Splunk in VMWare

### Step 1.1 Turn on Splunk VM

![VMWare Screenshot](resource/VMWare.png)

### Step 1.2 ssh into VM 

`ssh splunk_user@<ip address>`  
Password: Complex

![ssh Screenshot](resource/ssh.png)



### Step 1.3 Start Splunk Service (if VM was powered off)

`sudo /opt/splunk/bin/splunk start --run-as-root`

![Start Splunk Screenshot](resource/Start_Splunk.png)

## Step 2 Access Splunk

### Step 2.1 Open Splunk on Windows browser

Go to <ip address>:8000

![Splunk Screenshot](resource/Splunk.png)


### Step 2.2 Log into Splunk

username: splunk_user

password: Complex

![Splunk_Logon Screenshot](resource/Splunk_Logon.png)


## Step 3 Access DSDL

### 3.1 Access DSDL

![Splunk Home Page Screenshot](resource/Splunk_Homepage.png)


### 3.2 Navigate to container

Click on "Configuration" -> "container" in the left panel

![Navigation Container Screenshot](resource/DSDL_Navigation.png)



### 3.3 Spin up DSDL container

Select "Golden Image CPU" in Container Image dropdown

Click "Start"

![Configuration Container Screenshot](resource/DSDL_Config.png)

### 3.4 Access Jupyter Lab

Select "Jupyterlab"

Log in when prompted

Password: Super_Complex123

![Jupyter Lab Screenshot](resource/DSDL_login.png)


## Troubleshooting - Jupyterlab :8888 cannot be accessed

### T1 Restart docker through ssh terminal

`sudo systemctl restart docker`

### T2 Wait for a while then restart from step 3.3




