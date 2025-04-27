# generate-qr-code-with-GUI

## How to use application
- Start application "Generate.QR-code.exe".
- Enter the URL of your website.
- Enter a name for the QR-code to name it when is generating.
- Click on the button "Generate".
- The file generating is present in the path : %USERPROFILE%\Documents\qrcode

## How to install the project locally
- Create virtualenv.
```bash
python3 -m venv venv
```
- Activate the virtualenv.
```bash
source venv/bin/activate
```
- Install required packages.
```bash
pip3 install qrcode
pip3 install pillow
```
- Launch the project.
```bash
python3 main.py
```