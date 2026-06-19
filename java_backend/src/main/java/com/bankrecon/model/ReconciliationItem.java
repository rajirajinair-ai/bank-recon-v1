package com.bankrecon.model;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "reconciliation_items")
public class ReconciliationItem {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "group_id", nullable = false)
    private ReconciliationGroup group;

    @ManyToOne
    @JoinColumn(name = "bank_transaction_id")
    private BankTransaction bankTransaction;

    @ManyToOne
    @JoinColumn(name = "source_transaction_id")
    private SourceTransaction sourceTransaction;
}
