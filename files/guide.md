# The Guide for development a Data Collection System
##  1. Raspberry Pi
![alt text](image-1.png)  
__Figure 1.__ The pin diagram of the Raspberry Pi 3B+.  
![alt text](image-2.png)  
__Figure 2.__ The Raspberry Pi back image (SD card slot).
## 2. Ubuntu-Operation System(OS)
__NOTE 1:__ I have already assisted you in installing the Ubuntu OS, necessary Python packages and starting the SSH server as well as setting the WiFi setup. You can now access the Ubuntu OS directly via __XSHELL__ software.  
- __Ubuntu:__  
    - username = ubuntu      
    - password = ubuntugtiit
- __WiFi:__  
    - username = ubuntu
    - password = 88888888

__NOTE 2:__ Enable the mobile hotspot on your computer and configure the username and password as specified in NOTE 1. You will use the Raspberry Pi's IP address, which you can find here, for SSH remote access.
### 2.1. XSHELL
__Purpose:__ Remote login to the Raspberry Pi Ubuntu OS using the SSH protocol via [XSHELL](https://cdn.netsarang.net/8480c912/Xshell-8.0.0063p.exe) software.  
__HowToUse:__   
- __Step 1:__ Install the XSHELL software on Windows (Alternatively, you can use other SSH software for remote login).  __Omitted!__
- __Step 2:__ *打开XSHELL软件* - *文件* - *新建* - *名称(N): (任意填写)* - *协议(P): (SSH)* - *主机(H): (在电脑热点设置中，查看树莓派IP地址)* - *(端口号(O): 22)*
- __Step 3:__ *点击用户身份验证* - *填写用户名和密码(参考NOTE 1: Ubuntu)* - *点击连接*  
### 2.2. Download Project via Git  
__Git:__ Enter the command in the XSHELL - 本地Shell interface.  
- cd /  
- cd /usr/local/  
- sudo mkdir project  
- git clone https://github.com/bslbschef/ISEC2024-Final-Project  
- cd ISEC2024-Final-Project
## 3. Humidity sensor (DHT22)