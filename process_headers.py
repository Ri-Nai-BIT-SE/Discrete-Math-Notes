#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown 标题层级处理脚本
功能：
1. 为每个文件添加一号标题（基于文件的title字段）
2. 将原有的最高标题层级改为2级，其他标题按差值调整
"""

import os
import re
from pathlib import Path
import yaml


def extract_frontmatter_and_content(content):
    """提取前置元数据和正文内容"""
    if not content.startswith('---'):
        return None, content
    
    # 查找第二个 ---
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content
    
    try:
        frontmatter = yaml.safe_load(parts[1])
        content_body = parts[2]
        return frontmatter, content_body
    except yaml.YAMLError:
        return None, content


def find_min_header_level(content):
    """找到内容中最小的标题层级"""
    header_pattern = r'^(#{1,6})\s+'
    matches = re.findall(header_pattern, content, re.MULTILINE)
    
    if not matches:
        return None
    
    return min(len(match) for match in matches)


def adjust_headers(content, min_level):
    """调整标题层级"""
    if min_level is None:
        return content
    
    # 计算需要增加的层级数（让最小层级变为2级）
    level_diff = 2 - min_level
    
    if level_diff <= 0:
        return content
    
    def replace_header(match):
        current_hashes = match.group(1)
        new_level = len(current_hashes) + level_diff
        # 确保不超过6级标题
        new_level = min(new_level, 6)
        return '#' * new_level + match.group(0)[len(current_hashes):]
    
    # 替换所有标题
    header_pattern = r'^(#{1,6})(\s+.*)$'
    adjusted_content = re.sub(header_pattern, replace_header, content, flags=re.MULTILINE)
    
    return adjusted_content


def process_markdown_file(file_path):
    """处理单个Markdown文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取前置元数据和正文
        frontmatter, body = extract_frontmatter_and_content(content)
        
        if frontmatter is None:
            print(f"警告: {file_path} 没有有效的前置元数据")
            return False
        
        # 获取标题
        title = frontmatter.get('title', '未命名')
        
        # 查找最小标题层级
        min_level = find_min_header_level(body)
        
        # 调整标题层级
        adjusted_body = adjust_headers(body, min_level)
        
        # 添加一号标题
        new_content = f"---\n{yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)}---\n\n# {title}\n{adjusted_body}"
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ 已处理: {file_path}")
        if min_level:
            print(f"  - 原最高标题层级: {min_level}, 调整后: 2")
        else:
            print(f"  - 无标题内容")
        
        return True
        
    except Exception as e:
        print(f"✗ 处理失败 {file_path}: {e}")
        return False


def find_markdown_files(docs_dir):
    """查找所有Markdown文件"""
    markdown_files = []
    docs_path = Path(docs_dir)
    
    for file_path in docs_path.rglob('*.md'):
        if file_path.name == 'index.md':
            markdown_files.append(file_path)
    
    return markdown_files


def main():
    """主函数"""
    docs_dir = Path(__file__).parent / 'docs'
    
    if not docs_dir.exists():
        print(f"错误: docs目录不存在: {docs_dir}")
        return
    
    print(f"开始处理 {docs_dir} 目录下的Markdown文件...")
    
    # 查找所有Markdown文件
    markdown_files = find_markdown_files(docs_dir)
    
    if not markdown_files:
        print("未找到任何Markdown文件")
        return
    
    print(f"找到 {len(markdown_files)} 个文件")
    
    # 处理每个文件
    success_count = 0
    for file_path in markdown_files:
        if process_markdown_file(file_path):
            success_count += 1
        print()  # 空行分隔
    
    print(f"处理完成! 成功: {success_count}/{len(markdown_files)}")


if __name__ == '__main__':
    main() 
