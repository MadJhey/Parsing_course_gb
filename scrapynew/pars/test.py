import sys
from sys import Path


file = Path('__ file __'). resolve()
package_root_directory = file.parents [1]
# sys.path.append(str(package_root_directory))
print(str(package_root_directory))
# //from parser.items import ParserItem
