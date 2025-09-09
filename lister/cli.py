import os
import sys
import argparse
import stat
import datetime

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.0f}{unit}"
        size /= 1024
    return f"{size:.0f}PB"

def list_dir(path, show_all=False, long_format=False):
    try:
        entries = os.listdir(path)
    except Exception as e:
        print(f"Error: {e}")
        return
    if not show_all:
        entries = [e for e in entries if not e.startswith('.')]
    for entry in sorted(entries):
        full_path = os.path.join(path, entry)
        try:
            st = os.lstat(full_path)
        except Exception as e:
            print(f"{entry}: Error reading file info: {e}")
            continue
        if long_format:
            mode = stat.filemode(st.st_mode)
            size = format_size(st.st_size)
            mtime = datetime.datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m-%d %H:%M')
            print(f"{mode} {size:>8} {mtime} {entry}")
        else:
            print(entry)

def main():
    parser = argparse.ArgumentParser(description='List directory contents (like ls)')
    parser.add_argument('path', nargs='?', default='.', help='Directory to list')
    parser.add_argument('-a', '--all', action='store_true', help='Show all files including hidden')
    parser.add_argument('-l', '--long', action='store_true', help='Long format (permissions, size, date)')
    args = parser.parse_args()
    list_dir(args.path, show_all=args.all, long_format=args.long)

if __name__ == '__main__':
    main()
