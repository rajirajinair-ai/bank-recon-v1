package com.bankrecon.model;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;

@Data
@Entity
@Table(name = "report_requests")
public class ReportRequest {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "requested_by_id", nullable = false)
    private User requestedBy;

    @Column(nullable = false, length = 100)
    private String reportType;

    @Column(columnDefinition = "JSON")
    private String parameters;

    @Column(length = 50)
    private String status = "PENDING";

    @Column(length = 255)
    private String filePath;

    @Column(updatable = false)
    private LocalDateTime createdAt = LocalDateTime.now();
}
