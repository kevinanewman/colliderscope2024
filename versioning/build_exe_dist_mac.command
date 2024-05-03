#! /bin/zsh

cd ..

# build executable

pyinstaller exe_entry.py \
    --name colliderscope2024-0.0.9-mac-arm64.command \
    --paths .:filterwidget \
    --add-data assets:assets \
    --noconfirm \
    --onefile

# cleanup

mv *.spec versioning
rm -R __pycache__
rm -R build

cd versioning
