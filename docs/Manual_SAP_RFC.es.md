# SAP_RFC
  
Module to connect to SAP using RFC and execute functions  

*Read this in other languages: [English](Manual_SAP_RFC.md), [Español](Manual_SAP_RFC.es.md).*
  
![banner](imgs/Banner_SAP_RFC.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  


## Como usar este modulo
Para poder usar el modulo de SAP_RFC debemos tener en cuenta que el servidor donde se vaya a ejecutar las funciones mediante RFC esten activos y funcionando de forma correcta. Tener en cuenta todos los datos para realizar la conexion a SAP, asi como el usuario, contraseña, SAP Router y demas inputs necesarios.



## Descripción de los comandos

### Conectarse a SAP
  
Se conecta a una instancia de SAP mediante RFC
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la conexion|Nombre de la conexion. Puede ser cualquier nombre|test|
|App Server Host|Dirección IP del servidor de aplicaciones|20.20.40.3|
|Cliente|Número de cliente|400|
|Usuario|Nombre de usuario|User 1|
|Contraseña|Contraseña del usuario|)xV3-r9=c_|
|Numero de sistema|Número de sistema|01|
|Idioma|Idioma del sistema. Por defecto es EN|EN|
|SAP Router|Dirección IP del router de SAP|/H/13.157.33.21|
|ID de sistema|ID del sistema. Por defecto es PROD|PROD|
|Resultado|Resultado de la conexión. Retorna True si la conexion fue exitosa|res|

### Ejecutar funcion
  
Ejecuta una funcion usando RFC teniendo en cuenta los parametros de entrada. Devuelve los parametros de salida luego de la ejecucion.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la funcion|Nombre de la funcion a ejecutar|var|
|Tabla de parametros|Tabla de parametros de entrada|input|
|Resultado|Nombre de la variable donde se almacenara el resultado. Retorna los parametros de salida.|var|
