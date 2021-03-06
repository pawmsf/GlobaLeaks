# -*- coding: UTF-8
#   Requests
#   ********
#
# This file contains the specification of all the requests that can be made by a
# GLClient to a GLBackend.
# These specifications may be used with rest.validateMessage() inside each of the API
# handler in order to verify if the request is correct.

from globaleaks import models
from globaleaks.utils.structures import get_raw_request_format

uuid_regexp                       = r'^([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})$'
uuid_regexp_or_empty              = r'^([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})$|^$'
user_roles_regexp                 = r'^(admin|custodian|receiver)$'
user_states_regexp                = r'^(enabled|disabled)$'
email_regexp                      = r'^(([\w+-\.]){0,100}[\w]{1,100}@([\w+-\.]){0,100}[\w]{1,100})$'
email_regexp_or_empty             = r'^(([\w+-\.]){0,100}[\w]{1,100}@([\w+-\.]){0,100}[\w]{1,100})$|^$'
hidden_service_regexp             = r'^http(s?)://[0-9a-z]{16}\.onion$'
hidden_service_regexp_or_empty    = r'^http(s?)://[0-9a-z]{16}\.onion$$|^$'
https_url_regexp                  = r'^https://([0-9a-z\-]+)\.(.*)$'
https_url_regexp_or_empty         = r'^https://([0-9a-z\-]+)\.(.*)$|^$'
landing_page_regexp               = r'^(homepage|submissionpage)$'
context_selector_type_regexp      = r'^(list|cards)$'
tip_operation_regexp              = r'^(postpone|set)$'
shorturl_regexp                   = r'^(/s/[a-z0-9]{1,30})$'
longurl_regexp                    = r'^(/[a-z0-9#=_&?/-]{1,255})$'

token_regexp                      = r'([a-zA-Z0-9]{42})'
token_type_regexp                 = r'^submission$'

field_instance_regexp             = (r'^('
                                     'instance|'
                                     'reference|'
                                     'template)$')

field_type_regexp                 = (r'^('
                                     'inputbox|'
                                     'textarea|'
                                     'multichoice|'
                                     'selectbox|'
                                     'checkbox|'
                                     'tos|'
                                     'fileupload|'
                                     'date|'
                                     'fieldgroup)$')

field_attr_type_regexp            = (r'^('
                                     'int|'
                                     'bool|'
                                     'unicode|'
                                     'localized)$')

identityaccessreply_regexp        = (r'^('
                                     'pending|'
                                     'authorized|'
                                     'denied)$')

class SkipSpecificValidation: pass

DateType = r'(.*)'

# ContentType = r'(application|audio|text|video|image)'
# via stackoverflow:
# /^(application|audio|example|image|message|model|multipart|text|video)\/[a-zA-Z0-9]+([+.-][a-zA-z0-9]+)*$/
ContentType = r'(.*)'

FileDesc = {
    'name': unicode,
    'description': unicode,
    'size': int,
    'content_type': ContentType,
    'date': DateType
}

AuthDesc = {
    'username': unicode,
    'password': unicode,
}

ReceiptAuthDesc = {
    'receipt': unicode
}


TokenReqDesc = {
    'type': token_type_regexp
}

TokenAnswerDesc = {
    'human_captcha_answer': int,
    'proof_of_work_answer': int
}

SubmissionDesc = {
    'context_id': uuid_regexp,
    'receivers': [uuid_regexp],
    'identity_provided': bool,
    'answers': dict,
    'total_score': int
}

UserUserDesc = {
    'username': unicode,
    'name': unicode,
    'description': unicode,
    'public_name': unicode,
    'role': user_roles_regexp,
    'password': unicode,
    'old_password': unicode,
    'password_change_needed': bool,
    'deletable': bool,
    'state': user_states_regexp,
    'mail_address': email_regexp,
    'pgp_key_remove': bool,
    'pgp_key_fingerprint': unicode,
    'pgp_key_expiration': unicode,
    'pgp_key_public': unicode,
    'language': unicode
}

AdminUserDesc = UserUserDesc # currently the same

ReceiverReceiverDesc = {
    'username': unicode,
    'name': unicode,
    'description': unicode,
    'public_name': unicode,
    'role': user_roles_regexp,
    'password': unicode,
    'old_password': unicode,
    'password_change_needed': bool,
    'mail_address': email_regexp,
    'pgp_key_remove': bool,
    'pgp_key_fingerprint': unicode,
    'pgp_key_expiration': unicode,
    'pgp_key_public': unicode,
    'tip_notification': bool,
    'language': unicode
}

ReceiverOperationDesc = {
    'operation': unicode,
    'rtips': [uuid_regexp]
}

CommentDesc = {
    'content': unicode
}

TipOpsDesc = {
    'operation': tip_operation_regexp,
    'args': dict
}

WhisleblowerIdentityAnswers = {
    'identity_field_id': uuid_regexp,
    'identity_field_answers': dict
}

AdminNodeDesc = {
    'name': unicode,
    'description': unicode,
    'presentation': unicode,
    'footer': unicode,
    'security_awareness_title': unicode,
    'security_awareness_text': unicode,
    'whistleblowing_question': unicode,
    'whistleblowing_button': unicode,
    'whistleblowing_receipt_prompt': unicode,
    'hidden_service': hidden_service_regexp_or_empty,
    'public_site': https_url_regexp_or_empty,
    'tb_download_link': https_url_regexp,
    'languages_enabled': [unicode],
    'languages_supported': list,
    'default_language': unicode,
    'default_password': unicode,
    'maximum_namesize': int,
    'maximum_textsize': int,
    'maximum_filesize': int,
    'tor2web_admin': bool,
    'tor2web_custodian': bool,
    'tor2web_whistleblower': bool,
    'tor2web_receiver': bool,
    'tor2web_unauth': bool,
    'can_postpone_expiration': bool,
    'can_delete_submission': bool,
    'can_grant_permissions': bool,
    'allow_indexing': bool,
    'allow_unencrypted': bool,
    'disable_encryption_warnings': bool,
    'allow_iframes_inclusion': bool,
    'disable_privacy_badge': bool,
    'disable_security_awareness_badge': bool,
    'disable_security_awareness_questions': bool,
    'disable_key_code_hint': bool,
    'disable_donation_panel': bool,
    'disable_submissions': bool,
    'simplified_login': bool,
    'enable_captcha': bool,
    'enable_proof_of_work': bool,
    'enable_experimental_features': bool,
    'enable_custom_privacy_badge': bool,
    'custom_privacy_badge_tor': unicode,
    'custom_privacy_badge_none': unicode,
    'header_title_homepage': unicode,
    'header_title_submissionpage': unicode,
    'header_title_receiptpage': unicode,
    'header_title_tippage': unicode,
    'landing_page': landing_page_regexp,
    'context_selector_type': context_selector_type_regexp,
    'contexts_clarification': unicode,
    'submission_minimum_delay': int,
    'submission_maximum_ttl': int,
    'show_contexts_in_alphabetical_order': bool,
    'show_small_context_cards': bool,
    'widget_comments_title': unicode,
    'widget_messages_title': unicode,
    'widget_files_title': unicode,
    'threshold_free_disk_megabytes_high': int,
    'threshold_free_disk_megabytes_medium': int,
    'threshold_free_disk_megabytes_low': int,
    'threshold_free_disk_percentage_high': int,
    'threshold_free_disk_percentage_medium': int,
    'threshold_free_disk_percentage_low': int,
    'wbtip_timetolive': int,
    'basic_auth': bool,
    'basic_auth_username': unicode,
    'basic_auth_password': unicode
}

AdminNotificationDesc = {
    'server': unicode,
    'port': int,
    'security': unicode, # 'TLS' or 'SSL' only
    'username': unicode,
    'smtp_password': unicode,
    'source_name': unicode,
    'source_email': email_regexp,
    'tip_mail_template': unicode,
    'tip_mail_title': unicode,
    'file_mail_template': unicode,
    'file_mail_title': unicode,
    'comment_mail_template': unicode,
    'comment_mail_title': unicode,
    'message_mail_template': unicode,
    'message_mail_title': unicode,
    'admin_pgp_alert_mail_template': unicode,
    'admin_pgp_alert_mail_title': unicode,
    'pgp_alert_mail_template': unicode,
    'pgp_alert_mail_title': unicode,
    'receiver_notification_limit_reached_mail_template': unicode,
    'receiver_notification_limit_reached_mail_title': unicode,
    'tip_expiration_mail_template': unicode,
    'tip_expiration_mail_title': unicode,
    'admin_anomaly_mail_template': unicode,
    'admin_anomaly_mail_title': unicode,
    'disable_admin_notification_emails': bool,
    'disable_custodian_notification_emails': bool,
    'disable_receiver_notification_emails': bool,
    'tip_expiration_threshold': int,
    'notification_threshold_per_hour': int,
    'reset_templates': bool,
    'exception_email_address': email_regexp,
    'exception_email_pgp_key_fingerprint': unicode,
    'exception_email_pgp_key_expiration': unicode,
    'exception_email_pgp_key_public': unicode,
    'exception_email_pgp_key_remove': bool
}

AdminFieldOptionDesc = {
    'id': uuid_regexp_or_empty,
    'label': unicode,
    'presentation_order': int,
    'score_points': int,
    'trigger_field': uuid_regexp_or_empty,
    'trigger_step': uuid_regexp_or_empty
}

AdminFieldOptionDescRaw = get_raw_request_format(AdminFieldOptionDesc, models.FieldOption.localized_keys)

AdminFieldAttrDesc = {
    'id': uuid_regexp_or_empty,
    'name': unicode,
    'type': field_attr_type_regexp,
    'value': SkipSpecificValidation
}

AdminFieldAttrDescRaw = get_raw_request_format(AdminFieldAttrDesc, models.FieldAttr.localized_keys)

AdminFieldDesc = {
    'id': uuid_regexp_or_empty,
    'key': unicode,
    'instance': field_instance_regexp,
    'editable': bool,
    'template_id': uuid_regexp_or_empty,
    'step_id': uuid_regexp_or_empty,
    'fieldgroup_id': uuid_regexp_or_empty,
    'label': unicode,
    'description': unicode,
    'hint': unicode,
    'multi_entry': bool,
    'multi_entry_hint': unicode,
    'x': int,
    'y': int,
    'width': int,
    'required': bool,
    'preview': bool,
    'stats_enabled': bool,
    'type': field_type_regexp,
    'attrs': dict,
    'options': [AdminFieldOptionDesc],
    'children': list,
    'triggered_by_score': int
}

AdminFieldDescRaw = get_raw_request_format(AdminFieldDesc, models.Field.localized_keys)
AdminFieldDescRaw['options'] = [AdminFieldOptionDescRaw]
# AdminFieldDescRaw['attrs']; FIXME: we still miss a way for validating a hierarchy where
#                                    we have a variable dictionary like the attrs dictionary.

AdminStepDesc = {
    'id': uuid_regexp_or_empty,
    'label': unicode,
    'description': unicode,
    'children': [AdminFieldDesc],
    'questionnaire_id': uuid_regexp,
    'presentation_order': int,
    'triggered_by_score': int
}

AdminStepDescRaw = get_raw_request_format(AdminStepDesc, models.Step.localized_keys)
AdminStepDescRaw['children'] = [AdminFieldDescRaw]

AdminQuestionnaireDesc = {
    'id': uuid_regexp_or_empty,
    'key': unicode,
    'name': unicode,
    'show_steps_navigation_bar': bool,
    'steps_navigation_requires_completion': bool,
    'steps': [AdminStepDesc]
}

AdminQuestionnaireDescRaw = get_raw_request_format(AdminQuestionnaireDesc, models.Questionnaire.localized_keys)
AdminQuestionnaireDescRaw['steps'] = [AdminStepDescRaw]

AdminContextDesc = {
    'id': uuid_regexp_or_empty,
    'name': unicode,
    'description': unicode,
    'maximum_selectable_receivers': int,
    'tip_timetolive': int,
    'receivers': [uuid_regexp],
    'show_context': bool,
    'select_all_receivers': bool,
    'show_recipients_details': bool,
    'allow_recipients_selection': bool,
    'show_small_receiver_cards': bool,
    'enable_comments': bool,
    'enable_messages': bool,
    'enable_two_way_comments': bool,
    'enable_two_way_messages': bool,
    'enable_attachments': bool,
    'presentation_order': int,
    'recipients_clarification': unicode,
    'status_page_message': unicode,
    'show_receivers_in_alphabetical_order': bool,
    'questionnaire_id': unicode
}

AdminContextDescRaw = get_raw_request_format(AdminContextDesc, models.Context.localized_keys)

AdminReceiverDesc = {
    'id': uuid_regexp_or_empty,
    'contexts': [uuid_regexp],
    'can_delete_submission': bool,
    'can_postpone_expiration': bool,
    'can_grant_permissions': bool,
    'tip_notification': bool,
    'presentation_order': int,
    'configuration': unicode
}

AdminShortURLDesc = {
    'shorturl': shorturl_regexp,
    'longurl': longurl_regexp
}

NodeDesc = {
    'name': unicode,
    'description': unicode,
    'presentation': unicode,
    'footer': unicode,
    'security_awareness_title': unicode,
    'security_awareness_text': unicode,
    'hidden_service': hidden_service_regexp_or_empty,
    'public_site': https_url_regexp_or_empty,
    'tb_download_link': https_url_regexp,
    'languages_enabled': [unicode],
    'languages_supported': list,
    'default_language': unicode,
    'maximum_namesize': int,
    'maximum_textsize': int,
    'maximum_filesize': int,
    'tor2web_admin': bool,
    'tor2web_custodian': bool,
    'tor2web_whistleblower': bool,
    'tor2web_receiver': bool,
    'tor2web_unauth': bool,
    'can_postpone_expiration': bool,
    'can_delete_submission': bool,
    'can_grant_permissions': bool,
    'allow_indexing': bool,
    'allow_unencrypted': bool,
    'disable_privacy_badge': bool,
    'disable_security_awareness_badge': bool,
    'disable_security_awareness_questions': bool,
    'disable_key_code_hint': bool,
    'simplified_login': bool,
    'enable_captcha': bool,
    'enable_proof_of_work':  bool,
    'enable_custom_privacy_badge': bool,
    'custom_privacy_badge_tor': unicode,
    'custom_privacy_badge_none': unicode,
    'widget_comments_title': unicode,
    'widget_messages_title': unicode,
    'widget_files_title': unicode
}

TipOverviewDesc = {
    'context_id': uuid_regexp,
    'creation_date': DateType,
    'context_name': unicode,
    'id': uuid_regexp,
    'expiration_date': DateType
}

TipsOverviewDesc = [TipOverviewDesc]

FileOverviewDesc = {
    'id': uuid_regexp,
    'itip': uuid_regexp,
    'path': unicode
}

ReceiverIdentityAccessRequestDesc = {
    'request_motivation': unicode
}

CustodianIdentityAccessRequestDesc = {
    'reply': identityaccessreply_regexp,
    'reply_motivation': unicode
}

FilesOverviewDesc = [FileOverviewDesc]

StatsDesc = {
    'file_uploaded': int,
    'new_submission': int,
    'finalized_submission': int,
    'anon_requests': int,
    'creation_date': DateType
}

StatsCollectionDesc = [StatsDesc]

AnomalyDesc = {
    'message': unicode,
    'creation_date': DateType
}

AnomalyCollectionDesc = [AnomalyDesc]

ReceiverDesc = {
    'name': unicode,
    'contexts': [uuid_regexp],
    'description': unicode,
    'presentation_order': int,
    'id': uuid_regexp,
    'state': user_states_regexp
}

ReceiverCollectionDesc = [ReceiverDesc]

ContextDesc = {
    'id': uuid_regexp,
    'name': unicode,
    'description': unicode,
    'presentation_order': int,
    'receivers': [uuid_regexp],
    'select_all_receivers': bool,
    'tip_timetolive': int,
    'show_context': bool,
    'show_recipients_details': bool,
    'allow_recipients_selection': bool,
    'show_small_receiver_cards': bool,
    'maximum_selectable_receivers': int,
    'enable_comments': bool,
    'enable_messages': bool,
    'enable_two_way_messages': bool,
    'enable_attachments': bool,
    'show_receivers_in_alphabetical_order': bool
}

ContextCollectionDesc = [ContextDesc]

PublicResourcesDesc = {
    'node': NodeDesc,
    'contexts': [ContextDesc],
    'receivers': [ReceiverDesc]
}

StaticFileDesc = {
    'size': int,
    'filelocation': unicode,
    'content_type': unicode,
    'filename': unicode
}

InternalTipDesc = {
    'id': uuid_regexp,
    'new': bool,
    'context_id': uuid_regexp,
    'wb_steps': list,
    'receivers': [uuid_regexp],
    'files': [uuid_regexp],
    'creation_date': DateType,
    'expiration_date': DateType,
    'identity_provided': bool
}

WizardDesc = {
    'node': {
      'name': unicode,
      'description': unicode
    },
    'admin': {
      'password': unicode,
      'mail_address': unicode
    },
    'receiver': AdminUserDesc,
    'context': AdminContextDesc
}

ExceptionDesc = {
    'errorUrl': unicode,
    'errorMessage': unicode,
    'stackTrace': list,
    'agent': unicode
}
