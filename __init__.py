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
import os, re

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")
global string_connection

def clean_rfc_json(text):
    """
    Limpia JSON proveniente de SAP RFC.
    Recibe el text crudo, retorna un string JSON limpio.
    Funciona con dict o lista.
    """
    global _clean_array
    
    import re
    import json
    
    try:
        json.loads(text)
        return text
    except (json.JSONDecodeError, ValueError):
        pass
    
    stripped = text.strip()
    
    if stripped.startswith('{') and '[' in stripped:
        # Es un dict que puede tener arrays embebidos como string
        # Extraer arrays embebidos y limpiarlos
        def clean_embedded_array(match):
            global _clean_array
            key = match.group(1)
            arr_str = match.group(2)
            cleaned = _clean_array(arr_str)
            return '"{}": {}'.format(key, cleaned)
        
        # Buscar "KEY": "[{...}]" (array como string) o "KEY": [{...}] (array directo)
        # Primero intentar con array como string
        result = re.sub(
            r'"([^"]+)"\s*:\s*"(\[.*?\])"',
            clean_embedded_array,
            stripped,
            flags=re.DOTALL
        )
        
        # También limpiar arrays directos
        result = re.sub(
            r'"([^"]+)"\s*:\s*(\[[^\]]*\[.*?\])',
            clean_embedded_array,
            result,
            flags=re.DOTALL
        )
        
        try:
            json.loads(result)
            return result
        except:
            pass
    
    if stripped.startswith('[') or (stripped.startswith('{') and '":{' not in stripped):
        return _clean_array(stripped)
    
    return text


def _clean_array(text):
    """Limpia un array o serie de objetos JSON con comillas rotas."""
    import re
    import json
    raw_objects = re.findall(r'\{[^{}]+\}', text)
    
    cleaned = []
    for obj_str in raw_objects:
        inner = obj_str.strip('{}')
        fields = inner.split('","')
        
        clean_obj = {}
        for field in fields:
            parts = field.split('":"', 1)
            if len(parts) == 2:
                key = parts[0].strip('" ').replace('\\', '')
                value = parts[1].strip('" ')
                value = value.replace('"', '').replace('\\', '')
                clean_obj[key] = value
        
        if clean_obj:
            cleaned.append(clean_obj)
    
    return json.dumps(cleaned, ensure_ascii=False)




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
        name = name.replace(" ", "_")
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
        text = False
        FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
        executable_path = base_path + "modules" + os.sep + "SAP_RFC" + os.sep + "libs" + os.sep
        executable = executable_path + "sap_rfc.exe "
        parameters_connection_string = ""
        for table in parameters['table']:
            value = rocketbot.replaceByVar(vars_, table['value'])
            # print(value)
            
            if " " in value:
                table['value'] = "\"" + value + "\""
            parameters_connection_string += table['name'] + "=" + value + ","
        
        args = string_connection + " {function_name} {parameters}".format(function_name=function_name, parameters=parameters_connection_string[:-1])
        print("args: ", args)
        pipe = Popen(executable+args, stdout=PIPE, shell=True)
        res = pipe.communicate()
        # print(res)
        try:
            text = res[0].decode('utf-8')
        except:
            text = res[0].decode('latin-1')


        if "ErrorMessage" in text:
            print(text)
            error_text = text.split("ErrorMessage: ")[1].split("\n")[0]
            raise Exception(error_text)

        text = text.replace("\r\n","")
        text = re.sub(r'(\d)"(\s)', r'\1in\2', text)

        
        for i in range(10):
            try:
                text_json = json.loads(text)
                break
            except json.JSONDecodeError as e:
                pos = e.pos
                print(pos, repr(text[e.pos - 2: e.pos + 4]))
                text = text[:e.pos - 2] + text[e.pos - 2: e.pos + 2].replace('"', '') + text[e.pos +2:]
                text = clean_rfc_json(text)
                rocketbot.log("Reintento eliminando comillas: " + str(i) )

        else:
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