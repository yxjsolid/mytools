#$language = "VBScript"
#$interface = "1.0"

crt.Screen.Synchronous = False

Sub Main

	do while 1
		crt.Screen.Send "iwlist ath10 scan" & chr(13)
		crt.Sleep 5000
	loop


End Sub
