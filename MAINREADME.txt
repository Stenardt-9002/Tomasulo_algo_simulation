Give input in textinout.txt file according to format specified in textinoutbkup.txt
All execution hardwares are pipelined

if want simulation run this file:= python3 main.py



Enter textinout.txt enter the format given in SampleInputlist.txt


NOTE: Total time given in PDF ,1 are used in ISSUE ,1 are used in WRITEBACK ,rest in execution


--------------------------------------------
  |    ISSUE   EXEC       |    WRITE_BACK
  |      1    |  Given    |    1
  |      1    |   IN      |    1
  |      1    |   Pdf     |    1
--------------------------------------------
Registers use F1-F16
ALL HARDWARE have 1 quantity


Feature Of Hardware
Issue ,Execution,Writeback of same hardware can be used parallely




Feature of Reservation Table

'busy':If hardware part is busy,
'op':which operation is using it
['vj':0,'vk':0] : empty means reading hardware was not available /if something present means the name of hardware
'qj':0,'qk':0

Reservation Station for load ,complement and store differently


FEATURES of Register Renaming used

1 For WAR writing register is renamed and waited until all the registers are done reading .
2 For WAW writing register is renamed until original register is finished with writeback
3 If a register is renamed already then it is not renamed again ,the respective process queue for register renaming will be stalled.
4 For RAW stalling will be done for execution(no reading wll be done until writing).
5 If no register is left for renaming for WAR then statement will not be issued.
6 If no register is left for renaming for WAW then statement will not be writeback.



Please Inform in any bug found and program Halts in between
