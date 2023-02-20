This repository contains a tool for the automatic generation of a baseline implementation of new dialect support for ontop, as explained on [the ontop website](https://ontop-vkg.org/dev/db-adapter.html)

Running this script starts a series of input requests to specify some key terms that need to be provided for the generation of the code:

- *New SQL dialect name*: The name of the SQL dialect, preferably in pascal casing (e.g. `MySQL`)
- *JDBC Driver class name*: The class name of the JDBC Driver (e.g. `com.mysql.cj.jdbc.Driver`)
- *ontop base directory*: The path to the folder containing the `ontop` repository on your device

Furthermore, this script can also set up some more required files: The maven dependency to the JDBC and the database connection properties files. To include them, please type "`y`" when asked.

**Maven Dependency**:

- *groupId*: the groupId value of the maven dependency
- *artifactId*: the artifact value of the maven dependency
- *version*: the version of the dependency

**Database Connection**

This script generates/modifies the following files:

- *url*: The JDBC connection URL
- *user*: The UID of the user for the JDBC connection
- *password*: The PWD password of the user for the JDBC connection

***

The script will generate or modify the following files:

```
ontop
│
└───db/rdb/src/main
|   |
|   └───java/it/unibz/inf/ontop/model
│   |   |
│   |   └───type/impl
|   |   |   |
|   |   |   |   NewDialectDBTypeFactory.java
│   |   |
│   |   └───term/functionsymbol/db/impl
|   |   |   |
│   |   |   │   NewDialectDBFunctionSymbolFactory.java
│   |
|   └───resources/it/unibz/inf/ontop/injection
|   |   |
|   |   |   sql-default.properties (modified)
|
└───test/lightweight-tests
|   |   
|   |   pom.xml (modified)
|   |   
|   └───src/test
|   |   |
|   |   └───java/it/unibz/inf/ontop/docker/lightweight
|   |   |   |
|   |   |   |   NewDialectLightweightTest.java
|   |   |   |
|   |   |   └───newdialect
|   |   |   |   |
|   |   |   |   |   BindWithFunctionsNewDialectTest.java
|   |   |   |   |   ConstraintNewDialectTest.java
|   |   |   |   |   DistinctInAggregateNewDialectTest.java
|   |   |   |   |   LeftJoinProfNewDialectTest.java
|   |   |
|   |   └───resources
|   |   |   |
|   |   |   └───books/newdialect  
|   |   |   |   | 
|   |   |   |   |   books-newdialect.obda
|   |   |   |   |   books-newdialect.properties
|   |   |   |
|   |   |   └───dbconstraints
|   |   |   |   |
|   |   |   |   |   dbconstraints-newdialect.properties
|   |   |   |
|   |   |   └───prof/newdialect
|   |   |   |   |
|   |   |   |   |   prof-newdialect.obda
|   |   |   |   |   prof-newdialect.properties  
|   |   |   |
|   |   |   └───university
|   |   |   |   |
|   |   |   |   |   university-newdialect.properties
```

After running the script, run a search for the term "TODO-SCAFFOLD" to search for code segments that may be required to be changed for your implementation. Depending on your inputs, this should yield results in up to 6 files.

### Troubleshooting

- `sql-default.properties` or `pom.xml` were not modified
    - To modify existing files, this script uses a simple string replace opertation. This can lead to problems, if the existing files don't follow a specific pattern. In particular, the second `<dependencies>` block in the `pom.xml` file must end with `</dependencies>` followed by at least one empty line with no symbols or other whitespace. Similarly, `sql-default.properties` must contain the comment line `# Default Properties`, with one empty line before it.
- My DBMS or JDBC does not support default schemas
    - In this case, the `.obda` files need to be modified to refer to the tables with their fully qualified names.
    - The `dbconstraints` and `university` tests do not have included `.obda` files. For them, the test classes themselves have to be rewritten to access the tables directly.