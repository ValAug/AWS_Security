"""paginator example for IAM & ASG """

def get_asg_name_by_tags(region, filters):
    client = boto3.client('autoscaling', region_name=region)
    paginator = client.get_paginator('describe_auto_scaling_groups')
    page_iterator = paginator.paginate(PaginationConfig={'PageSize': 100})
    jmse_filter = 'AutoScalingGroups[] | [?'
    for tag in REQUIRED_TAGS:
        jmse_filter += f'contains(Tags[?Key==`{tag}`].Value, `{filters[tag]}`) && '
    jmse_filter = f'{jmse_filter[:-4]}]'
    return list(page_iterator.search(jmse_filter))[0]['AutoScalingGroupName']