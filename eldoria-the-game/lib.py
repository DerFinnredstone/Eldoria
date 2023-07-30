import subprocess

#def

#start.py

def start_command():
    # Führe den Befehl aus und erhalte den Output
    cmd = ["python main.py"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, _ = process.communicate()

    # Konvertiere den Output in einen Byte-String und gib ihn aus
    if isinstance(output, bytes):
        print(output.decode("utf-8"))
    else:
        print(output)

#var

#
