import sys
import subprocess

def command_exists(command: str):
    """Check wheather `command` is an executable."""
    from shutil import which

    return which(command) is not None

# check pre-commit
if command_exists('pre-commit'):
    print('pre-commit is already installed! Proceeding with setup...')
else:
    print('pre-commit is not installed! Proceeding with installation...')
    # check pipx
    if command_exists('pipx'):
        print('using pipx to install pre-commit...')
        subprocess.run(['pipx', 'install', 'pre-commit'], check=True)
    else:
        print('pipx is not installed!')
        install_pipx = input('do you want to install pipx? (y/n): ').strip().lower()

        if install_pipx == 'y':
            print('installing pipx...')
            subprocess.run([sys.executable, "-m", "pip", "install", "--user", "pipx"], check=True)
            subprocess.run([sys.executable, "-m", "pipx", "ensurepath"], check=True)

            # check if pipx isn't added to PATH yes
            if not command_exists('pipx'):
                print('please restart your terminal or run `source ~/.bashrc` and rerun this script.')
                sys.exit(1)

            print('installing pre-commit using pipx...')
            subprocess.run(['pipx', 'install', 'pre-commit'], check=True)
        else:
            print('pipx is required for installation. exiting...')
            sys.exit(1)

# setup pre-commit
try:
    subprocess.run(['pre-commit', 'install'])
    print('noice! pre-commit setup complete!')
except subprocess.CalledProcessError:
    print('failed to install pre-commit hooks. check logs.')
    sys.exit(1)
