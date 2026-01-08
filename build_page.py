def main():
    # 个人信息配置
    personal_info = {
        "name": "ZiQin Wang",
        "title": "Senior Frontend Engineer",
        "description": "I’m Miles, an experienced senior engineer specializing in frontend and full-stack product development. I thrive on delivering complex features, mentoring teams, and maintaining curiosity alongside a steady output tempo. This repository mirrors my GitHub profile, so everything shown here also appears on https://github.com/didadida262.",
        "skills": ["Frontend", "Backend & Services", "Engineering & Deployment", "Visualization & Mapping"],
        "projects": [
            {"name": "Annotation Platform (project_labelV2)", "url": "https://project-label-v2.vercel.app"},
            {"name": "Point Cloud Simulation Platform (project_pointcloud)", "url": "https://project-pointcloud.vercel.app"},
            {"name": "3D Situation Simulation (project_cesium)", "url": "https://project-cesium-react.vercel.app"}
        ],
        "contact": {
            "github": "https://github.com/didadida262",
            "linkedin": "https://linkedin.com/in/yourprofile"
        }
    }
    # HTML模板
    html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{personal_info['name']} - Tech Card</title>
<style>
body {{
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    line-height: 1.6;
    background-color: #f4f4f4;
}}
.container {{
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}}
h1 {{
    color: #333;
    text-align: center;
    margin-bottom: 10px;
}}
.title {{
    text-align: center;
    color: #666;
    font-size: 1.2em;
    margin-bottom: 20px;
}}
.skills {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 20px 0;
}}
.skill {{
    background: #007bff;
    color: white;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.9em;
}}
.projects, .contact {{
    margin: 20px 0;
}}
a {{
    color: #007bff;
    text-decoration: none;
}}
a:hover {{
    text-decoration: underline;
}}
</style>
</head>
<body>
<div class="container">
<h1>{personal_info['name']}</h1>
<div class="title">{personal_info['title']}</div>
<p>{personal_info['description']}</p>
<h2>技能</h2>
<div class="skills">
"""
    # 添加技能标签
    for skill in personal_info['skills']:
        html_content += f' <span class="skill">{skill}</span>\n'
    html_content += """
</div>
<h2>项目经历</h2>
<div class="projects">
<ul>
"""
    # 添加项目链接
    for project in personal_info['projects']:
        html_content += f' <li><a href="{project["url"]}" target="_blank">{project["name"]}</a></li>\n'
    html_content += f"""
</ul>
</div>
<h2>联系方式</h2>
<div class="contact">
<p>
<a href="{personal_info['contact']['github']}" target="_blank">GitHub</a> |
<a href="{personal_info['contact']['linkedin']}" target="_blank">LinkedIn</a>
</p>
</div>
</div>
</body>
</html>
"""
    # 写入文件
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("index.html generated successfully!")

if __name__ == "__main__":
    main()
