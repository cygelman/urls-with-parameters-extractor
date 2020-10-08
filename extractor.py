import re
import os
import sys

try:
    path_to_file = sys.argv[1]
    filename = os.path.basename(path_to_file).replace('.txt','')
    way_back_file = open(path_to_file)
    content = way_back_file.read()

    urlRegex = re.compile(r'(http+.*\?+\w+=+.*)')

    result = urlRegex.findall(content)
    result_file = open(f'./{filename}_params_only.txt', 'w')
    result_filename = f'{filename}_params_only.txt'

    count = 0
    for line in result:
        result_file.write(line + '\n')
        count += 1
    
    print(f'[V] File \"{result_filename}\" saved with {count} results')
    result_file.close()
    way_back_file.close()

except:
    print('[X] Error with the file or no file specified')
    sys.exit()

# Use: python3 extractor.py FILE_NAME