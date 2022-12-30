# SAP_RFC
  
Módulo para conectarse a SAP mediante RFC y ejecutar funciones  

*Read this in other languages: [English](Manual_SAP_RFC.md), [Español](Manual_SAP_RFC.es.md).*
  
![banner](imgs/Banner_SAP_RFC.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Conectarse a SAP
  
Se conecta SAP por RFC
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la conexion|Nombre de la conexion a SAP|test|
|App Server Host|Host del servidor de aplicaciones|20.20.40.3|
|Cliente|Cliente de SAP|400|
|Usuario|Usuario de SAP|User 1|
|Contraseña|Contraseña de SAP|)xV3-r9=c_|
|Numero de sistema|Numero de sistema de SAP|01|
|Idioma|Idioma de SAP|EN|
|SAP Router|SAP Router|/H/13.157.33.21|
|ID de sistema|ID de sistema de SAP|PROD|
|Resultado|Variable donde se guardara el resultado de la conexion|res|

### Ejecutar funcion
  
Ejecuta una funcion usando RFC
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la funcion|Nombre de la funcion a ejecutar|var|
|Tabla de parametros|Tabla de parametros de la funcion||
|Resultado|Variable donde se guardara el resultado de la conexion|var|
