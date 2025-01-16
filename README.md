# DevLogTool
Creates a markdown Devlog file from a template file. Don't change that since the code relies on it. If you still want to change it, you will have to modify parts of the code too.

## How it works
It creates a new log with an index one higher than the previous largest index. This index can be found in the filename, along with the current date and time, down to the minute. The program then takes a template and replaces information such as time, date, title, and file content if the user chooses to enter it automatically. The log is then saved in the log folder.

## How to use
- Pull the Git repository onto your local machine and place the "New Devlog" folder (with a space) onto the desktop or anywhere else that is convenient. For example: "C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs". I would recommend creating a new folder called "My Programs" or something similar, where you can store your own programs. (It will still work.) The application can then be accessed by the Windows search bar, and you can pin it to the Windows start menu. :)


heres the current template:

```
# Dev Diary Nr.

## Title

## Date: YYYY-MM-DD | Time: HH:MM

### Lessons learned:
- 

### What I did:
- 

### Challenges faced:
- 

### Next steps:
- 
```
this will look something like this:
# Dev Diary Nr.

## Title

## Date: YYYY-MM-DD | Time: HH:MM

### Lessons learned:
- 

### What I did:
- 

### Challenges faced:
- 

### Next steps:
- 

