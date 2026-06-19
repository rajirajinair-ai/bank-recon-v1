package com.bankrecon.controller;

import com.bankrecon.model.ReportRequest;
import com.bankrecon.repository.ReportRequestRepository;
import com.bankrecon.service.ReportService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/reports")
public class ReportController {

    @Autowired
    private ReportRequestRepository reportRequestRepository;

    @Autowired
    private ReportService reportService;

    @PostMapping("/generate/{id}")
    public ResponseEntity<String> generateReport(@PathVariable Long id) {
        if (!reportRequestRepository.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        reportService.generateReport(id);
        return ResponseEntity.ok("Report generation started for ID: " + id);
    }
}
