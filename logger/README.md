# Logger System

## Logs
v1.3.6
- "delete" now use prompt_toolkit for input filename
- "list entries" now use prompt_toolkit
- 
v1.3.5
- Refactor: input status and progress now use prompt_toolkit
- Refactor: convert from json to log, input filename using prompt_toolkit
- Refactor: input function on main menu has been reworked
- TODO :
	- refactor input validator in delete and list entries
v1.3.4-Experiment
- Edit feature is now fully functional
- options of what field the user want's to edit is not implemented
- Add autocompletion and suggestion for "Task" on update by using existed "Task" in log entry as ref.

v1.3.3-Experiment
- edit feature now can edit progress and status (status need some works)
- TODO : make "options" of what field the user want's to edit, to fix the edit status

v1.3.2-Experiment
- refactor: changed some function name 
- style: changing the style of how .log is written (convert.py)

v1.3.1-Experiment
- changed the versioning
- "Delete file" feature is working
- change the .log file into read-only to prevent user from messing with the file
  outside of the tools, to ensure file integrity
- Add converter feature to convert .json to .log manually
- Edit feature is half way done
ToDo List : 
	- Move the entry update logic for status and progress to utils/ as public module function
	- name it as progress_status.py
	- this file will be used by update.py and edit.py
	
v1.3.0-Experiment
- Reworking the structure of the program
- Add convert to raw text
- change the extension file into .log for more easier classification
- N.B. delete function is not working for now, will be done tomorrow

v1.2.0
- Add open edit feature
- open & edit feature is using existing text editor tools such as Nano and Micro
- in feature gedit will be added

v1.1.4
- Add debug file for debuging
- 
 
v1.1.3
- Finishing the log entries listing feature
- N.B. clean the entryList file, still have lot of debug lines

v1.1.2
- Changes the program file structure to be more tidy and more managed

v1.1.1
- NULL {Forgot to documenting it}
