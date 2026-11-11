# Windows Setup: Install Visual Studio Code

Use this guide if you are using a Windows computer.

## 1. Download Visual Studio Code

1. Open the official Visual Studio Code download page: https://code.visualstudio.com/Download
2. Under **Windows**, choose **User Installer**.
   - Most Windows laptops and desktops use **x64**.
   - Choose **Arm64** only if your Windows computer has an ARM-based processor.
3. Open the downloaded installer when it finishes.

## 2. Install Visual Studio Code

1. Read and accept the licence agreement.
2. Keep the default installation location unless you have a reason to change it.
3. On the **Additional Tasks** screen, we recommend selecting:
   - **Add to PATH** (if offered)
   - **Add "Open with Code" action** to the Windows File Explorer context menu (if offered)
   - **Register Code as an editor for supported file types** (if offered)
4. Select **Install**, then **Finish**.
5. Open Visual Studio Code.

## 3. Install Python

Visual Studio Code is the code editor; Python is installed separately.

1. Visit the official Python downloads page: https://www.python.org/downloads/windows/
2. Download a current stable Python 3 Windows installer.
3. Run the installer.
4. On the first installer screen, select **Add python.exe to PATH** if that option is shown.
5. Select **Install Now** and finish the installation.

## 4. Install the Python extension in VS Code

1. Open Visual Studio Code.
2. Select the **Extensions** icon on the left sidebar (or press `Ctrl+Shift+X`).
3. Search for **Python**.
4. Install the extension published by **Microsoft**.

## 5. Open the workshop repository

1. Extract the workshop ZIP file if you have not already.
2. In VS Code, select **File → Open Folder**.
3. Choose the extracted `github-ai-workshop-CarletonWIE` folder.
4. Open a `.py` file, such as `01-introduction/01_intro.py`.

## 6. Check that Python works

In VS Code, open **Terminal → New Terminal** and enter:

```powershell
python --version
```

If Windows does not recognize `python`, try:

```powershell
py --version
```

If either command displays a Python 3 version, Python is available. If neither works, revisit the Python installation steps or ask the workshop facilitator for help.

To run the open Python file, use the Run button in the top-right corner after selecting a Python interpreter, or enter a command such as:

```powershell
python 01-introduction/01_intro.py
```

If your computer uses the `py` command instead, use:

```powershell
py 01-introduction/01_intro.py
```

## Before the workshop

- [ ] Visual Studio Code is installed.
- [ ] Python 3 is installed.
- [ ] The Microsoft Python extension is installed.
- [ ] The workshop repository folder opens in VS Code.
- [ ] A Python file runs successfully.

**Download safety:** Only download VS Code and Python from their official websites linked above.
