#! /bin/zsh

cd ..

# build executable

pyinstaller exe_entry.py \
    --name colliderscope2024-0.0.1-mac-arm64.command \
    --paths .:. \
    --add-data assets:assets \
    --noconfirm \
    --onefile

# cleanup

mv *.spec versioning
rm -R __pycache__
rm -R build

cd versioning