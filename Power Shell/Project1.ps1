#Just for context I wrote this script with the intention of using it for my upcoming server patch so the pathways in this version have been simplified. 
#The end user would need folders to match the serverlist, outfile, and filename otherwise it will not run properly. 
# Servers1.txt has my servers line by line in the .txt document. To emulate this simply add your hostname and the script will treat it like an array. 

$ServerList = Get-Content "C:\Project\Servers1.txt" 
$outfile = "C:\Project\PatchVerification.csv"
$filename = "C:\Project\PatchVerification.csv"

#This part of the script checks for an existing verification output file and deletes if it does exist. I did this to prevent confusion on my team if someone doesn't move the output file to the correct folder after validating. 

if (Test-Path $filename) {
  Remove-Item $filename
  Write-Host "Deleted the existing Server Patch Verification file." -BackgroundColor Red -ForegroundColor Black
}

#This line is for my more...impatient coworkers. We validate around ~30-40 servers so when this is used at my job it can take 5-10 minutes. 
Write-Host "Please wait while the Server Patch Verification file is generated." -BackgroundColor Red -ForegroundColor Black

#This section here really does all the work. Line one gathers the computer name from the server list which is treated like an array with one server name on each line. 
#Line 2 is Win32_QuickFixEngineering which shows a condensed update history.
#Line 3 is used to set how far back the update history goes. I usually validate 3 months to make sure the previous patches and current were applied. 
#Line 4 organized by Computer Name, Patch Description, Installation Date, the Patch ID, and lastly the boot time to make sure the server came back up after patching. 
#Line 5 creates the .csv file for my team to review after downtime patching is complete. 
ForEach($server in $ServerList){

$boottime = (Get-CimInstance -ClassName win32_operatingsystem -ComputerName $server | select csname, lastbootuptime)
Get-WmiObject Win32_QuickFixEngineering -ComputerName $Server |
Where-Object { $_.InstalledOn -gt (Get-Date).AddMonths(-24) }|
Select-Object -Property PSComputerName,Description, InstalledOn, HotFixID, @{n='Last Server Boot Time';e={$boottime}}|
Export-Csv -Path $outfile -Append
}

#Self explanatory: Just shows the process was completed. 
Write-Host "A new patch verification file has been generated in the Downtime folder. Please delete or move once validation is complete." -BackgroundColor Red -ForegroundColor Black 
