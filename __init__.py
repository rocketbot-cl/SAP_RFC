# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "SAP_RFC" + os.sep + "libs" + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from subprocess import Popen, PIPE
import os

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")
global string_connection

if module == "connect":
    name = GetParams("name")
    app_server_host = GetParams("app_server_host")
    client_id = GetParams("client_id")
    user = GetParams("user")
    password = GetParams("password")
    system_number = GetParams("system_number")
    language = GetParams("language")
    sap_router = GetParams("sap_router")
    system_id = GetParams("system_id")
    result = GetParams("result")

    try:
        FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
        executable_path = base_path + "modules" + os.sep + "SAP_RFC" + os.sep + "libs" + os.sep
        executable = executable_path + "sap_rfc.exe "
        string_connection = "name={name},app_server_host={app_server_host},client_id={client_id},user={user},password={password},system_number={system_number},language={language},sap_router={sap_router},system_id={system_id}".format(name=name, app_server_host=app_server_host, client_id=client_id, user=user, password=password, system_number=system_number, language=language, sap_router=sap_router, system_id=system_id)
        pipe = Popen(executable+string_connection, stdout=PIPE, shell=True)
        connection_result = pipe.communicate()[0]
        print("connection_result: ", connection_result)
        text = connection_result.decode('utf-8')
        if "True" in text:
            SetVar(result, True)
    except Exception as e:
        SetVar(result, False)
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "execute_function":
    function_name = GetParams("function_name")
    parameters = eval(GetParams("iframe"))
    result = GetParams("result")
    try:
        import json
        FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
        executable_path = base_path + "modules" + os.sep + "SAP_RFC" + os.sep + "libs" + os.sep
        executable = executable_path + "sap_rfc.exe "
        parameters_connection_string = ""
        for table in parameters['table']:
            parameters_connection_string += table['name'] + "=" + table['value'] + ","
        args = string_connection + " {function_name} {parameters}".format(function_name=function_name, parameters=parameters_connection_string[:-1])
        print("args: ", args)
        pipe = Popen(executable+args, stdout=PIPE, shell=True)
        text = pipe.communicate()[0].decode('utf-8')
        if "ErrorMessage" in text:
            print(text)
            error_text = text.split("ErrorMessage: ")[1].split("\n")[0]
            raise Exception(error_text)
        text = text.replace("\r\n","")
        text_json = json.loads(text)
        for k, v in text_json.items():
            try:
                v = v.replace("\r\n","")
                v = json.loads(v)
                text_json[k] = v
            except:
                continue
        SetVar(result, text_json)
    except Exception as e:
        SetVar(result, False)
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e