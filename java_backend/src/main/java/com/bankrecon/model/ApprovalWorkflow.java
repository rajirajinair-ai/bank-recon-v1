package com.bankrecon.model;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;

@Data
@Entity
@Table(name = "approval_workflows")
public class ApprovalWorkflow {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToOne
    @JoinColumn(name = "reconciliation_group_id", nullable = false)
    private ReconciliationGroup reconciliationGroup;

    @Column(length = 50)
    private String currentState = "DRAFT";

    private LocalDateTime updatedAt = LocalDateTime.now();
}
