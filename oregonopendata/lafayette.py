import json, pandas, pytesseract, scrapy
from pdf2image import convert_from_path
from argparse import ArgumentParser
from pprint import pprint


class LafayetteDataLoader:

    def __init__(self):
        self.city_council_url = "https://www.ci.lafayette.or.us/index.asp?SEC=44E71BFC-D809-4ECB-8344-4E12CCCFC0C6"

    def pdf_read_text(self, filename):
        # Convert PDF to images
        pages = convert_from_path("data/cc_01-11-2024_minutes.pdf", 300)
        num_pages = len(pages)

        fulltext = ""

        for i in range(0, num_pages):
            t = pytesseract.image_to_string(pages[i])

            fulltext += t

        return fulltext

if __name__ == "__main__":
    ap = ArgumentParser()

    args = ap.parse_args()


