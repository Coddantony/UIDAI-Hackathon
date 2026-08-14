import xml.etree.ElementTree as ET


ALLOWED_FIELDS = ("name", "dob", "gender")


def parse_xml(data):
    """Extract the supported identity attributes from an eKYC XML payload."""
    if not data or not isinstance(data, str):
        return {}

    try:
        root = ET.fromstring(data)
        poi = root.find("UidData/Poi")
        if poi is None:
            return {}
        return {
            field: poi.attrib[field]
            for field in ALLOWED_FIELDS
            if field in poi.attrib
        }
    except (ET.ParseError, ValueError, TypeError):
        return {}
