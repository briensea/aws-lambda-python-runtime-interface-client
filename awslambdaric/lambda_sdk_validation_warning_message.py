"""
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
Holds warning message that is emitted when an unhandled exception is raised during function invocation.
"""
lambda_invalid_sdk_requirements_warning_message_warning_type = "LAMBDA_WARNING"


def generate_invalid_sdk_requirement_message(
    lambda_boto3_version,
    lambda_botocore_version,
    installed_package,
    installed_package_version,
):
    return f"The deployed package {installed_package} version {installed_package_version} is not supported by the AWS SDK boto3 version {lambda_boto3_version} and botocore {lambda_botocore_version} included in the Lambda runtime. This can cause function errors, either now or after a future Lambda runtime update. We recommend packaging your own copy of the AWS SDK and its dependencies, either in your function code or as a Lambda layer. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/python-package.html"
