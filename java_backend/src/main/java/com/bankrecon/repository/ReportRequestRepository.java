package com.bankrecon.repository;

import com.bankrecon.model.ReportRequest;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ReportRequestRepository extends JpaRepository<ReportRequest, Long> {
}
