import xml.etree.ElementTree as ET


def is_well_formed_xml(data: str) -> bool:
    if not isinstance(data, str) or not data.strip():
        return False
    try:
        ET.fromstring(data)
        return True
    except ET.ParseError:
        return False
