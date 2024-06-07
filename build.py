import subprocess

jobs = 10
target = "debug"

subprocess.run(f'scons -j{jobs} target=template_{target} platform=linux arch=x86_64', shell=True, cwd='./')
subprocess.run(f'scons -j{jobs} target=template_{target} platform=linux arch=arm64', shell=True, cwd='./')
subprocess.run(f'scons -j{jobs} target=template_{target} platform=linux arch=rv64', shell=True, cwd='./')

subprocess.run(f'scons -j{jobs} target=template_{target} platform=windows arch=x86_32', shell=True, cwd='./')
subprocess.run(f'scons -j{jobs} target=template_{target} platform=windows arch=x86_64', shell=True, cwd='./')

#subprocess.run(f'scons -j{jobs} target=template_{target} platform=macos arch=x86_64', shell=True, cwd='./')
#subprocess.run(f'scons -j{jobs} target=template_{target} platform=macos arch=arm64', shell=True, cwd='./')

#subprocess.run(f'scons -j{jobs} target=template_{target} platform=web', shell=True, cwd='./')

#subprocess.run(f'scons -j{jobs} target=template_{target} platform=android arch=arm32', shell=True, cwd='./')
#subprocess.run(f'scons -j{jobs} target=template_{target} platform=android arch=arm64', shell=True, cwd='./')

target = "release"

subprocess.run(f'scons -j{jobs} target=template_{target} platform=linux arch=x86_64', shell=True, cwd='./')
subprocess.run(f'scons -j{jobs} target=template_{target} platform=linux arch=arm64', shell=True, cwd='./')
subprocess.run(f'scons -j{jobs} target=template_{target} platform=linux arch=rv64', shell=True, cwd='./')

subprocess.run(f'scons -j{jobs} target=template_{target} platform=windows arch=x86_32', shell=True, cwd='./')
subprocess.run(f'scons -j{jobs} target=template_{target} platform=windows arch=x86_64', shell=True, cwd='./')

#subprocess.run(f'scons -j{jobs} target=template_{target} platform=macos arch=x86_64', shell=True, cwd='./')
#subprocess.run(f'scons -j{jobs} target=template_{target} platform=macos arch=arm64', shell=True, cwd='./')

#subprocess.run(f'scons -j{jobs} target=template_{target} platform=web', shell=True, cwd='./')

#subprocess.run(f'scons -j{jobs} target=template_{target} platform=android arch=arm32', shell=True, cwd='./')
#subprocess.run(f'scons -j{jobs} target=template_{target} platform=android arch=arm64', shell=True, cwd='./')

