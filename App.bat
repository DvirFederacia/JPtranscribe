@echo off
echo Running script with argument: %1 >> debug.log
cd %~dp0
echo Current directory: %~dp0 >> debug.log
set PYTHONIOENCODING=utf-8
python JPtranscribe.py --path %1 >> debug.log 2>&1