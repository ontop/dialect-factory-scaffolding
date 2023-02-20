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
|   |   |   sql-default.properties
|
└───test/lightweight-tests
|   |   
|   |   pom.xml
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

After running the script, run a search for them term "TODO-SCAFFOLD" to search for code segments that may be required to be changed for your implementation.

### Troubleshooting

`sql-default.properties` or `pom.xml` were not modified:
To modify existing files, this script uses a simple string replace opertation.