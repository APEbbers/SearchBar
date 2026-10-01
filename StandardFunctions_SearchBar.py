def ReturnXML_Value(
    path: str, ElementName: str, attribKey: str = "", attribValue: str = ""
):
    import defusedxml.ElementTree as ET
    import os
 
    # Passing the path of the
    # xml document to enable the
    # parsing process
    PackageXML = os.path.join(os.path.dirname(__file__), path)
    tree = ET.parse(PackageXML)
    # getting the parent tag of
    # the xml document
    root = tree.getroot()
    result = ""
    for child in root:
        if str(child.tag).split("}")[1] == ElementName:
            if attribKey != "" and attribValue != "":
                for key, value in child.attrib.items():
                    if key == attribKey and value == attribValue:
                        result = child.text
                        return result
            else:
                result = child.text
    return result


def ReturnXML_Value_Git(
    User="APEbbers",
    Repository="FreeCAD-Ribbon",
    Branch="main",
    File="package.xml",
    ElementName: str = "",
    attribKey: str = "",
    attribValue: str = "",
    host="https://codeberg.org/",
):
    import requests_local as requests
    import defusedxml.ElementTree as ET

    result = None
    try:
        if host.endswith("/") is False:
            host = host + "/"
        
        # Passing the path of the
        # xml document to enable the
        # parsing process
        url = f"{host}/{User}/{Repository}/{Branch}/{File}"
        response = requests.get(url)
        data = response.content
        root = ET.fromstring(data)
        result = ""
        for child in root:
            if str(child.tag).split("}")[1] == ElementName:
                if attribKey != "" and attribValue != "":
                    for key, value in child.attrib.items():
                        if key == attribKey and value == attribValue:
                            result = child.text
                            return result
                else:
                    result = child.text
    except Exception:
        pass
    return result
