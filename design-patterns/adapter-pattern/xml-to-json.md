

### **Example 2: Adapting Different Data Formats**

**Scenario:**

Suppose you have an application that processes employee data from various sources. Your system expects data in JSON format, but you receive data in XML format from an external service.

**Target Interface (JSON Employee Reader):**

```python
# json_employee_reader.py

import json

class JsonEmployeeReader:
    def read_employee_data(self, json_data):
        data = json.loads(json_data)
        # Process employee data
        print(f"Processing employee: {data['name']}")
```

**Adaptee (XML Data):**

```python
# xml_data_provider.py

class XmlDataProvider:
    def get_employee_xml(self):
        return """
        <employee>
            <name>Jane Doe</name>
            <position>Software Engineer</position>
        </employee>
        """
```

**Challenge:**

- The `JsonEmployeeReader` expects data in JSON format.
- The external service provides data in XML format.
- Modifying `JsonEmployeeReader` or `XmlDataProvider` is not desirable.

**Applying the Adapter Pattern:**

**Create an Adapter:**

```python
# xml_to_json_adapter.py

from json_employee_reader import JsonEmployeeReader
from xml_data_provider import XmlDataProvider
import xml.etree.ElementTree as ET
import json

class XmlToJsonAdapter(JsonEmployeeReader):
    def __init__(self, xml_provider):
        self.xml_provider = xml_provider
    
    def read_employee_data(self):
        xml_data = self.xml_provider.get_employee_xml()
        # Convert XML to JSON
        root = ET.fromstring(xml_data)
        data = {child.tag: child.text for child in root}
        json_data = json.dumps(data)
        # Call the method from JsonEmployeeReader
        super().read_employee_data(json_data)
```

**Usage in Client Code:**

```python
# client.py

from xml_data_provider import XmlDataProvider
from xml_to_json_adapter import XmlToJsonAdapter

def main():
    xml_provider = XmlDataProvider()
    adapter = XmlToJsonAdapter(xml_provider)
    adapter.read_employee_data()

if __name__ == "__main__":
    main()
```

**Output:**

```
Processing employee: Jane Doe
```

**Explanation:**

- The `XmlToJsonAdapter` inherits from `JsonEmployeeReader`.
- It overrides the `read_employee_data` method to fetch XML data and convert it to JSON.
- The adapter allows `JsonEmployeeReader` to process XML data without modification.

---
