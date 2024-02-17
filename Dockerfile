# 使用 Python 官方镜像作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器中的工作目录
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口 8000 供外界访问
EXPOSE 8000

# 启动 Django 应用
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
