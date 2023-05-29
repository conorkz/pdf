# PDF watermarker and merger
These scripts can watermark and merge any pdf files.	 
## Requirements
- Python 3.x
- PyPDF2 (`pip install PyPDF2`)
- Or just run `$ pip install -r requirements.txt`
## Usage
1. Open a command prompt or terminal and navigate to the directory where you saved the script.
2. To merge two pdf files run `merger.py` using the following command: `python merger.py <first.pdf> <second.pdf>`
3. To watermark a pdf file, put your watermark icon in a pdf file and specify this file in `watermrk.py`.In my case, `wtr.pdf`

Example:
`python merger.py dummy.pdf twopage.pdf`
This command will merge these two pdf files and save as `merged.pdf`
