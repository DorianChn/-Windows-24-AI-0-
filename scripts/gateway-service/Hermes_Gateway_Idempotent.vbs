' Hermes_Gateway_Idempotent.vbs
' 幂等启动 Gateway — 已有实例则跳过，防止双实例
' 放到: %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\

Dim objWMI, colProcesses, objProcess
Dim objShell
Dim found

Set objWMI = GetObject("winmgmts:\\.\root\cimv2")
Set colProcesses = objWMI.ExecQuery("SELECT * FROM Win32_Process WHERE Name='python.exe'")

found = False
For Each objProcess in colProcesses
    If InStr(objProcess.CommandLine, "gateway run") > 0 Then
        found = True
        Exit For
    End If
Next

If Not found Then
    Set objShell = CreateObject("WScript.Shell")
    objShell.Run "python -m hermes gateway run", 0, False
End If
