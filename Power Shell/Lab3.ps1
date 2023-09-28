function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}

$IP = getIP
$User = $env:Username
$ver = $PSVersionTable.PSVersion.Major
$HOSTNAME = [System.Net.Dns]::GetHostName()
$DATE = get-date


$BODY = "This machine's IP is $IP. User is $User. Hostname is $HOSTNAME. PowerShell $ver. Today's Date is $DATE."

Write-Host $body

$outlook = New-Object -ComObject Outlook.Application
$mail = $outlook.CreateItem(0)
$mail.Subject = "Lab 3 System Info"
$mail.Body = $body
$mail.Recipients.Add('obriemh@mail.uc.edu')
$mail.Send()


