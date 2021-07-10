@echo off
TITLE Batch Script to run MTS Web Application
echo Starting the MTS Application...
echo Enter Ctrl + c to stop application
echo -----------------------
cmd /k "cd /d C:\Users\Chisom1\Documents\Final Year Project\MTS\venv\scripts & activate & cd /d C:\Users\Chisom1\Documents\Final Year Project\MTS & python manage.py runserver"
