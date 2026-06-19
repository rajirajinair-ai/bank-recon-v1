package com.bankrecon.model;

import jakarta.persistence.*;
import lombok.Data;
import java.util.List;

@Data
@Entity
@Table(name = "companies")
public class Company {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true, nullable = false, length = 50)
    private String code;

    @Column(nullable = false, length = 255)
    private String name;

    @Column(length = 15)
    private String gstNumber;

    @Column(length = 10)
    private String panNumber;

    @Column(length = 3, columnDefinition = "VARCHAR(3) DEFAULT 'INR'")
    private String currency = "INR";
}
