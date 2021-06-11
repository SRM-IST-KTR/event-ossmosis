echo "Enter into Vue Project [...]"
cd web
echo "Installing Node Dependencies [...]"
yarn
echo "Creating Vue.js production build [...]"
yarn build
cd ..
echo "Deleting old build artifacts [...]"
if [ -d "server/dist" ]
then
echo "Old files found! Deleting..."
rm -rf server/dist
else
echo "No old build artifacts found! Skipping..."
fi
echo "Moving build artifacts to production [...]"
mv web/dist server/dist
echo "Enter into Django Project [...]"
cd server
pip install -r requirements.txt
echo "Copying static files to Django static directory [...]"
python3 manage.py collectstatic --no-input
echo "Files successfully copied!"