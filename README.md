# FolderPermissions
A script for getting folder permissions on all sub directories of a root. Exports to CSV file

I made this purely for some work and organisation purposes to check who had access to which folders in shares. 
I could not find a similar script but also wanted to practice coding and learn.

Note - This can only be ran on local paths as I haven't included network paths yet. For example, to run this on a share on your server, you will need to login directly to the server and run the script locally using the shares local path.

RUNNING THE SCRIPT

When you run the script, it will ask you for the location you want to save the csv file. When inputting the file path DO NOT enter the final \ or /. 
Examples - C:/ should be entered as C:
         - C:/users/sjm/ should be entered asa C:/users/sjm

The next step it will ask for the root folder you want to get a list of all of the folders within.

This is not recursive as I didn't want it to walk and get nested folders so it is normal for it to stop after it retrieves these.

Finally, it will save the csv in your location. 

If you encounter bugs feel free to raise any issues/ask questions or offer improvements as I am fairly new to coding and was mainly doing this for practice.
I know it is rough and I stopped working on it once I had achieved the result of what I wanted it to do. 

I hope this saves someone some time somewhere!

All the best,

Shaun
