import pandas as pd  
  
# Read the CSV file  
df = pd.read_csv('drugsatfda20230620/ApplicationDocs.txt', sep='\t', encoding='ISO-8859-1')  
  
# Extract unique URLs from the ApplicationDocsURL field  
urls = set(df['ApplicationDocsURL'])  
  
# Create an HTML file with the URLs as hyperlinks  
with open('urls.html', 'w') as file:  
    # Write the basic HTML structure  
    file.write('<!DOCTYPE html>\n')  
    file.write('<html lang="en">\n')  
    file.write('<head>\n')  
    file.write('<meta charset="UTF-8">\n')  
    file.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')  
    file.write('<title>URLs from ApplicationDocs</title>\n')  
    file.write('</head>\n')  
    file.write('<body>\n')  
    file.write('<h1>URLs from ApplicationDocs</h1>\n')  
    file.write('<ul>\n')  
  
    # Loop through the URLs and write them as list items with hyperlinks  
    for url in urls:  
        file.write(f'<li><a href="{url}">{url}</a></li>\n')  
  
    # Close the HTML structure  
    file.write('</ul>\n')  
    file.write('</body>\n')  
    file.write('</html>\n')  
