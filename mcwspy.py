import os
import requests                # https://requests.readthedocs.io/en/latest/
from dotenv import load_dotenv # https://github.com/theskumar/python-dotenv
from array import array
from struct import Struct


class CustomField:
    def __init__(self,
                 identifier: str = None,
                 isRequired: bool = None,
                 label: str = None,
                 type: str = None,
                 values: array = None) -> None:
        pass


class CustomFieldTaskOption:
    def __init__(self, customFields: array[CustomField], _CF: CustomField = None) -> None:
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
                 rejectableSteps: array = None,
                 setDates: bool = None,
                 statusSteps: array = None,
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
                 selectedLaunchableProcessWorkflows: array[str] = None) -> None:
        pass


class PacketContentOptions:
    def __init__(self,
                 dispositionEnabled: bool = None,
                 optionalCustomFields: array[CustomField] = None,
                 requiredCustomFields: array[CustomField] = None,
                 useCustomFieldsForDisposition: bool = None) -> None:
        pass


class OptionalPacketSections:
    def __init__(self,
                 customFieldsEnabled: bool = None,
                 optionalCustomFields: array[CustomField] = None,
                 regulatoryAffairsAssessmentEnabled: bool = None,
                 requiredCustomFields: array[CustomField] = None,
                 riskAssessmentEnabled: bool = None,
                 supportingInformationEnabled: bool = None,
                 validationEnabled: bool = None,
                 verificationEnabled: bool = None) -> None:
        pass


class PacketType:
    def __init__(self,
                 defaultWorkflows: array[str],
                 isAdvanced: bool,
                 name: str,
                 numberingSeries: str,
                 businessUnits: array[str] = None,
                 optionalPacketSections: OptionalPacketSections = None,
                 packetContentOptions: PacketContentOptions = None,
                 packetTypeInformation: PacketTypeInformation = None) -> None:
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
    def __init__(self, allPhases: array = None, infocardID: str = None,
                 infoCardNumber: str = None, invalidPhases: array = None,
                 revision: str = None, selectedPhaseID: str = None,
                 validPhases: array = None) -> None:
        pass


class DispositionFields:
    def __init__(self,
                 hasCustomFields: bool,
                 inventory: str,
                 market: str,
                 WIP: str,
                 _CF: CustomField = None,
                 customFields: array = None) -> None:
        pass


class AdvancedPacketTaskOptionFile:
    def __init__(self, fileName: str, id: str) -> None:
        pass


class InfoCard:
    def __init__(self,
                 action: str = None,
                 attachments: array = None,
                 author: str = None,
                 changeNumber: str = None,
                 completed=None, 
                 created=None, 
                 customFields: array[KeyValuePair] = None,
                 effective=None,
                 expiration=None,
                 file: File = None,
                 formFields: array = None,
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
                 _fileAttachments: array[AdvancedPacketTaskOptionFile] = None,
                 _infoCardLinks: InfoCard = None,
                 details: str = None,
                 fileAttachments: array[AdvancedPacketTaskOptionFile] = None,
                 infoCardLinks: array[InfoCard] = None,
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
                 taskContents: array[AdvancedPacketTaskContent],
                 taskNumber: str,
                 taskOptions: array[AdvancedPacketTaskOption],
                 _customFieldtaskOption: CustomFieldTaskOption = None,
                 dueDate=None,
                 expirationDate=None) -> None:
        pass


class AdvancedPacketType:
    def __init__(self, numberingSeries: str, packetTypeName: str,
                 allowAttachmentsAndLinksOnAllSteps: bool = None,
                 allowPacketToBeEditedDuringChangeRequestStep: bool = None,
                 defaultWorkflows: array = None,
                 dispositionCustomFields: Struct = None,
                 dispositionEnabled: bool = None,
                 enableChildTaskNumberingSeries: bool = None,
                 enableDueDate: bool = None,
                 enablePacketSectionCustomFields: bool = None,
                 packetSectionCustomFields: Struct = None,
                 regulatoryAffairsAssessment: bool = None,
                 requireChangeRequestStepOnWorkflow: bool = None,
                 riskAssessment: bool = None,
                 selectedProcessWorkflows: array = None,
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
                 changePasswordOnNextLogin : str = None, city : str = None, company : str = None,
                 country : str = None, createdate = None, createdBy : str = None, deleteDate = None,
                 department : str = None, displayName : str = None, email : str = None,
                 employeeNumber : str = None, enabled : bool = None, esigLocked : str = None,
                 esigPassword : str = None, fax : str = None, firstName : str = None,
                 lastName : str = None, loginLocked : str = None, message : str = None,
                 password : str = None, phone : str = None, roles : array = None,
                 state : str = None, suffix : str = None, supervisor : str = None,
                 title : str = None, userGUID : str = None, userID : str = None,
                 userName : str = None, zipcode : str = None) -> None:
        pass


class Comment:
    def __init__(self, body: str = None, creationDate: str = None,
                 message: str = None, rowID: str = None,
                 user: User = None) -> None:
        pass


class Comments:
    def __init__(self, comments: array[Comment] = None, message: str = None) -> None:
        pass


class Version:
    def __init__(self, application: str = None, version: str = None) -> None:
        pass


class Session:
    def __init__(self, logout: bool = False) -> None:
        """Creates a new MasterControl WS Session

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
    
    # AdvancedPacketService Methods

    def get_advanced_packet_task(self, task: Task) -> AdvancedPacketTask:
        pass

    def get_packet_type(self, packetName: str) -> PacketType:
        pass

    def get_packet_types(self, filter: str = None) -> array[PacketType]:
        pass

    def get_advanced_packet_task_with_packet_id(self, packetID: str) -> AdvancedPacketTask:
        pass

    def create_advanced_packet_type(self, 
                                 advancedPacketTypeOptions: AdvancedPacketType, 
                                 businessUnits: array[str]) -> bool:
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

    def disconnect(self, connectionID: str) -> bool:
        pass

    def is_connected(self, connectionID: str) -> bool:
        pass

    def get_user_id(self, connectionID: str) -> str:
        pass

    def get_version(self) -> Version:
        pass

    def return_version(self, version: Version) -> Version:
        pass

    # CopyService Methods

    def email(self, connectionID: str, infoCardNumber: str, revision: str, 
              emailAddresses: str, emailSubject: str = None, emailMessage: str = None, 
              usePublished: bool = False) -> str:
        pass

    # CustomFieldService Methods
    # DatasetService Methods
    # DataStructureService Methods
    # EnterpriseBusinessUnitService Methods
    # ExamService Methods
    # ExternalGUIService Methods
    # ExternalTraining Methods
    # FileLibraryService Methods
    # FileService Methods
    # HTMLFormService Methods
    # ImportService Methods
    # InfocardService Methods
    # InfoCardTypeService Methods
    # LicenseService Methods
    # LifecycleService Methods
    # NumberingSeriesService Methods
    # RecallService Methods
    # RouteService Methods
    # SearchService Methods
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
    # VaultService Methods
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
    def getAllVaults(self):
        reqJSON = {"arguments":{"connectionID":self.connectionID},
                "methodName":"getAllVaults","serviceName":"VaultService"}
        return requests.get(self.url, json = reqJSON)
    

