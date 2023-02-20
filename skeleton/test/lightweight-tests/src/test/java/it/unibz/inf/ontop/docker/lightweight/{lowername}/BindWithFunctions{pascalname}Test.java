package it.unibz.inf.ontop.docker.lightweight.{lowername};

import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableSet;
import it.unibz.inf.ontop.docker.lightweight.AbstractBindTestWithFunctions;
import it.unibz.inf.ontop.docker.lightweight.{pascalname}LightweightTest;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.sql.SQLException;

/**
 * Class to test if functions on Strings and Numerics in SPARQL are working properly.
 *
 */
@{pascalname}LightweightTest
public class BindWithFunctions{pascalname}Test extends AbstractBindTestWithFunctions {

    private static final String PROPERTIES_FILE = "/books/{lowername}/books-{lowername}.properties";
    private static final String OBDA_FILE = "/books/{lowername}/books-{lowername}.obda";

    @BeforeAll
    public static void before() throws IOException, SQLException {
        initOBDA(OBDA_FILE, OWL_FILE, PROPERTIES_FILE);
    }

    @AfterAll
    public static void after() throws SQLException {
        release();
    }

}
