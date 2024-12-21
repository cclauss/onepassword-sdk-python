"""
Generated by typeshare 1.12.0
"""

from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, ConfigDict, Field
from typing import List, Literal, Optional, Union


class GeneratePasswordResponse(BaseModel):
    """
    For future use, if we want to return more information about the generated password.
    Currently, it only returns the password itself.
    """

    password: str
    """
    The generated password.
    """


class ItemCategory(str, Enum):
    LOGIN = "Login"
    SECURENOTE = "SecureNote"
    CREDITCARD = "CreditCard"
    CRYPTOWALLET = "CryptoWallet"
    IDENTITY = "Identity"
    PASSWORD = "Password"
    DOCUMENT = "Document"
    APICREDENTIALS = "ApiCredentials"
    BANKACCOUNT = "BankAccount"
    DATABASE = "Database"
    DRIVERLICENSE = "DriverLicense"
    EMAIL = "Email"
    MEDICALRECORD = "MedicalRecord"
    MEMBERSHIP = "Membership"
    OUTDOORLICENSE = "OutdoorLicense"
    PASSPORT = "Passport"
    REWARDS = "Rewards"
    ROUTER = "Router"
    SERVER = "Server"
    SSHKEY = "SshKey"
    SOCIALSECURITYNUMBER = "SocialSecurityNumber"
    SOFTWARELICENSE = "SoftwareLicense"
    PERSON = "Person"
    UNSUPPORTED = "Unsupported"


class ItemFieldType(str, Enum):
    TEXT = "Text"
    CONCEALED = "Concealed"
    CREDITCARDTYPE = "CreditCardType"
    CREDITCARDNUMBER = "CreditCardNumber"
    PHONE = "Phone"
    URL = "Url"
    TOTP = "Totp"
    EMAIL = "Email"
    REFERENCE = "Reference"
    UNSUPPORTED = "Unsupported"


class ItemFieldDetailsTypes(str, Enum):
    OTP = "Otp"


class ItemFieldDetailsOtp(BaseModel):
    """
    The computed OTP code and other details
    """

    type: Literal[ItemFieldDetailsTypes.OTP] = ItemFieldDetailsTypes.OTP
    content: OtpFieldDetails


# Field type-specific attributes.
ItemFieldDetails = ItemFieldDetailsOtp


class ItemField(BaseModel):
    """
    Represents a field within an item.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    """
    The field's ID
    """
    title: str
    """
    The field's title
    """
    section_id: Optional[str] = Field(alias="sectionId", default=None)
    """
    The ID of the section containing the field. Built-in fields such as usernames and passwords don't require a section.
    """
    field_type: ItemFieldType = Field(alias="fieldType")
    """
    The field's type
    """
    value: str
    """
    The string representation of the field's value
    """
    details: Optional[ItemFieldDetails] = Field(default=None)
    """
    Field type-specific attributes.
    """


class ItemSection(BaseModel):
    """
    A section groups together multiple fields in an item.
    """

    id: str
    """
    The section's unique ID
    """
    title: str
    """
    The section's title
    """


class AutofillBehavior(str, Enum):
    ANYWHEREONWEBSITE = "AnywhereOnWebsite"
    EXACTDOMAIN = "ExactDomain"
    NEVER = "Never"


class Website(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    url: str
    """
    The website URL
    """
    label: str
    """
    The label of the website, e.g. 'website', 'sign-in address'
    """
    autofill_behavior: AutofillBehavior = Field(alias="autofillBehavior")
    """
    The auto-fill behavior of the website
    
    For more information, visit https://support.1password.com/autofill-behavior/
    """


class Item(BaseModel):
    """
    Represents a 1Password item.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    """
    The item's ID
    """
    title: str
    """
    The item's title
    """
    category: ItemCategory
    """
    The item's category
    """
    vault_id: str = Field(alias="vaultId")
    """
    The ID of the vault where the item is saved
    """
    fields: List[ItemField]
    """
    The item's fields
    """
    sections: List[ItemSection]
    """
    The item's sections
    """
    tags: List[str]
    """
    The item's tags
    """
    websites: List[Website]
    """
    The websites used for autofilling for items of the Login and Password categories.
    """
    version: int
    """
    The item's version
    """


class ItemCreateParams(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    category: ItemCategory
    """
    The item's category
    """
    vault_id: str = Field(alias="vaultId")
    """
    The ID of the vault where the item is saved
    """
    title: str
    """
    The item's title
    """
    fields: Optional[List[ItemField]] = Field(default=None)
    """
    The item's fields
    """
    sections: Optional[List[ItemSection]] = Field(default=None)
    """
    The item's sections
    """
    tags: Optional[List[str]] = Field(default=None)
    """
    The item's tags
    """
    websites: Optional[List[Website]] = Field(default=None)
    """
    The websites used for autofilling for items of the Login and Password categories.
    """


class ItemOverview(BaseModel):
    """
    Represents a decrypted 1Password item.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    """
    The item's ID
    """
    title: str
    """
    The item's title
    """
    category: ItemCategory
    """
    The item's category
    """
    vault_id: str = Field(alias="vaultId")
    """
    The ID of the vault where the item is saved
    """
    websites: List[Website]
    """
    The websites used for autofilling for items of the Login and Password categories.
    """


class OtpFieldDetails(BaseModel):
    """
    Additional attributes for OTP fields.
    """

    model_config = ConfigDict(populate_by_name=True)

    code: Optional[str] = Field(default=None)
    """
    The OTP code, if successfully computed
    """
    error_message: Optional[str] = Field(alias="errorMessage", default=None)
    """
    The error message, if the OTP code could not be computed
    """


class VaultOverview(BaseModel):
    """
    Represents a decrypted 1Password vault.
    """

    id: str
    """
    The vault's ID
    """
    title: str
    """
    The vault's title
    """


class PasswordRecipeMemorableInner(BaseModel):
    """
    Generated type representing the anonymous struct variant `Memorable` of the `PasswordRecipe` Rust enum
    """

    model_config = ConfigDict(populate_by_name=True)

    separator_type: SeparatorType = Field(alias="separatorType")
    """
    The type of separator between chunks.
    """
    capitalize: bool
    """
    Uppercase one randomly selected chunk.
    """
    word_list_type: WordListType = Field(alias="wordListType")
    """
    The type of word list used.
    """
    word_count: int = Field(alias="wordCount")
    """
    The number of "words" (words or syllables).
    """


class PasswordRecipePinInner(BaseModel):
    """
    Generated type representing the anonymous struct variant `Pin` of the `PasswordRecipe` Rust enum
    """

    length: int
    """
    Number of digits in the PIN.
    """


class PasswordRecipeRandomInner(BaseModel):
    """
    Generated type representing the anonymous struct variant `Random` of the `PasswordRecipe` Rust enum
    """

    model_config = ConfigDict(populate_by_name=True)

    include_digits: bool = Field(alias="includeDigits")
    """
    Include at least one digit in the password.
    """
    include_symbols: bool = Field(alias="includeSymbols")
    """
    Include at least one symbol in the password.
    """
    length: int
    """
    The length of the password.
    """


class PasswordRecipeTypes(str, Enum):
    MEMORABLE = "Memorable"
    PIN = "Pin"
    RANDOM = "Random"


class PasswordRecipeMemorable(BaseModel):
    type: Literal[PasswordRecipeTypes.MEMORABLE] = PasswordRecipeTypes.MEMORABLE
    parameters: PasswordRecipeMemorableInner


class PasswordRecipePin(BaseModel):
    type: Literal[PasswordRecipeTypes.PIN] = PasswordRecipeTypes.PIN
    parameters: PasswordRecipePinInner


class PasswordRecipeRandom(BaseModel):
    type: Literal[PasswordRecipeTypes.RANDOM] = PasswordRecipeTypes.RANDOM
    parameters: PasswordRecipeRandomInner


PasswordRecipe = Union[PasswordRecipeMemorable, PasswordRecipePin, PasswordRecipeRandom]


class SeparatorType(str, Enum):
    DIGITS = "digits"
    DIGITSANDSYMBOLS = "digitsAndSymbols"
    SPACES = "spaces"
    HYPHENS = "hyphens"
    UNDERSCORES = "underscores"
    PERIODS = "periods"
    COMMAS = "commas"


class WordListType(str, Enum):
    FULLWORDS = "fullWords"
    SYLLABLES = "syllables"
    THREELETTERS = "threeLetters"
