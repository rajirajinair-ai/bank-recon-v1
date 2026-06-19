package com.bankrecon;

import com.bankrecon.model.ReportRequest;
import com.bankrecon.model.User;
import com.bankrecon.model.Role;
import com.bankrecon.repository.ReportRequestRepository;
import com.bankrecon.repository.UserRepository;
import com.bankrecon.repository.RoleRepository;
import com.bankrecon.service.ReportService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

@SpringBootTest
@ActiveProfiles("test")
class ReportServiceTests {

    @Autowired
    private ReportService reportService;

    @Autowired
    private ReportRequestRepository reportRequestRepository;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private RoleRepository roleRepository;

    @BeforeEach
    void setUp() {
        reportRequestRepository.deleteAll();
        userRepository.deleteAll();
        roleRepository.deleteAll();
    }

    @Test
    void testGenerateReport() throws InterruptedException {
        Role role = new Role();
        role.setName("Reporter");
        roleRepository.save(role);

        User user = new User();
        user.setUsername("reportadmin");
        user.setPassword("secret");
        user.setRole(role);
        userRepository.save(user);

        ReportRequest req = new ReportRequest();
        req.setRequestedBy(user);
        req.setReportType("Summary");
        reportRequestRepository.save(req);

        reportService.generateReport(req.getId());

        Thread.sleep(2500);

        ReportRequest completed = reportRequestRepository.findById(req.getId()).orElse(null);
        assertNotNull(completed);
        assertEquals("COMPLETED", completed.getStatus());
        assertEquals("/media/reports/report_" + req.getId() + ".csv", completed.getFilePath());
    }
}
