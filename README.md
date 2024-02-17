# GitHub Codespaces ♥️ Django

欢迎来到您崭新的运行 Django 的 Codespace！我们已经为您启动并运行了一切，方便您探索 Django。

从 git 的角度来看，您也有一个空白的画布可以工作。这里有一个初始提交，包含您现在看到的内容 - 从这里开始您将去向何方完全取决于您！

您在这里做的一切都包含在这一个 codespace 中。GitHub 上还没有仓库。如果您准备好了，您可以点击“发布分支”，我们将为您创建仓库并上传您的项目。如果您只是在探索，并且不再需要这段代码，那么您可以简单地删除您的 codespace，它将永远消失。
收集静态文件：

```python
python manage.py collectstatic
```
运行此应用程序：

```python
python manage.py runserver
```

docker运行
```
docker-compose up -d
```
进入数据库
```
docker exec -it peekpabackend_db_1 bash
psql -U postgres
```
清库
```
\c peekpa_db
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
```

同步数据
```
python3 manage.py makemigrations
python3 manage.py migrate
```