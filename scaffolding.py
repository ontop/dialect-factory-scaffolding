import re
import os, os.path
from dataclasses import dataclass

@dataclass
class EnvironmentDefinition:
    pascal_name: str
    lower_name: str
    ontop_base_dir: str
    driver_classname: str

    group_id: str
    artifact_id: str
    version: str

    connection_url: str
    connection_user: str
    connection_password: str

def to_pascal_name(name: str) -> str:
    parts = re.split("[^0-9A-Za-z]", name)
    return "".join([part[0].upper() + part[1:] for part in parts if part])

def do_input() -> EnvironmentDefinition:
    print("New SQL dialect name: ", end="")
    name = input().strip()
    pascal_name = to_pascal_name(name)
    lower_name = pascal_name.lower()

    print("JDBC Driver class name: ", end="")
    classname = input().strip()

    print("ontop base directory [..]: ", end="")
    base_dir = input().strip()
    if not base_dir:
        base_dir = ".."

    print("\n\nInclude maven dependency to pom.xml [y]/n: ", end="")
    inp = input().strip().lower()
    if not inp:
        inp = "y"
    if inp == "y":
        print("    groupId: ", end="")
        group_id = input().strip()
        print("    artifactId: ", end="")
        artifact_id = input().strip()
        print("    version: ", end="")
        version = input().strip()
    else:
        group_id = ""
        artifact_id = ""
        version = ""

    print("\n\nSet up connection to database [y]/n: ", end="")
    inp = input().strip().lower()
    if not inp:
        inp = "y"
    if inp == "y":
        print("    url: ", end="")
        url = input().strip()
        print("    user: ", end="")
        user = input().strip()
        print("    password: ", end="")
        password = input().strip()
    else:
        url = "TODO-SCAFFOLD"
        user = "TODO-SCAFFOLD"
        password = "TODO-SCAFFOLD"

    return EnvironmentDefinition(pascal_name, lower_name, base_dir, classname, group_id, artifact_id, version, url, user, password)

def copy_scaffold(env: EnvironmentDefinition, path: str = "") -> None:
    full_path = os.path.join("skeleton", path)
    for item in os.listdir(full_path):
        if os.path.isdir(os.path.join(full_path, item)):
            copy_scaffold(env, os.path.join(path, item))
            continue
        full_file_path = os.path.join(full_path, item)
        file_path = os.path.join(path, item).replace("{pascalname}", env.pascal_name).replace("{lowername}", env.lower_name)
        full_ontop_path = os.path.join(env.ontop_base_dir, file_path)
        if not os.path.exists(os.path.dirname(full_ontop_path)):
            os.makedirs(os.path.dirname(full_ontop_path), exist_ok=True)
        copy_file(full_file_path, full_ontop_path, env)

def copy_file(from_path: str, to_path: str, env: EnvironmentDefinition) -> None:
    with open(from_path, "r") as file:
        full_text = file.read()
    full_text = full_text.replace("{pascalname}", env.pascal_name).replace("{lowername}", env.lower_name).replace("{classname}", env.driver_classname).replace("{url}", env.connection_url).replace("{user}", env.connection_user).replace("{password}", env.connection_password)
    with open(to_path, "w") as file:
        file.write(full_text)
        
def modify_sql_default_properties(env: EnvironmentDefinition) -> None:
    file_path = os.path.join(env.ontop_base_dir, "db", "rdb", "src", "main", "resources", "it", "unibz", "inf", "ontop", "injection", "sql-default.properties")
    with open(file_path, "r") as file:
        full_text = file.read()

    injected_reference = f"""
#{env.pascal_name}
{env.driver_classname}-symbolFactory = it.unibz.inf.ontop.model.term.functionsymbol.db.impl.{env.pascal_name}DBFunctionSymbolFactory
{env.driver_classname}-typeFactory = it.unibz.inf.ontop.model.type.impl.{env.pascal_name}DBTypeFactory
{env.driver_classname}-serializer = it.unibz.inf.ontop.generation.serializer.impl.DefaultSelectFromWhereSerializer
{env.driver_classname}-metadataProvider = it.unibz.inf.ontop.dbschema.impl.DefaultDBMetadataProvider


# Default factories
    """[1:-5]

    full_text = full_text.replace("\n\n# Default factories", injected_reference)

    with open(file_path, "w") as file:
        file.write(full_text)

def modify_test_pom(env: EnvironmentDefinition) -> None:
    if not env.group_id:
        return
    pom_path = os.path.join(env.ontop_base_dir, "test", "lightweight-tests", "pom.xml")
    with open(pom_path, "r") as file:
        full_text = file.read()

    injected_dependency = f"""
    <dependency>
            <groupId>{env.group_id}</groupId>
            <artifactId>{env.artifact_id}</artifactId>
            <version>{env.version}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>


    """[1:-5]

    full_text = full_text.replace("</dependencies>\n\n", injected_dependency)

    with open(pom_path, "w") as file:
        file.write(full_text)


def main() -> None:
    env = do_input()
    copy_scaffold(env)
    modify_sql_default_properties(env)
    modify_test_pom(env)
    

if __name__ == "__main__":
    main()