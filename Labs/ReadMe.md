Lab 7 will use the PSWindowsUpdate module to help automate Windows Update and surpress the annoying reboot reminders. 
The module can be found at https://github.com/mgajda83/PSWindowsUpdate. 

To start, you will need to make sure unsigned PowerShell scripts are allowed to be ran using Set-ExecutionPolicy Unrestricted. 
Next, run Install-Module -Name PSWindowsUpdate. You will need to install an additional dependency however if the PowerShell session was ran as an Administrator you can simply select "Yes" on these prompts. 

Finally you can import the module using Import-Module -Name PSWindowsUpdate for that session. 

This can be taken even further by automating the script with Task Scheduler! I find Windows Updates to be annoying and the constant prompting is annoying when I am working on multiple things over the span of several days and may not want to reboot. 
