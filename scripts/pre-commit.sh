#!/bin/bash

# function to check for commands
command_exists() {
  command -v "$1" &>/dev/null
}

# check if pre-commit is already installed
if command_exists pre-commit; then
  echo "pre-commit is already installed! Proceeding with setup..."
else
  echo "pre-commit is not installed! Proceeding with installation..."
  # check if pipx is installed
  if command_exists pipx; then
    echo "Using pipx to install pre-commit..."
    pipx install pre-commit
  else
    echo "pipx is not installed!"
    read -p "Do you want to install pipx? (y/n): " install_pipx
    if [[ "$install_pipx" == "y" || "$install_pipx" == "Y" ]]; then
      echo "Installing pipx..."
      python3 -m pip install --user pipx
      python3 -m pipx ensurepath

      # reload the shell environment if pipx was just added to PATH
      if ! command_exists pipx; then
        echo "Please restart your terminal or run 'source ~/.bashrc' and rerun this script."
        exit 1
      fi
      # install pre-commit
      echo "Using pipx to install pre-commit..."
      pipx install pre-commit
    else
      echo "pipx is required for installation. re-run the script if you want us to install. exiting..."
      exit 1
    fi
  fi
fi

# setup pre-commit
if pre-commit install; then
  echo "pre-commit hooks installed successfully!"
else
  echo "Failed to install pre-commit hooks. Please check for issues."
  exit 1
fi

echo "noice! pre-commit setup complete!"
