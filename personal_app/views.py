from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def personal_upload(request):
    return render(request, 'personal_app/upload.html')


@staff_member_required
def personal_list(request):
    return render(request, 'personal_app/list.html')


# Amazon Cognito 인증 공급자를 초기화합니다
# AWS.config.region = 'ap-northeast-2'; // 리전
# AWS.config.credentials = new AWS.CognitoIdentityCredentials({
#     IdentityPoolId: 'ap-northeast-2:4678854b-ede0-447c-b3f6-6aadb2f2ae2f',
# });

# {
#    "Version": "2012-10-17",
#    "Statement": [
#       {
#          "Effect": "Allow",
#          "Principal": "*",
#          "Action": [
#             "s3:DeleteObject",
#             "s3:GetObject",
#             "s3:ListBucket",
#             "s3:PutObject",
#             "s3:PutObjectAcl"
#          ],
#          "Resource": [
#             "arn:aws:s3:::mypersonal-ik",
#             "arn:aws:s3:::mypersonal-ik/*"
#          ]
#       }
#    ]
# }
#
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Sid": "Allow get requests originating from family.ikjekal.com.",
#             "Effect": "Allow",
#             "Principal": "*",
#             "Action": [
#                 "s3:DeleteObject",
#                 "s3:GetObject",
#                 "s3:ListBucket",
#                 "s3:PutObject",
#                 "s3:PutObjectAcl"
#             ],
#             "Resource": "arn:aws:s3:::mypersonal-ik/*",
#             "Condition": {
#                 "StringLike": {
#                     "aws:Referer": [
#                         "https://family.ikjekal.com/*"
#                     ]
#                 }
#             }
#         }
#     ]
# }