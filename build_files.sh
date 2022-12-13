# build_files.sh
echo "BUILD START"
pip install -r requirements.txt
python3.11.0 manage.py collectstatic --noinput --clear
echo "BUILD END"