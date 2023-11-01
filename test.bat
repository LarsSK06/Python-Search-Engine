@echo off


set url =%ip%:%port%?query=a

echo Calling...
call curl -H "Host: mywebsite.com" http://127.0.0.1:5000/search?query=a