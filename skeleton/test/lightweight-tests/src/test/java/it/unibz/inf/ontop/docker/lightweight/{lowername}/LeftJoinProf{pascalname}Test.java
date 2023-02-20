package it.unibz.inf.ontop.docker.lightweight.{lowername};

import com.google.common.collect.ImmutableList;
import it.unibz.inf.ontop.docker.lightweight.AbstractLeftJoinProfTest;
import it.unibz.inf.ontop.docker.lightweight.{pascalname}LightweightTest;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.sql.SQLException;

@{pascalname}LightweightTest
public class LeftJoinProf{pascalname}Test extends AbstractLeftJoinProfTest {

    private static final String PROPERTIES_FILE = "/prof/{lowername}/prof-{lowername}.properties";
    private static final String OBDA_FILE = "/prof/{lowername}/prof-{lowername}.obda";


    @BeforeAll
    public static void before() throws IOException, SQLException {
        initOBDA(OBDA_FILE, OWL_FILE, PROPERTIES_FILE);
    }

    @AfterAll
    public static void after() throws SQLException {
        release();
    }

}
