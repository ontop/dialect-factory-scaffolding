package it.unibz.inf.ontop.docker.lightweight.{lowername};

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSet;
import it.unibz.inf.ontop.docker.lightweight.AbstractDistinctInAggregateTest;
import it.unibz.inf.ontop.docker.lightweight.{pascalname}LightweightTest;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.sql.SQLException;

@{pascalname}LightweightTest
public class DistinctInAggregate{pascalname}Test extends AbstractDistinctInAggregateTest {

    private static final String PROPERTIES_FILE = "/university/university-{lowername}.properties";

    @BeforeAll
    public static void before() throws IOException, SQLException {
        initOBDA(OBDA_FILE, OWL_FILE, PROPERTIES_FILE);
    }

    @AfterAll
    public static void after() throws SQLException {
        release();
    }

}
