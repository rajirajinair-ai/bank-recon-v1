package com.bankrecon.model;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "system_settings")
public class SystemSetting {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true, nullable = false, length = 100)
    private String settingKey;

    @Column(columnDefinition = "TEXT", nullable = false)
    private String value;

    @Column(columnDefinition = "TEXT")
    private String description;
}
