Setup:

Clone the Project, run the Pip Installer to load dependencies and proceed using the Command-Line Tool

```sh
git clone git@github.com:RogerWebb/oregonpublicdata.git
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Load an ORESTAR Excel Export File

```sh
python -m oregonopendata.orestar load-file <filename>
```