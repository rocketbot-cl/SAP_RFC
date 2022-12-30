# SAP_RFC
  
Module to connect to SAP using RFC and execute functions  

*Read this in other languages: [English](Manual_SAP_RFC.md), [Español](Manual_SAP_RFC.es.md).*
  
![banner](imgs/Banner_SAP_RFC.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Connect to SAP
  
Connect to SAP using RFC
|Parameters|Description|example|
| --- | --- | --- |
|Connection name|Connection name to SAP|test|
|App Server Host|App Server Host|20.20.40.3|
|Client|SAP Client|400|
|User|SAP User|User 1|
|Password|SAP Password|)xV3-r9=c_|
|System Number|SAP System Number|01|
|Language|SAP Language|EN|
|SAP Router|SAP Router|/H/13.157.33.21|
|System ID|SAP System ID|PROD|
|Result|Variable where the result of the connection will be saved|res|

### Execute function
  
Execute a function using RFC
|Parameters|Description|example|
| --- | --- | --- |
|Function name|Function name to execute|var|
|Parameters Table|Function parameters table||
|Result|Variable where the result of the connection will be saved|var|
