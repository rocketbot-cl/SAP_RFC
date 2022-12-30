# SAP_RFC
  
Module to connect to SAP using RFC and execute functions  

*Read this in other languages: [English](Manual_SAP_RFC.md), [Español](Manual_SAP_RFC.es.md).*
  
![banner](imgs/Banner_SAP_RFC.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  


## How to use this module
In order to use the SAP_RFC module we must take into account that the server where the functions are going to be executed through RFC are active and working correctly. Take into account all the data to make the connection to SAP, as well as the user, password, SAP Router and other necessary inputs.



## Description of the commands

### Connect to SAP
  
Connects to an SAP instance via RFC
|Parameters|Description|example|
| --- | --- | --- |
|Connection name|Connection name. Can be any name|test|
|App Server Host|IP address of the application server|20.20.40.3|
|Client|Client number|400|
|User|User name|User 1|
|Password|User password|)xV3-r9=c_|
|System Number|System number|01|
|Language|System language. By default is EN|EN|
|SAP Router|IP address of the SAP router|/H/13.157.33.21|
|System ID|System ID. By default is PROD|PROD|
|Result|Result of the connection. Returns True if the connection was successful|res|

### Execute function
  
Executes a function using RFC taking into account the input parameters. Returns the output parameters after execution.
|Parameters|Description|example|
| --- | --- | --- |
|Function name|Name of the function to execute|var|
|Parameters Table|Input parameters table|input|
|Result|Name of the variable where the result will be stored. Return output parameters|var|
