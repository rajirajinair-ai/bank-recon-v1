package com.bankrecon.model;

import jakarta.persistence.*;
import lombok.Data;
import java.math.BigDecimal;

@Data
@Entity
@Table(name = "bank_accounts")
public class BankAccount {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "bank_id", nullable = false)
    private Bank bank;

    @ManyToOne
    @JoinColumn(name = "company_id", nullable = false)
    private Company company;

    @Column(unique = true, nullable = false, length = 50)
    private String accountNumber;

    @Column(nullable = false, length = 50)
    private String accountType;

    @Column(length = 3)
    private String currency = "INR";

    @Column(precision = 15, scale = 2)
    private BigDecimal openingBalance = BigDecimal.ZERO;
}
