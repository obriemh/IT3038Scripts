#Allows execution of unsigned code. This may not be secure for all users so be cautious when executing PS scripts from unknown sources!
Set-ExecutionPolicy Unrestricted

#Installs the Windows Update PowerShell module.
Install-Module -Name PSWindowsUpdate

#THis will import the module into the current PS session. 
Import-Module -Name PSWindowsUpdate

#I have a lot of issues with Windows Updates freezing or erroring out and rather than having to manually stop or start services, this will do it for you. 
Reset-WUComponents

#This will first check for Windows Component updates such as Office 365 products. 
Get-WUList –MicrosoftUpdate

#This will install all updates and ignore prompts for a reboot. We get it Microsoft, but we can wait until we're done working. We don't need to drop everything and be bullied into rebooting. 
Install-WindowsUpdate -AcceptAll -IgnoreReboot

#This verifies the update status. 
Get-WUHistory