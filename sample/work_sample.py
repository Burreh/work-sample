import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('sma_gentext.xml')
root = tree.getroot()

# Find the targeted element value with id = "42007"
target_value = None
for trans_unit in root.findall('.//trans-unit'):
    if trans_unit.get('id') == '42007':
        target_element = trans_unit.find('target')
        if target_element is not None:
            target_value = target_element.text
        break

# Write the value to a file
if target_value is not None:
    with open('test42007.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(target_value)
    print('Value written to test42007.txt')
else:
    print('Value not found')
