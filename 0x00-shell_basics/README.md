# Shell, basics

**1. `pwd`** [Print the absolute path name of the current working directory].

**2. `ls`** [Display the contents list of your current directory].

**3. `cd ~`** [Changes the working directory to the user’s home directory].

**4. `ls -l`** [Display current directory contents in a long format].

**5. `ls -l -a`** [Display current directory contents, including hidden files (starting with .). Use the long format].

**6. `ls -n -d .* [[:digit:]]`** [Display current directory contents].

	* Long format.

	* With user and group IDs displayed numerically.

	* And hidden files (starting with .).

**7. `mkdir /tmp/my_first_directory`** [creates a directory named my_first_directory in the /tmp/ directory].

**8. `mv`** [Move the file].

**9. `rm`** [Delete the file].

**10. `rm -r`** [Delete the directory].

**11. `cd -`** [Changes the working directory to the previous one].

**12. `ls -l -a . .. /boot`** [Lists all files].

**13. `file <file>`** [Prints the type of the file].

**14. `ln -s /bin/ls __ls__`** [Create a symbolic link to /bin/ls, named __ls__].

**15. `cp -n *.html ..`** [Copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory].

**16. `mv [[:upper:]]* /tmp/u`** [Moves all files beginning with an uppercase letter to the directory /tmp/u].

**17. `rm *~`** [Deletes all files in the current working directory that end with the character ~].

**18. `mkdir -p welcome/to/school`** [Creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory].

**19. `ls -a -p -v --format=comma`** [lists all the files and directories of the current directory, separated by commas (,).].

**20. `0 string SCHOOL School data !:mime School`** [Create a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.].

