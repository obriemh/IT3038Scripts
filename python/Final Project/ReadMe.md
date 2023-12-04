
##Purpose
I thought this was a fun way to track the progress of each of the major UC Athletics programs as they go into their inaugural Big XII season. 
This project scrapes the data of the select athletic program and includes wins, loses, dates, times, and arenas where the event took place if provided. 
This project was designed to help me make further use of the web scraper functionality we did a few weeks back. 

##Prequesites 
This project requires the following install commands to be run:
pip install lxml
pip install beautifulsoup4
pip install pandas
pip install requests. 

Alternatively, one may choose to use Anaconda which includes those modules. 

##Running
To run the file, open a command prompt and use the cd command to change your directory to whereever the files were downloaded. Please note: The files MUST stay together. 
You will be prompted to pick one of the three major sporting events that the source website offers. Football, Men's Basketball, Women's Football. 

##Limitations
Please keep all the files in the same folder when launch. If any are moved, you will get an a missing file error. 
The source website has a webscrapping limit of 20 requests per minute. I did not run into issues with this when building the program and with the limited data, I don't think this is an issue for users of this particular application. 

Go Bearcats!
