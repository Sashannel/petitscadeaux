location="$(pwd)/output"
chmod u+w "$location"

cd /bin
ls > "$location/bin.txt"
cd /etc
ls > "$location/etc.txt"
cd /lib
ls > "$location/lib.txt"

echo "Files written successfully"
