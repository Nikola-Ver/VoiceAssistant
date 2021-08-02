Set WshShell=WScript.CreateObject("WSCript.shell")
WshShell.CurrentDirectory = "C:\Program Files\VoiceAssistant"
RetCode=WshShell.Run("hiddenStart.vbs",0,False)