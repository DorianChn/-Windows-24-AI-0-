#!/usr/bin/env python3
"""创建新项目模板"""

import os
import sys
from pathlib import Path

def create_python_project(project_name, project_type="web"):
    """创建Python项目"""
    print(f"🚀 创建Python项目: {project_name}")
    
    # 创建目录
    project_dir = Path.cwd() / project_name
    project_dir.mkdir(exist_ok=True)
    
    # 创建子目录
    dirs = ["app", "tests", "docs", "scripts"]
    for d in dirs:
        (project_dir / d).mkdir(exist_ok=True)
    
    # 创建文件
    files = {
        "README.md": f"# {project_name}\n\n项目描述\n",
        "requirements.txt": "flask>=2.0.0\npytest>=7.0.0\n",
        ".gitignore": "__pycache__/\n*.pyc\n.env\nvenv/\n.idea/\n",
        "app/__init__.py": "",
        "app/models.py": "",
        "app/views.py": "",
        "tests/__init__.py": "",
        "tests/test_app.py": "",
    }
    
    for file, content in files.items():
        (project_dir / file).write_text(content, encoding="utf-8")
    
    print(f"✅ 项目创建完成: {project_dir}")
    print(f"📁 项目结构:")
    for item in sorted(project_dir.rglob("*")):
        if item.is_file():
            print(f"  {item.relative_to(project_dir)}")
    
    return 0

def create_web_project(project_name):
    """创建Web项目"""
    print(f"🌐 创建Web项目: {project_name}")
    
    project_dir = Path.cwd() / project_name
    project_dir.mkdir(exist_ok=True)
    
    # 创建目录
    dirs = ["static/css", "static/js", "static/images", "templates", "tests"]
    for d in dirs:
        (project_dir / d).mkdir(parents=True, exist_ok=True)
    
    # 创建文件
    files = {
        "README.md": f"# {project_name}\n\nWeb项目\n",
        "requirements.txt": "flask>=2.0.0\n",
        ".gitignore": "__pycache__/\n*.pyc\n.env\nvenv/\n",
        "app.py": """from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
""",
        "templates/index.html": """<!DOCTYPE html>
<html>
<head>
    <title>项目</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
""",
        "static/css/style.css": "body { font-family: Arial; }",
        "static/js/main.js": "// JavaScript代码",
    }
    
    for file, content in files.items():
        (project_dir / file).write_text(content, encoding="utf-8")
    
    print(f"✅ Web项目创建完成: {project_dir}")
    return 0

def main():
    if len(sys.argv) < 2:
        print("用法: python create-project.py <项目名称> [类型]")
        print("类型: python, web (默认: python)")
        return 1
    
    project_name = sys.argv[1]
    project_type = sys.argv[2] if len(sys.argv) > 2 else "python"
    
    if project_type == "web":
        return create_web_project(project_name)
    else:
        return create_python_project(project_name)

if __name__ == "__main__":
    sys.exit(main())
