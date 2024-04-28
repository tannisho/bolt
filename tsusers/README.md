For creating/populating the tsusers group on xrdp servers
-- 

Copies a file of the tsusers to the xrdp server then executes a shell script that checks if the 
tusers group exists and if not creates it. If it already exists it removes all the users from 
the group and then populates it with the users from the file it uploaded earlier.


Usage:
 - populate tsuser group on xrdp_server1: ./tsusers.sh xrdp_server1
 - populate tsuser group on xrdp servers: ./tsusers_all.sh


Files:

xrdp_servers/*
 - filenames are the xrdp server hostnames and each contains the users belonging to it.

tsadmins.lst
 - file containing xrdp admin users, ie:

  foobar1 
  barfoo1
  barbaz1
  barboo1

tsusers/work/*
 - scripts for gathering existing usernames and matching usernames with xrdp servers
 - ga.py: grabs all usernames in xrdp_servers/* and matches full name to it. redirect output to 'username_fullname_table' file.
 - can.py: grabs users full names from csv file and outputs 'username:xrdp_server' if exists in username_fullname_table file, otherwise outputs 'NOT FOUND'. csv file should have 3 fields, second field should be 'firstname lastname', third field should be xrdp_server.


Option 1 (removes duplicate UID's):

 - subcon.py: checks uids from csv file and skips if not an integer or 5 numbers, substitutes Cell.* with appropriate xrdp_server. Next converts uid to username and outputs as 'username:xrdp_server' if found, else output 'UID not found: uid'. csv file should have 4 fields, second field should be 'uid', third field should be 'xrdp_server'.
 - clnl.py: removes duplicates from ideally a master list of all outputs of subcon.py. assumes subcon.py master list is /tmp/2. 
 - pop_xrdp.sh: takes output from clnl.py and populates xrdp_servers lists. assumes clnl.py output is /tmp/1. 


Option 2 (leaves duplicates):


 - subcon.py: checks uids from csv file and skips if not an integer or 5 numbers, substitutes Cell.* with appropriate xrdp_server. Next converts uid to username and outputs as 'username:xrdp_server' if found, else output 'UID not found: uid'. csv file should have 4 fields, second field should be 'uid', third field should be 'xrdp_server'. Redirection output command: 'python subcon.py | grep -v UID > /tmp/1' 
 - pop_xrdp.sh: takes output from last command from /tmp/1. 
