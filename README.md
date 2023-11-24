# workshop_cv_alliance
This is a github repository for the workshop that we have done for the Alliance University

## Clone the repository or download the repository

```
git clone https://github.com/spcCodes/workshop_cv_alliance.git
```
## Model for this repository

Link: https://drive.google.com/drive/folders/1SmZ6AiADEYJzjoBTtMHLI40321t4bCVJ?usp=sharing

## To create a virtual environment in Python 3.10 using `pyenv` on computer, follow these steps:

1. **Install pyenv** (if not already installed):
   
   If you haven't installed `pyenv` yet, you can do so using a package manager like Homebrew. Open your terminal and run these commands:

   ```bash
   brew update
   brew install pyenv
   ```

2. **Set up pyenv**: (This is an optional step)

   Add the following lines to your shell profile configuration file (e.g., `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`) to enable `pyenv`:

   ```bash
   export PATH="$HOME/.pyenv/bin:$PATH"
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"
   ```

   After adding these lines, you'll need to restart your terminal or run `source ~/.your_shell_profile` to apply the changes.

3. **Install Python 3.10.13**:

   Before creating a virtual environment, you need to install Python 3.10.13 using `pyenv`. Run the following command:

   ```bash
   pyenv install 3.10.13
   ```

   Replace `3.10.13` with the specific version of Python 3.10 you want to install.

4. **Create a virtual environment**:

   Now that Python 3.10.13 is installed, you can create a virtual environment using the `pyenv virtualenv` command. Replace `myenv` with your preferred virtual environment name:

   ```bash
   pyenv virtualenv 3.10.13 myenv
   ```

5. **Activate the virtual environment**:

   To activate the virtual environment, use the `pyenv activate` command:

   ```bash
   pyenv activate myenv
   ```

6. **Deactivate the virtual environment**:

   To deactivate the virtual environment and return to the system's Python, simply use the `pyenv deactivate` command:

   ```bash
   pyenv deactivate
   ```
