package com.bankrecon.service;

import com.bankrecon.model.ReportRequest;
import com.bankrecon.repository.ReportRequestRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import java.util.Optional;

@Service
public class ReportService {

    @Autowired
    private ReportRequestRepository reportRequestRepository;

    @Async
    public void generateReport(Long reportId) {
        Optional<ReportRequest> requestOpt = reportRequestRepository.findById(reportId);

        if (requestOpt.isPresent()) {
            ReportRequest report = requestOpt.get();
            report.setStatus("PROCESSING");
            reportRequestRepository.save(report);

            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }

            report.setStatus("COMPLETED");
            report.setFilePath("/media/reports/report_" + reportId + ".csv");
            reportRequestRepository.save(report);
        }
    }
}
