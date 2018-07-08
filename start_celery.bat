@echo off

python manage.py celery -A MultipleInterfaceManager worker --loglevel=info
python manage.py celery beat --loglevel=info
celery flower #启动任务监控后台

echo 启动完毕，准备退出。。。
