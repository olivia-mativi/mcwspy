""" mcwspy - A MasterControl WebServices API Abstraction Module in Python
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

import os
import requests                # https://requests.readthedocs.io/en/latest/
from dotenv import load_dotenv # https://github.com/theskumar/python-dotenv
from struct import Struct
from typing import List, Any
import json


class CustomField:
    def __init__(self,
                 identifier: str = None,
                 isRequired: bool = None,
                 label: str = None,
                 type: str = None,
                 values: List = None) -> None:
        pass


class CustomFieldTaskOption:
    def __init__(self, customFields: List[CustomField], _CF: CustomField = None) -> None:
        pass


class TaskStep:
    def __init__(self, stepID: str = None, stepName: str = None) -> None:
        pass


class TaskSignoffStatus:
    def __init__(self, commentsAllowed: bool = None, 
                 commentsRequired: bool = None, 
                 hasRejectToStep: bool = None,
                 id: str = None,
                 name: str = None,
                 rejectableSteps: List = None,
                 setDates: bool = None,
                 statusSteps: List = None,
                 translatedName: str = None) -> None:
        pass


class Task:
    def __init__(self, _signOffStatus: TaskSignoffStatus) -> None:
        pass


class PacketTypeInformation:
    def __init__(self,
                 allowAttachmentsAndLinksOnAllSteps: bool = None,
                 allowPacketToBeEditedDuringChangeRequest: bool = None,
                 enableChildTaskNumberingSeries: bool = None,
                 enableDueDate: bool = None,
                 requireChangeRequest: bool = None,
                 selectedLaunchableProcessWorkflows: List[str] = None) -> None:
        pass


class PacketContentOptions:
    def __init__(self,
                 dispositionEnabled: bool = None,
                 optionalCustomFields: List[CustomField] = None,
                 requiredCustomFields: List[CustomField] = None,
                 useCustomFieldsForDisposition: bool = None) -> None:
        pass


class OptionalPacketSections:
    def __init__(self,
                 customFieldsEnabled: bool = None,
                 optionalCustomFields: List[CustomField] = None,
                 regulatoryAffairsAssessmentEnabled: bool = None,
                 requiredCustomFields: List[CustomField] = None,
                 riskAssessmentEnabled: bool = None,
                 supportingInformationEnabled: bool = None,
                 validationEnabled: bool = None,
                 verificationEnabled: bool = None) -> None:
        pass


class PacketType:
    def __init__(self,
                 defaultWorkflows: List[str],
                 isAdvanced: bool,
                 name: str,
                 numberingSeries: str,
                 businessUnits: List[str] = None,
                 optionalPacketSections: OptionalPacketSections = None,
                 packetContentOptions: PacketContentOptions = None,
                 packetTypeInformation: PacketTypeInformation = None) -> None:
        self.defaultWorkflows = defaultWorkflows
        self.isAdvanced = isAdvanced
        self.name = name
        self.numberingSeries = numberingSeries
        self.businessUnits = businessUnits
        self.optionalPacketSections = optionalPacketSections
        self.packetContentOptions = packetContentOptions
        self.packetTypeInformation = packetTypeInformation
        if(type(self.optionalPacketSections) != OptionalPacketSections):
            pass
        if(type(self.packetContentOptions) != PacketContentOptions):
            pass
        if(type(self.packetTypeInformation) != PacketTypeInformation):
            pass


class File:
    def __init__(self,
                 checksum: str = None,
                 content: bin = None,
                 fileName: str = None,
                 id: str = None,
                 message: str = None,
                 mimeType: str = None,
                 size: int = None,
                 url: str = None) -> None:
        pass


class KeyValuePair:
    def __init__(self, Key=None, Value=None) -> None:
        self.Key = Key
        self.Value = Value
        pass


class InfoCardPhaseList:
    def __init__(self, allPhases: List = None, infocardID: str = None,
                 infoCardNumber: str = None, invalidPhases: List = None,
                 revision: str = None, selectedPhaseID: str = None,
                 validPhases: List = None) -> None:
        pass


class DispositionFields:
    def __init__(self,
                 hasCustomFields: bool,
                 inventory: str,
                 market: str,
                 WIP: str,
                 _CF: CustomField = None,
                 customFields: List = None) -> None:
        pass


class AdvancedPacketTaskOptionFile:
    def __init__(self, fileName: str, id: str) -> None:
        pass


class InfoCard:
    def __init__(self,
                 action: str = None,
                 attachments: List = None,
                 author: str = None,
                 changeNumber: str = None,
                 completed=None, 
                 created=None, 
                 customFields: List[KeyValuePair] = None,
                 effective=None,
                 expiration=None,
                 file: File = None,
                 formFields: List = None,
                 infoCardID: str = None,
                 infoCardNumber: str = None,
                 infocardtype: str = None,
                 lifecycle: str = None,
                 message: str = None,
                 notes: str = None,
                 owner: str = None,
                 previousNumber: str = None,
                 released=None,
                 revision: str = None,
                 status: str = None,
                 subtype: str = None,
                 taskName: str = None,
                 title: str = None,
                 type: str = None,
                 vault: str = None,
                 workflowName: str = None) -> None:
        pass


class AdvancedPacketTaskOption:
    def __init__(self,
                 isRequired: bool,
                 optionName: str,
                 typeID: int,
                 _fileAttachments: List[AdvancedPacketTaskOptionFile] = None,
                 _infoCardLinks: InfoCard = None,
                 details: str = None,
                 fileAttachments: List[AdvancedPacketTaskOptionFile] = None,
                 infoCardLinks: List[InfoCard] = None,
                 justification: str = None) -> None:
        pass


class AdvancedPacketTaskContent:
    def __init__(self,
                 hasCourseInfoCardLink: bool,
                 hasDispositionFields: bool,
                 id: str,
                 isTrainingRequired: bool,
                 _keyValuePair: KeyValuePair = None,
                 changeDescription: str = None,
                 dispositionFields: DispositionFields = None,
                 notes: str = None,
                 reasonForChange: str = None,
                 trainingJustification: str = None) -> None:
        pass


class AdvancedPacketTask:
    def __init__(self,
                 isChangeRequest: bool,
                 proposedChanges: str,
                 reasonForChanges: str,
                 taskContents: List[AdvancedPacketTaskContent],
                 taskNumber: str,
                 taskOptions: List[AdvancedPacketTaskOption],
                 _customFieldtaskOption: CustomFieldTaskOption = None,
                 dueDate=None,
                 expirationDate=None) -> None:
        pass


class AdvancedPacketType:
    def __init__(self, numberingSeries: str, packetTypeName: str,
                 allowAttachmentsAndLinksOnAllSteps: bool = None,
                 allowPacketToBeEditedDuringChangeRequestStep: bool = None,
                 defaultWorkflows: List = None,
                 dispositionCustomFields: Struct = None,
                 dispositionEnabled: bool = None,
                 enableChildTaskNumberingSeries: bool = None,
                 enableDueDate: bool = None,
                 enablePacketSectionCustomFields: bool = None,
                 packetSectionCustomFields: Struct = None,
                 regulatoryAffairsAssessment: bool = None,
                 requireChangeRequestStepOnWorkflow: bool = None,
                 riskAssessment: bool = None,
                 selectedProcessWorkflows: List = None,
                 supportingInformation: bool = None,
                 useCustomFieldsForDisposition: bool = None,
                 validation: bool = None,
                 verification: bool = None) -> None:
        pass


class MissingEnvironmentVariableError(Exception):
    def __init__(self, missingVal: str) -> None:
        """Handles missing environment variables with a little more detail

        Args:
            missingVal (str): Value that is missing from the environment variable in .env
        """
        super().__init__("\n===\nMissing value for environment variable "+missingVal+"; please create/open .env and add the missing value.\n===")
    pass


class User:
    def __init__(self, address1: str = None, address2: str = None, changeApproveOnNextLogin: str = None,
                 changePasswordOnNextLogin: str = None, city: str = None, company: str = None,
                 country: str = None, createdate = None, createdBy: str = None, deleteDate = None,
                 department: str = None, displayName: str = None, email: str = None,
                 employeeNumber: str = None, enabled: bool = None, esigLocked: str = None,
                 esigPassword: str = None, fax: str = None, firstName: str = None,
                 lastName: str = None, loginLocked: str = None, message: str = None,
                 password: str = None, phone: str = None, roles: List = None,
                 state: str = None, suffix: str = None, supervisor: str = None,
                 title: str = None, userGUID: str = None, userID: str = None,
                 userName: str = None, zipcode: str = None) -> None:
        pass


class Comment:
    def __init__(self, body: str = None, creationDate: str = None,
                 message: str = None, rowID: str = None,
                 user: User = None) -> None:
        pass


class Comments:
    def __init__(self, comments: List[Comment] = None, message: str = None) -> None:
        pass


class Version:
    def __init__(self, application: str = None, version: str = None) -> None:
        pass


class InfoCardType:
    def __init__(self, name: str, type: str) -> None:
        """An InfoCard Type object for use in creating or modifying IC Types and their relationships.

        Args:
            name (str): the name of the infocard type
            type (str): the type of the infocard type. valid options: "Document", "Organizer",
            "Form Template", "Form", "Course", "Job Code", "Trainee", "Trainer", "Exam",
            "Project Templates", "Projects", "BOM", "Submissions Locker", "Supplier",
            "Audit Checklist", "Audit", "Risk File", "Audit Entity", "Word Template",
            "GCP Study", and "GLP Study".
        """
        pass


class EBUEntity:
    def __init__(self, name: str = None, type: str = None) -> None:
        pass
        

class ExamAnswer:
    def __init__(self, answerID: str = None, correct: str = None,
                 correctOrder=None, displayOrder=None, matchText: str = None,
                 questionID: str = None, text: str = None) -> None:
        pass


class ExamQuestion:
    def __init__(self, _a: ExamAnswer = None, answers: List[ExamAnswer] = None,
                 correctAnswer: str = None, desc: str = None, examID: str = None,
                 failIfWrong=None, order=None, points: int=None,
                 questionID: str = None, required=None, text: str = None,
                 type: str = None) -> None:
        pass


class Exam:
    def __init__(self, _a: ExamAnswer = None, _q: ExamQuestion = None,
                 questions: List[ExamQuestion]=None) -> None:
        pass


class BinaryFile:
    def __init__(self, checksum: str = None, content: bin = None,
                 filename: str = None, message: str = None,
                 mimeType: str = None) -> None:
        pass


class Query:
    def __init__(self, name: str = None, qArray: List = None) -> None:
        pass


class Vault:
    def __init__(self, description: str = None, id: str = None,
                 message: str = None, name: str = None) -> None:
        pass


class Vaults:
    def __init__(self, vaults: List[Vault] = None) -> None:
        pass


class FileLite:
    def __init__(self, fileName: str = None, message: str = None, url: str = None) -> None:
        pass


class WebLink:
    def __init__(self, message: str = None, url: str = None) -> None:
        pass


class HTMLForm:
    def __init__(self, data: str = None, result: str = None) -> None:
        pass


class InfoCardImportItem:
    def __init__(self, infoCardNumberOrNumberingSeries: str, infoCardType: str,
                 lifecycle: str, revision: str, title: str, author: str = None,
                 changeNumber: str = None, createCourse: bool = False,
                 documentConnectionsURL: str = None, effectiveDate: str = None,
                 expirationDate: str = None, filePath: str = None,
                 lastReviewDate: str = None, notes: str = None,
                 owner: str = None, releaseDate: str = None,
                 previousNumber: str = None, revisionOrdinalNumber: int = None,
                 subtype: str = None, useNumberingSeries: bool = False) -> None:
        pass


class User:
    def __init__(self, active: int = None, address1: str = None, address2: str = None,
                 changeApproveOnNextLogin: str = None, changePasswordOnNextLogin: str = None,
                 city: str = None, company: str = None, country: str = None,
                 createDate: str = None, createdBy: str = None, deleteDate: str = None,
                 department: str = None, displayName: str = None, email: str = None,
                 employeeNumber: str = None, enabled: bool = False, esigLocked: str = None,
                 esigPassword: str = None, fax: str = None, firstName: str = None,
                 jobTitle: str = None, lastName: str = None, loginLocked: str = None,
                 message: str = None, password: str = None, phone: str = None,
                 roles: List = None, state: str = None, suffix: str = None,
                 supervisor: str = None, title: str = None, userGUID: str = None,
                 userID: str = None, userName: str = None, zipCode: str = None) -> None:
        pass


class ContactInformation:
    def __init__(self, address1: str = None, address2: str = None,
                 city: str = None, company: str = None, country: str = None,
                 fax: str = None, phone: str = None, state: str = None,
                 zipCode: str = None) -> None:
        pass


class UserInformation:
    def __init__(self, active: int = None,
                 createDate: str = None, createdBy: str = None, deleteDate: str = None, 
                 department: str = None, displayName: str = None, email: str = None, 
                 employeeNumber: str = None, enabled: bool = False, esigLocked: str = None, 
                 esigPassword: str = None, firstName: str = None, 
                 jobTitle: str = None, lastName: str = None, loginLocked: str = None, 
                 message: str = None, password: str = None, 
                 supervisor: str = None, title: str = None, userGUID: str = None, 
                 userID: str = None, userName: str = None) -> None:
        pass


class FullUser:
    def __init__(self, contactInformation: ContactInformation = None,
                 userInformation: UserInformation = None) -> None:
        pass


class Users:
    def __init__(self, message: str = None, users: List[User] = None) -> None:
        pass


class UploadBatchFile:
    def __init__(self, fileName: str, filePath: str, mimeType: str) -> None:
        pass


class SearchParameter:
    def __init__(self, custom: bool = None, identifier: str = None,
                 label: str = None, logic: str = None, operator: str = None,
                 value: str = None) -> None:
        """_summary_ A search parameter object that houses and generates JSON to be used in search queries.

        Args:
            custom (bool, optional): _description_. Custom Field Identifier. Defaults to None.
            identifier (str, optional): _description_. Defaults to None.
            label (str, optional): _description_. Defaults to None.
            logic (str, optional): _description_. And/Or. Defaults to None.
            operator (str, optional): _description_. =/!=/>=/<=/>/</like/notlike/starts/ends. Defaults to None.
            value (str, optional): _description_. Value to compare. Defaults to None.
        """
        self.custom = custom
        self.identifier = identifier
        self.label = label
        self.logic = logic
        self.operator = operator
        self.value = value
        self.dict = {
            "operator": self.operator,
            "custom": str(self.custom),
            "label": self.label,
            "identifier": self.identifier,
            "value": self.value,
            "logic": self.logic
        }


class SearchParameters:
    def __init__(self, parameters: List[SearchParameter] = None) -> None:
        self.dict = {
            "searchParameters":{
                "message":"",
                "parameters":[]
            }
        }
        #create a list that is the attributes of the params
        self.paramAttributes = []
        for param in parameters:
            self.paramAttributes.append(param.dict)
        self.dict["searchParameters"]["parameters"].extend(self.paramAttributes)
        self.json = json.dumps(self.dict, indent=4)
        

class Row:
    def __init__(self, columns: List[KeyValuePair] = None) -> None:
        self.columns = columns


class RecordSet:
    def __init__(self, columnList: str = None, recordCount: int = None, rows: List[Row] = None) -> None:
        self.columnList = columnList
        self.recordCount = recordCount
        self.rows = rows


class Session:
    def __init__(self, logout: bool=False) -> None:
        """Creates a new MasterControl WS Session. Site URL and API key must be
        set in a .env file.

        Args:
            logout (bool, optional): Logout current web connection. Defaults to False.
        """
        load_dotenv()
        try:
            self.url = os.environ["SITE_URL"]
        except KeyError:
            raise MissingEnvironmentVariableError("SITE_URL")
        try:
            self.key = os.environ["API_KEY"]
        except KeyError:
            raise MissingEnvironmentVariableError("API_KEY")
        self.authJSON = {
                        "arguments":
                        {
                            "apiKey":self.key,
                            "logoutCurrentWebConnection":str(logout).lower()
                        },
                        "methodName":"connectWithApiKey",
                        "serviceName":"ConnectionService"
                        }
        self.connectionID = requests.post(self.url, json = self.authJSON).json()['result']
        print("Session Initialized: " + self.connectionID)
    
    def build_search_arguments(self, searchParameters: dict, listPage: str):
        searchArgs = {
            "connectionID":self.connectionID,
            "list":listPage
        }
        searchArgs.update(searchParameters)
        #searchParameters["list"] = listPage
        #searchParameters["connectionID"] = self.connectionID
        return searchArgs

    def build_request_json(self, methodName: str, serviceName: str, **kwargs) -> dict:
        dict = {
            "serviceName":serviceName,
            "methodName":methodName,
            "arguments":kwargs
        }
        return dict

    # AdvancedPacketService Methods

    def get_advanced_packet_task(self, task: Task) -> AdvancedPacketTask:
        pass

    def get_packet_type(self, packetName: str) -> PacketType:
        reqjson = self.build_request_json("getPacketType", 
                                       "AdvancedPacketService",
                                       **{"packetName":packetName,
                                          "connectionID":self.connectionID})
        result = requests.get(self.url, json=reqjson)
        result = result.json()
        pktType = PacketType(result["result"]["defaultWorkflows"],
                             result["result"]["isAdvanced"],
                             result["result"]["name"],
                             result["result"]["numberingSeries"],
                             result["result"]["businessUnits"],
                             result["result"]["optionalPacketSections"],
                             result["result"]["packetContentOptions"],
                             result["result"]["packetTypeInformation"])
        return pktType

    def get_packet_types(self, filter: str = None) -> List[PacketType]:
        pass

    def get_advanced_packet_task_with_packet_id(self, packetID: str) -> AdvancedPacketTask:
        pass

    def create_advanced_packet_type(self, 
                                 advancedPacketTypeOptions: AdvancedPacketType, 
                                 businessUnits: List[str]) -> bool:
        pass

    # ApprovalService Methods

    def approve_simple_task(self, parallelID: str, packetID: str,
                          packetStep: str, status: str, password: str,
                          packetName: str, comments: str) -> str:
        pass

    def approve_training_task(self, parallelID: str, packetID: str,
                          packetStep: str, status: str, password: str,
                          packetName: str, comments: str) -> str:
        pass

    def approve_document_task(self, parallelID: str, packetID: str,
                          packetStep: str, status: str, password: str,
                          packetName: str, comments: str, effectiveDate: str = None,
                          expirationDate: str = None, phases: InfoCardPhaseList = None) -> str:
        pass

    def are_dates_needed_on_approval(self, packetID: str, packetStep: str, parallelID: str) -> bool:
        pass

    def approve_collaboration(self, packetid: str, stepid: str, packetName: str,
                             signoff: str, password: str, comments: str) -> str:
        pass

    # AuditService Methods
    # BillOfMaterialsService Methods
    # CommentService Methods

    def get_comments(self, task: Task) -> Comments:
        pass

    def add_comment(self, comment: str, task: Task) -> Comment:
        pass

    # ConnectionService Methods

    def connect(self, userID: str, password: str, logoutCurrentWebConnection: bool = False, useOkta: bool = False) -> str:
        pass

    def connect_with_api_key(self, apikey: str, logoutCurrentWebConnection: bool = False) -> str:
        pass

    def disconnect(self) -> bool:
        pass

    def is_connected(self) -> bool:
        pass

    def get_user_id(self) -> str:
        pass

    def get_version(self) -> Version:
        pass

    def return_version(self, version: Version) -> Version:
        pass

    # CopyService Methods

    def email(self, infoCardNumber: str, revision: str, 
              emailAddresses: str, emailSubject: str = None, emailMessage: str = None, 
              usePublished: bool=False) -> str:
        pass

    # CustomFieldService Methods

    def assign_custom_fields_to_infocard_types(self, 
                                               infoCardTypes: List[InfoCardType],
                                               customFields: List[CustomField],
                                               changeReason: str) -> bool:
        pass

    # DatasetService Methods

    def get_dataset_data(self, datasetName: str, recordID: str) -> str:
        pass

    def get_external_data_set_as_json(self, datasetName: str, parameters: Struct) -> str:
        pass

    # DataStructureService Methods

    def get_external_data_structure_data(self, externalDataStructureName: str,
                                         filterParameters: List = None, returnQuery: bool = None) -> any:
        pass

    # EnterpriseBusinessUnitService Methods

    def assign_business_unit_to_entities(self, businessUnitNames: List[str],
                                         entities: List[EBUEntity], changeReason: str = None) -> bool:
        pass

    # ExamService Methods

    def get_exam(self, examID: str) -> Exam:
        pass

    def score_exam(self, examID: str, packetID: str, answerStruct: List[ExamAnswer], isPreExam=None) -> bool:
        pass

    def get_exam_results(self, examPerformanceID: str) -> Exam:
        pass

    # ExternalGUIService Methods

    def get_external_route_builder_url(self, routeID: str, closeMethod: str = None, exitURL: str = None,
                                       showChangeRequest: bool = None, showNotify: bool = None,
                                       showEscalation: bool = None, showShredRedlines: bool = None,
                                       showModifyUserOptions: bool = None) -> str:
        pass

    def get_external_collaboration_url(self, taskID: str, closeMethod: str = None, exitURL: str = None) -> str:
        pass

    # ExternalTraining Methods

    def import_training(self, userName: str, courseName: str, courseNumber: str, completionDate: str,
                        source: str, score: str, status: str, courseDescription: str,
                        attachment: BinaryFile) -> str:
        pass

    # FileLibraryService Methods

    def get_library_info(self, formatTimes: bool = None) -> Query:
        pass

    # FileService Methods

    def get_binary_pdf(self, infoCardNumber: str, revision: str, pdfType: str, trainingCourseID: str = None) -> BinaryFile:
        pass

    def get_pdf(self, infoCardNumber: str, revision: str, pdfType: str, directoryPath: str = None, trainingCourseID: str = None) -> FileLite:
        """DEPRECATED FOR CLOUD-BASED SYSTEMS

        Args:
            infoCardNumber (str): _description_
            revision (str): _description_
            pdfType (str): _description_
            directoryPath (str, optional): _description_. Defaults to None.
            trainingCourseID (str, optional): _description_. Defaults to None.

        Returns:
            FileLite: _description_
        """
        pass

    def get_file(self, infoCardNumber: str, revision: str, directoryPath: str = None, trainingCourseID: str = None) -> FileLite:
        """DEPRECATED FOR CLOUD-BASED SYSTEMS

        Args:
            infoCardNumber (str): _description_
            revision (str): _description_
            directoryPath (str, optional): _description_. Defaults to None.
            trainingCourseID (str, optional): _description_. Defaults to None.

        Returns:
            FileLite: _description_
        """
        pass
    
    def get_binary_file(self, infoCardNumber: str, revision: str, trainingCourseID: str = None) -> BinaryFile:
        pass

    def get_binary_attachments(self, infoCardNumber: str, revision: str) -> Struct:
        pass

    def get_file_details(self, infoCardNumber: str, infoCardRevision: str) -> List[File]:
        pass

    def upload_file(self, infoCardNumber: str, revision: str, filePath: str, fileType: str = None,
                    saveType: str = None, reason: str = None) -> FileLite:
        pass

    def upload_binary(self, infoCardNumber: str, revision: str, binaryFile: BinaryFile, fileType: str = None,
                      saveType: str = None, reason: str = None) -> BinaryFile:
        pass

    def get_file_link_by_infocard_number_and_rev(self, infoCardNumber: str, revision: str, securityType: str,
                                                 linkType: str) -> WebLink:
        pass

    def get_file_link(self, infoCardID: str, securityType: str, linkType: str) -> WebLink:
        pass

    def get_file_link_by_num_rev(self, infoCardNumber: str, revision: str, securityType: str,
                                 linkType: str) -> WebLink:
        pass

    def get_latest_redline_binary_file(self, taskID: str, docNum: str, docRev: str) -> BinaryFile:
        pass

    def get_binary_sub_file(self, infoCardID: str, subFileID: str) -> BinaryFile:
        pass

    def is_connection_valid(self) -> bool:
        pass

    # HTMLFormService Methods

    def get_html_form(self, packetID: str, packetName: str, stepID: str, pStepID: str, event: str, 
                      altUser: str, formTemplate: str, formID: str) -> HTMLForm:
        pass

    def get_html_form_in_json(self) -> HTMLForm:
        pass

    def add_attachment(self, formID: str, fieldName: str, fileName: str, base64) -> str:
        pass

    def get_max_array_id_for_field(self, formID: str, fieldID: str) -> int:
        pass

    def get_form_id(self, packetID: str) -> str:
        pass

    def get_attachments(self, formID, fieldName) -> Query:
        pass

    def get_attachment_info(self, attachmentID: str, formID: str) -> Struct:
        pass
    
    def remove_attachment(self, attachmentID, fieldName, formID) -> bool:
        pass

    def can_edit_attachments(self, packetID: str, currentStepID: str, pageNumber: str) -> bool:
        pass

    # ImportService Methods

    def infocard_import(self, infoCardImportItems: List[InfoCardImportItem]) -> Struct:
        pass

    def upload_files_for_batch(self, batchName: str) -> List[UploadBatchFile]:
        pass
    
    def get_files_for_batch(self, batchName: str) -> List[UploadBatchFile]:
        pass

    # InfocardService Methods
    # InfoCardTypeService Methods
    # LicenseService Methods
    # LifecycleService Methods
    # NumberingSeriesService Methods
    # RecallService Methods
    # RouteService Methods
    # SearchService Methods

    def get_json_search_fields(self, list: str) -> SearchParameters:
        pass

    def search(self, searchdict: dict) -> Any:
        response = requests.get(self.url, json=searchdict)
        return response.json()

    # SignatureService Methods
    # SupplierService Methods
    # TaskService Methods
    # TaskStepService Methods
    # Training Methods
    # TrainingClassAttendance Methods
    # TrainingImportService Methods
    # TrainingTaskFileService Methods
    # TypeService Methods
    # UserService Methods

    def get_all_users(self, includeRoleMembership: bool = False, startIndex: int = None,
                      count: int = None) -> Users:
        pass

    def get_user_locale(self, userID: str = None) -> str:
        pass

    def get_user_by_id(self, userID: str) -> User:
        pass
    
    def get_full_user_by_user_name(self, userName: str) -> FullUser:
        pass
    
    def change_time_zone(self, timeZone: str, editedUserID: str = None) -> bool:
        pass

    def change_language(self, language: str) -> bool:
        pass

    def create_user(self, user: User, activeDirectoryUserName: str = None,
                    activeDirectory: str = None) -> bool:
        pass

    def update_user(self, user: User, contactInformation: ContactInformation = None, reason: str = None) -> bool:
        pass

    def add_user_to_role(self, userID: str, roleName: str) -> bool:
        pass

    def get_all_roles(self, includeUserMembership: bool = False, startIndex: int = None, count: int = None) -> List:
        pass

    def delete_user_from_role(self, userID: str, roleName: str, clearCache: bool = False) -> bool:
        pass

    def is_member(self, userID: str, roleName: str) -> bool:
        pass

    def get_members(self, roleName: str) -> Any:
        pass


    # VaultService Methods

    def get_all_vaults(self) -> Vaults:
        reqJSON = {"arguments":{"connectionID":self.connectionID},
                "methodName":"getAllVaults","serviceName":"VaultService"}
        vaultsJSON = requests.get(self.url, json = reqJSON)
        pass

    def get_doc_view_vaults(self) -> Vaults:
        pass

    def get_lifecycles_for_user(self, lifecyclePhaseOrder: str = None, rightName: str = None) -> Any:
        pass

    def update_vault(self, vaultName: str, newVaultName: str = None, vaultDescription: str = None,
                     enterpriseBusinessUnits: List = None) -> bool:
        pass






    def getAllUsers(self, numUsers : int, includeRoles : bool = False):
        reqJSON = {
        "arguments":{
            "count":numUsers,
            "startIndex":"1",
            "connectionID":self.connectionID,
            "includeRoleMembership":str(includeRoles).lower()
        },
        "methodName":"getAllUsers",
        "serviceName":"UserService"}
        return requests.get(self.url, json = reqJSON)
    def getAllDepartments(self):
        reqJSON = {
        "arguments":{"connectionID":self.connectionID},
        "methodName":"getAllDepartments",
        "serviceName":"UserService"}
        return requests.get(self.url, json = reqJSON)
    def getSystemRights(self, viewOnly : bool):
        reqJSON = {
        "arguments":{
            "connectionID":self.connectionID,
            "viewOnly":viewOnly
        },
        "methodName":"getSystemRights",
        "serviceName":"UserService"}
        return requests.get(self.url, json = reqJSON)
    def getRoleMembers(self, roleName : str):
        reqJSON = {
        "arguments":{
            "connectionID":self.connectionID,
            "roleName":roleName
        },
        "methodName":"getMembers",
        "serviceName":"UserService"}
        return requests.get(self.url, json = reqJSON)
    def getAllRoles(self, numRecords : int, includeUsers : bool):
        reqJSON = {
        "arguments":{
            "count":numRecords,
            "startIndex":"1",
            "connectionID":self.connectionID,
            "includeUserMembership":str(includeUsers).lower()
        },
        "methodName":"getAllRoles",
        "serviceName":"UserService"}
        return requests.get(self.url, json = reqJSON) 

    

