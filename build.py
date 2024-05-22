import os
import subprocess
import platform

# Paths
project_dir = os.path.abspath(os.path.dirname(__file__))
windows_script = os.path.join(project_dir, 'windows.py')
linux_script = os.path.join(project_dir, 'linux.py')
builds_dir = os.path.join(project_dir, 'builds')
icon_path = os.path.join(project_dir, 'image.ico')

# Ensure builds directory exists
if not os.path.exists(builds_dir):
    os.makedirs(builds_dir)

def build_windows():
    print("Building portable Windows executable...")
    if not os.path.exists(icon_path):
        print(f"Icon file not found at: {icon_path}")
        return

    command = [
        'pyinstaller', 
        '--onefile', 
        '--noconsole', 
        f'--icon={icon_path}', 
        '--distpath', builds_dir, 
        windows_script
    ]
    
    result = subprocess.run(command)
    if result.returncode == 0:
        print("Windows portable build successful!")
    else:
        print("Windows portable build failed!")

def build_linux():
    print("Building Linux executable and .deb package...")
    dist_dir = os.path.join(project_dir, 'dist')
    result = subprocess.run(['pyinstaller', '--onefile', '--distpath', dist_dir, linux_script])
    if result.returncode == 0:
        executable_path = os.path.join(dist_dir, 'linux')
        os.makedirs(builds_dir, exist_ok=True)
        result = subprocess.run(['fpm', '-s', 'dir', '-t', 'deb', '-n', 'cleaner', '--prefix', '/usr/local/bin', executable_path], cwd=builds_dir)
        if result.returncode == 0:
            print("Linux .deb package build successful!")
        else:
            print("Linux .deb package build failed!")
    else:
        print("Linux executable build failed!")

if __name__ == "__main__":
    if platform.system() == "Windows":
        build_windows()
    elif platform.system() == "Linux":
        build_linux()
    else:
        print("Unsupported platform!")