import os
import datetime
import shutil

shutil.copy2('C:/Program Files (x86)/Steam/userdata/916735995/218620/remote/save098.sav',
             'C:/Users/Pintér Péter/Documents/PD2Backup')
Current_Date = datetime.datetime.today().strftime('%Y-%b-%d')
os.rename(r'C:\Users\Pintér Péter\Documents\PD2Backup\save098.sav', r'C:\Users\Pintér Péter\Documents\PD2Backup\save098_' + str(Current_Date) + '.sav')
print('Done.')
