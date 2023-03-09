# Shell, permissions

**1. `su betty`** [Switche the current user to the user betty].

**2. `whoami`** [Print the effective username of the current user].

**3. `groups`** [Print all the groups the current user is part of].

**4. `sudo chown betty hello`** [Change the owner of the file hello to the user betty].

**5. `touch hello`** [Create an empty file called hello].

**6. `chmod u+x hello`** [Add execute permission to the owner of the file hello].

**7. `chmod 754 hello`** [Add execute permission to the owner and the group owner, and read permission to other users, to the file hello].

**8. `chmod ugo+x hello`** [Add execution permission to the owner, the group owner and the other users, to the file hello].

**9. `chmod 007 hello`** [Set the permission to the file hello as follows:].

	* Owner: no permission at all

	* Group: no permission at all Other 

	* users: all the permissions

**10. `chmod 753 hello`** [Set the mode of the file hello to this:].

	`-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello`

**11. `chmod --reference=olleh hello`** [Set the mode of the file hello the same as olleh’s mode].

**12. `chmod a+X *`** [Add execute permission to all subdirectories of the current directory for the owner, the group owner and all other users].

	* Regular files should not be changed.

**13. `mkdir -m 751 my_dir`** [Create a directory called my_dir with permissions 751 in the working directory].

**14. `chgrp school hello`** [Change the group owner to school for the file hello].

**15. `sudo chown vincent:staff *`** [Change the owner to vincent and the group owner to staff for all the files and directories in the working directory].

**16. `sudo chown -h vincent:staff _hello`** [Change the owner and the group owner of _hello to vincent and staff respectively].

	* The file _hello is a symbolic link.

**17. `sudo chown  --from=guillaume betty hello`** [Change the owner of the file hello to betty only if it is owned by the user guillaume].

**18. `telnet towel.blinkenlights.nl`** [Play the StarWars IV episode in the terminal].

