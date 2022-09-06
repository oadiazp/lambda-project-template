import argparse

import boto3

client = boto3.client('lambda')


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('project')

    return parser.parse_args()


def get_project_functions(project):
    return filter(
        lambda func: func['FunctionName'].startswith(project),
        client.list_functions()['Functions']
    )


if __name__ == '__main__':
    arguments = get_arguments()
    project = arguments.project

    functions = get_project_functions(project=project)

    for func in functions:
        mappings = client.list_event_source_mappings(
            FunctionName=func['FunctionName']
        )['EventSourceMappings']

        for mapping in mappings:
            client.delete_event_source_mapping(UUID=mapping['UUID'])

        client.delete_function(FunctionName=func['FunctionName'])
