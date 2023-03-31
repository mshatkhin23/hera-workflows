from hera.workflows import DAG, Parameter, Task, Workflow, script, WorkflowTemplate


@script()
def out():
    print(20)


@script()
def in_(a: str, b: str):
    """Test test test."""
    print(a)
    print(b)

@script()
def echo(message: str) -> None:  # pragma: no cover
    """Prints out a message."""
    # TODO Remove function or replace with your logic
    print(message)


with Workflow(generate_name="script-param-passing-", entrypoint="d") as w:
    echo(arguments={"message": "Hello world"})
    with DAG(name="d"):
        t1: Task = out()
        t2 = in_(arguments=Parameter(name="a", value=t1.result))
        t3 = echo(arguments=Parameter(name="message", value="Hello World!"))
        t1 >> t2 >> t3

import os
yaml_path = 'tmp_manifests'
full_path = os.path.join(yaml_path, 'script-param-passing.yaml')
# if os.path.exists(yaml_path):
#     os.remove(yaml_path)
# w.to_file(yaml_path)
with open(full_path, 'w') as f:
    f.write(w.to_yaml())
