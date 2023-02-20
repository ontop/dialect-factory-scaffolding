package it.unibz.inf.ontop.docker.lightweight.{lowername};

import it.unibz.inf.ontop.dbschema.RelationID;
import it.unibz.inf.ontop.docker.lightweight.AbstractConstraintTest;
import it.unibz.inf.ontop.docker.lightweight.{pascalname}LightweightTest;
import it.unibz.inf.ontop.exception.MetadataExtractionException;
import org.junit.jupiter.api.Disabled;

import java.io.IOException;
import java.sql.SQLException;

@{pascalname}LightweightTest
public class Constraint{pascalname}Test extends AbstractConstraintTest {

    private static final String PROPERTIES_FILE = "/dbconstraints/dbconstraints-{lowername}.properties";

    public Constraint{pascalname}Test(String method) {
        super(method, PROPERTIES_FILE);
    }

}
