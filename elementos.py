from colorama import Fore
from threading import Lock

lock = Lock()
encontrado = []

data = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

titulo = '''
▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄·     ▄▄▄   ▄▄▄·  ▄▄▄·▄▄▄▄▄      ▄▄▄  
██· █▌▐█▀▄.▀·▐█ ▀█▪    ▀▄ █·▐█ ▀█ ▐█ ▄█•██  ▪     ▀▄ █·
██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄    ▐▀▀▄ ▄█▀▀█  ██▀· ▐█.▪ ▄█▀▄ ▐▀▀▄ 
▐█▌██▐█▌▐█▄▄▌██▄▪▐█    ▐█•█▌▐█ ▪▐▌▐█▪·• ▐█▌·▐█▌.▐▌▐█•█▌
 ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀     .▀  ▀ ▀  ▀ .▀    ▀▀▀  ▀█▄▀▪.▀  ▀

'''
logo = Fore.GREEN+r'''
////////////////////////////////////////////////
//██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ██╗//
//██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗  ██║//
//██║   ██║██████╔╝██████╔╝██║██╗██║██╔██╗ ██║//
//██║   ██║██╔══██╗██╔══██╗██║██║██║██║╚██╗██║//
//╚██████╔╝██║  ██║██████╔╝╚█║████╔╝██║ ╚████║//
// ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚╝╚═══╝ ╚═╝  ╚═══╝//
////////////////////////////////////////////////
                                    +              
                                   / \
 _____        _____     __________/ o \/\_________      _________
|o o o|_______|    |___|               | | # # #  |____|o o o o  |  /\
|o o o|  * * *|: ::|. .|               |o| # # #  |. . |o o o o  | //\\
|o o o|* * *  |::  |. .| []  []  []  []|o| # # #  |. . |o o o o  | ((|))
|o o o|**  ** |:  :|. .| []  []  []    |o| # # #  |. . |o o o o  | ((|))
|_[]__|__[]___|_||_|__<|____________;;_|_|___/\___|_.|_|____[]___|   |
 FUZZING WEB  

'''

status = {
    100: "Continue: El servidor ha recibido los encabezados de la solicitud y el cliente puede continuar enviando el cuerpo de la solicitud.",
    101: "Switching Protocols: El servidor acepta cambiar el protocolo de comunicación (como de HTTP a WebSocket).",
    102: "Processing: El servidor ha recibido la solicitud, pero aún no ha terminado de procesarla (utilizado en WebDAV).",
    200: "OK: La solicitud ha sido procesada con éxito y el servidor devuelve los datos solicitados.",
    201: "Created: La solicitud ha tenido éxito y ha resultado en la creación de un recurso.",
    202: "Accepted: La solicitud ha sido aceptada, pero aún no se ha completado el procesamiento.",
    203: "Non-Authoritative Information: La respuesta contiene información no verificada proveniente de un tercero.",
    204: "No Content: La solicitud ha tenido éxito, pero el servidor no devuelve ningún contenido.",
    205: "Reset Content: Similar a 204, pero indica al cliente que debe reiniciar la vista o formulario.",
    206: "Partial Content: El servidor devuelve parte del contenido solicitado, generalmente en respuesta a solicitudes de rango.",
    300: "Multiple Choices: Hay varias opciones para el recurso solicitado y el cliente debe elegir una.",
    301: "Moved Permanently: El recurso solicitado ha sido movido de manera permanente a una nueva URL.",
    302: "Found: El recurso ha sido movido temporalmente a otra URL (usualmente se utiliza para redirecciones).",
    303: "See Other: El servidor sugiere al cliente una nueva URL para obtener el recurso usando el método GET.",
    304: "Not Modified: El recurso no ha cambiado desde la última solicitud, por lo que el cliente puede usar una versión en caché.",
    305: "Use Proxy: El recurso solicitado solo está disponible a través de un proxy.",
    307: "Temporary Redirect: Similar a 302, pero el método de la solicitud no debe cambiar (se debe usar el método original).",
    308: "Permanent Redirect: Similar a 301, pero garantiza que el método no cambie (usado en redirecciones permanentes).",
    400: "Bad Request: La solicitud contiene sintaxis incorrecta o no puede ser procesada por el servidor.",
    401: "Unauthorized: La solicitud requiere autenticación. El cliente debe autenticarse para obtener la respuesta.",
    402: "Payment Required: Este código es reservado para usos futuros (originalmente pensado para sistemas de pago).",
    403: "Forbidden: El cliente no tiene permiso para acceder al recurso solicitado, incluso si ha sido autenticado.",
    404: "Not Found: El recurso solicitado no ha sido encontrado en el servidor.",
    405: "Method Not Allowed: El método HTTP utilizado no está permitido para el recurso solicitado.",
    406: "Not Acceptable: El recurso no está disponible en el formato solicitado.",
    407: "Proxy Authentication Required: Similar a 401, pero requiere autenticación a través de un proxy.",
    408: "Request Timeout: El servidor agotó el tiempo de espera antes de recibir la solicitud completa.",
    409: "Conflict: Hay un conflicto con el estado actual del recurso (usualmente relacionado con solicitudes PUT).",
    410: "Gone: El recurso solicitado ya no está disponible y no se espera que vuelva a estarlo.",
    411: "Length Required: El servidor requiere que la solicitud incluya el encabezado Content-Length.",
    412: "Precondition Failed: Una condición en los encabezados de la solicitud no ha sido cumplida por el servidor.",
    413: "Payload Too Large: El servidor rechaza la solicitud porque el cuerpo es demasiado grande.",
    414: "URI Too Long: La URI solicitada es demasiado larga para ser procesada por el servidor.",
    415: "Unsupported Media Type: El servidor no puede manejar el tipo de medio solicitado en la solicitud.",
    416: "Range Not Satisfiable: El cliente ha solicitado una porción de un archivo que el servidor no puede proporcionar (usualmente en solicitudes de rango).",
    417: "Expectation Failed: El servidor no puede cumplir con los requisitos del encabezado Expect de la solicitud.",
    500: "Internal Server Error: El servidor encontró una condición inesperada que le impidió completar la solicitud.",
    501: "Not Implemented: El servidor no tiene soporte para la funcionalidad requerida para procesar la solicitud.",
    502: "Bad Gateway: El servidor recibió una respuesta inválida de un servidor upstream mientras actuaba como gateway o proxy.",
    503: "Service Unavailable: El servidor no está disponible, generalmente debido a sobrecarga o mantenimiento.",
    504: "Gateway Timeout: El servidor acting como gateway no recibió una respuesta a tiempo de un servidor upstream.",
    505: "HTTP Version Not Supported: El servidor no soporta la versión del protocolo HTTP utilizada en la solicitud."
}