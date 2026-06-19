package com.bankrecon.model;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;
import java.util.List;

@Data
@Entity
@Table(name = "reconciliation_groups")
public class ReconciliationGroup {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(updatable = false)
    private LocalDateTime createdAt = LocalDateTime.now();

    @ManyToOne
    @JoinColumn(name = "created_by_id")
    private User createdBy;

    @Column(length = 50)
    private String status = "DRAFT";

    @OneToMany(mappedBy = "group", cascade = CascadeType.ALL)
    private List<ReconciliationItem> items;
}
