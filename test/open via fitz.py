import fitz
import re

pdf = fitz.open('/home/mykola/Documents/SM-F721B_UM_CIS_TT_Ukr_Rev.2.0_230210.pdf')
document_page_numbers = pdf.page_count #кількість сторінок
start_page_of_content = 1
final_page_of_content = 3
dict_of_pages = {}
for page_old in range(start_page_of_content, final_page_of_content):
    content = pdf[page_old]
    example_content = content.get_text()
    pattern = r'(\d+)\s+(.*?)$'
    matches = re.findall(pattern, example_content, re.MULTILINE)

    for page, section in matches:
        print(f"Page: {page}, Section: {section}")
        dict_of_pages[page] = section
print(dict_of_pages)
pdf.close()