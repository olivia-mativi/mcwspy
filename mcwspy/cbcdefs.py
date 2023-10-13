""" cbcdefs - A MasterControl WebServices API Abstration Extension Module in Python
    Copyright (C) 2023  Olivia Mativi

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>."""

from mcwspy import Session, SearchParameter, SearchParameters
from typing import List, Any
import json
excludeList = ["ANONYMOUS", "APIUSER", "PLACEHOLDER_BASIC", "PLACEHOLDER_FULL", "SYSADMIN"]

def get_license_usage_full_basic(session: Session, exportRoles: bool, exportPath: str = None) -> str:
    data = session.getAllUsers(10000, True).json()
    fullLicenseNum = 0
    basicLicenseNum = 0
    numEmptyUsers = 0
    for i in data['result']['users']:
        if i['roles'] == [] and i['userName'] not in excludeList:
            numEmptyUsers+=1
    numUsers = len(data['result']['users']) - len(excludeList) - numEmptyUsers
    for i in data['result']['users']:
        if i['roles'] != [] and i['userName'] not in excludeList:
            if i['roles'][0]['name'].endswith('F'):
                fullLicenseNum += 1
            elif i['roles'][0]['name'].endswith('B'):
                basicLicenseNum += 1
    if exportRoles:
        f = open(exportPath, "w")
        for i in data['result']['users']:
            if i['roles'] != [] and i['userName'] not in excludeList:
                f.write(i['userName'] + "\n")
                for j in i['roles']:
                    f.write("\t" + j['name'] + "\n")
        f.close()
    return ("Total Users: " + str(numUsers) + 
            "\nFull Licenses: " + str(fullLicenseNum) + 
            "\nBasic Licenses: " + str(basicLicenseNum))

def get_approved_draft_pdfs(session: Session) -> None:
    return

def get_released_document_infocard_attributes(session: Session, attribute: str, sorted: bool, path: str) -> List[str]:
    a = SearchParameter(None,"VAULT_NAME","","and","like","CBC Public")
    b = SearchParameter(None,"DOCUMENT_NUM","","and","notlike","TMPL")
    c = SearchParameter(None,"DOCUMENT_NUM","","and","notlike","ORG")
    d = SearchParameter(None,"VAULT_NAME","","and","notlike","CBC Public Published-Draft")
    e = SearchParameter(None,"VAULT_NAME","","and","notlike","CBC Public Native-Draft")
    f = SearchParameter(None,"VAULT_NAME","","and","notlike","CBC Public Published-Archive")
    g = SearchParameter(None,"VAULT_NAME","","and","notlike","CBC Public Native-Archive")

    sps = SearchParameters([a,b,c,d,e,f,g])
    arg = session.build_search_arguments(sps.dict, "infocards")
    reqdict = (session.build_request_json("search","searchService",**arg))
    searchResult = session.search(reqdict)
    data = json.dumps(searchResult)
    data = json.loads(data)
    attributeList = []
    for row in data["result"]["rows"]:
        for column in row["columns"]:
            if column["key"] == attribute:
                attributeList.append(column["value"])
    if sorted: attributeList.sort()
    outString = ""
    for attribute in attributeList:
        outString += str(attribute) + "\n"
    f = open(path, "w")
    f.write(outString)
    f.close()
    return outString