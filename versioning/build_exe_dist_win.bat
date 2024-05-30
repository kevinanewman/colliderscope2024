REM usage build_dist

cd ..

REM build executable

pyinstaller exe_entry.py ^
    --name colliderscope2024-0.0.28-win ^
    --paths .;filterwidget ^
    --add-data assets;assets ^
    --noconfirm ^
    --onefile

REM cleanup

move /Y  *.spec versioning
rmdir /S /Q __pycache__
rmdir /S /Q build

cd versioning
