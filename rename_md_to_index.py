# -*- coding: utf-8 -*-
"""
将 name.md 文件重命名为 name/index.md 的脚本
"""

import os
import shutil
from pathlib import Path


def rename_md_to_index(directory=".", recursive=True):
    """
    将指定目录下的所有 .md 文件重命名为对应目录下的 index.md
    
    Args:
        directory (str): 要处理的目录路径，默认为当前目录
        recursive (bool): 是否递归处理子目录，默认为True
    """
    directory_path = Path(directory)
    
    if not directory_path.exists():
        print(f"错误: 目录 '{directory}' 不存在")
        return
    
    # 查找所有 .md 文件（递归或非递归）
    if recursive:
        md_files = list(directory_path.rglob("*.md"))
        print(f"递归搜索目录 '{directory}' 及其子目录...")
    else:
        md_files = list(directory_path.glob("*.md"))
        print(f"搜索目录 '{directory}'...")
    
    # 过滤掉已经是 index.md 的文件
    md_files = [f for f in md_files if f.name != "index.md"]
    
    if not md_files:
        print(f"在目录 '{directory}' 中没有找到需要处理的 .md 文件")
        return
    
    print(f"找到 {len(md_files)} 个需要处理的 .md 文件:")
    for md_file in md_files:
        relative_path = md_file.relative_to(directory_path)
        print(f"  - {relative_path}")
    
    print("\n开始处理...")
    
    processed_count = 0
    skipped_count = 0
    error_count = 0
    
    for md_file in md_files:
        # 获取文件名（不包含扩展名）
        file_stem = md_file.stem
        
        # 创建目标目录（在原文件所在目录下）
        parent_dir = md_file.parent
        target_dir = parent_dir / file_stem
        target_file = target_dir / "index.md"
        
        try:
            # 如果目标目录不存在，创建它
            if not target_dir.exists():
                target_dir.mkdir(parents=True, exist_ok=True)
                relative_target_dir = target_dir.relative_to(directory_path)
                print(f"✓ 创建目录: {relative_target_dir}")
            
            # 如果目标文件已存在，询问是否覆盖
            if target_file.exists():
                relative_target_file = target_file.relative_to(directory_path)
                response = input(f"文件 '{relative_target_file}' 已存在，是否覆盖？(y/N): ")
                if response.lower() not in ['y', 'yes']:
                    relative_md_file = md_file.relative_to(directory_path)
                    print(f"⚠ 跳过: {relative_md_file}")
                    skipped_count += 1
                    continue
            
            # 移动文件
            shutil.move(str(md_file), str(target_file))
            relative_md_file = md_file.relative_to(directory_path)
            relative_target_file = target_file.relative_to(directory_path)
            print(f"✓ 重命名: {relative_md_file} -> {relative_target_file}")
            processed_count += 1
            
        except Exception as e:
            relative_md_file = md_file.relative_to(directory_path)
            print(f"✗ 处理 {relative_md_file} 时出错: {e}")
            error_count += 1
    
    print(f"\n处理完成！")
    print(f"成功处理: {processed_count} 个文件")
    if skipped_count > 0:
        print(f"跳过: {skipped_count} 个文件")
    if error_count > 0:
        print(f"错误: {error_count} 个文件")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="将 .md 文件重命名为对应目录下的 index.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  python rename_md_to_index.py                    # 递归处理当前目录及子目录
  python rename_md_to_index.py ./docs             # 递归处理指定目录及子目录
  python rename_md_to_index.py -d ./my_docs       # 使用 -d 参数指定目录
  python rename_md_to_index.py --no-recursive     # 只处理当前目录，不递归
  python rename_md_to_index.py ./docs --no-recursive  # 只处理指定目录，不递归
        """
    )
    
    parser.add_argument(
        "directory", 
        nargs="?", 
        default=".", 
        help="要处理的目录路径（默认为当前目录）"
    )
    
    parser.add_argument(
        "-d", "--dir", 
        dest="directory", 
        help="要处理的目录路径"
    )
    
    parser.add_argument(
        "--no-recursive", 
        action="store_true",
        help="不递归处理子目录，只处理指定目录下的文件"
    )
    
    args = parser.parse_args()
    
    print("=== MD文件重命名工具 ===")
    print(f"处理目录: {os.path.abspath(args.directory)}")
    print(f"递归处理: {'否' if args.no_recursive else '是'}")
    print()
    
    rename_md_to_index(args.directory, recursive=not args.no_recursive)


if __name__ == "__main__":
    main() 
