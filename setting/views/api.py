import socket
from django.shortcuts import redirect


# 重啟伺服器

def post_restart_service(request):
    if request.method == 'POST':
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_client.connect(('192.168.77.78', 8000))
        message = b'restart service'
        message = bytes(f"{len(message):<20}", 'utf-8') + message
        socket_client.send(message)
        return redirect('news:setting')
