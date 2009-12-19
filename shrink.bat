@echo off 

cd dist

"D:\Install\7-Zip\7z.exe" -aoa x library.zip -olibrary\ 
del library.zip 
 
cd library\ 
"D:\Install\7-Zip\7z.exe" a -tzip -mx9 ..\library.zip -r 
cd.. 
rd library /s /q 
 
upx.exe --force --best *.*
